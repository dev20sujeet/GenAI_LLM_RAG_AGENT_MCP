# Day 7 — Output Validation, Retries & Error Recovery

**Category:** Prompt Engineering (02)
**Prereqs:** Day 6 (structured outputs) shipped and run — especially Lab 3's manual validation loop.
**Default model:** `gemini-2.5-flash-lite`, key read via `os.getenv("GOOGLE_API_KEY")`.

> Day 6 ended with a hand-rolled retry loop. Day 7 replaces it with **tenacity** (the standard Python retry library) and teaches the one distinction that separates resilient LLM code from fragile code: **there are two completely different kinds of retry, and the fix for one is useless for the other.**

---

## 1. Vocabulary

| Term | Concept | Code / API |
|---|---|---|
| **Transient failure** | A temporary error that will likely succeed if you just try again: rate limits (429), server errors (5xx), network timeouts. | Retry the **same** request, with backoff |
| **Permanent failure** | An error that retrying cannot fix: bad request (400), auth failure (401/403), schema-impossible input. | Do **not** retry — fail fast |
| **Validation / semantic failure** | The call succeeded (HTTP 200) but the output is wrong: failed a Pydantic validator, missing business-rule constraint. | Retry a **different** request — feed the error back |
| **Exponential backoff** | Wait longer between each retry: 1s, 2s, 4s, 8s... Gives an overloaded server time to recover. | `wait_exponential(multiplier=1, max=30)` |
| **Jitter** | Add randomness to backoff so many clients don't retry in lockstep. ([AWS: Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)) | `wait_random_exponential(multiplier=1, max=30)` |
| **Thundering herd** | The failure mode jitter prevents: N clients all hit a rate limit at the same instant, all back off the *same* fixed amount, all retry at the *same* instant — re-creating the spike. | The reason plain exponential backoff isn't enough |
| **Idempotency** | A property where doing the operation twice has the same effect as doing it once. Pure LLM reads are safe to retry; side-effecting tool calls (charge a card) are not. | Idempotency keys for non-idempotent ops |
| **Circuit breaker** | A guard that stops sending requests after repeated failures, fails fast for a cooldown, then probes to see if the service recovered. ([Fowler](https://martinfowler.com/bliki/CircuitBreaker.html)) | `pybreaker`, or a manual counter |
| **Fallback** | A secondary path when the primary fails: a cheaper/different model, a cached answer, or a graceful default. | `try primary / except: secondary` |
| **Graceful degradation** | Returning a reduced-but-useful response instead of crashing, when nothing else works. | Return a default object with a `needs_review` flag |
| **tenacity** | The de-facto standard Python retry library. Decorator-based, composable wait/stop/retry policies. ([docs](https://tenacity.readthedocs.io/)) | `@retry(...)` |
| **`RetryError`** | What tenacity raises when retries are exhausted (unless `reraise=True`, which re-raises the original exception instead). | `from tenacity import RetryError` |

> **Style flag:** "Circuit breaker" is a metaphor borrowed from electrical engineering — the real thing is a stateful guard with three states (closed = normal, open = failing fast, half-open = probing). I'll keep saying "breaker," but that's the mechanism underneath.

---

## 2. What / Why / When

### The crux of the whole day (read this twice)

There are **two fundamentally different kinds of retry**, and people constantly conflate them:

| | Transient retry | Validation retry |
|---|---|---|
| **What failed** | The network / server (429, 503, timeout) | The model's *content* (failed a validator) |
| **HTTP status** | Non-200 (the call errored) | 200 (the call succeeded, output is just wrong) |
| **What you retry** | The **exact same** request | A **modified** request — with the error fed back |
| **Does backoff help?** | **Yes** — server needs time to recover | **No** — waiting changes nothing about the content |
| **Does feedback help?** | **No** — the server didn't read your prompt | **Yes** — the model corrects when told what was wrong |
| **Right tool** | **tenacity** (backoff + jitter) | **Manual feedback loop** or **Instructor** |

If you remember nothing else from Day 7: **backoff fixes infrastructure, feedback fixes content. Using one for the other does nothing.** A 503 doesn't care what's in your prompt; a failed validator doesn't care how long you waited.

### What this day covers
Systematic failure handling for LLM pipelines: detecting *which kind* of failure occurred, retrying transient ones correctly (backoff + jitter, capped attempts), retrying validation ones correctly (error feedback), and recovering when retries are exhausted (fallback, graceful degradation).

### Why it exists
In a notebook, you call the API once and it works. In production, at scale, over weeks:
- You **will** hit rate limits (429) during traffic spikes.
- The provider **will** have transient 5xx blips.
- Networks **will** time out.
- The model **will** occasionally produce output that fails your validators.

Code that crashes on the first 429 isn't production code. And code that retries *wrong* — hammering a rate-limited API with no backoff — makes the outage worse (thundering herd).

### When to retry vs not

| Situation | Retry? | How |
|---|---|---|
| 429 Too Many Requests | **Yes** | Backoff + jitter (tenacity) |
| 500 / 502 / 503 / 504 | **Yes** | Backoff + jitter (tenacity) |
| Network timeout / connection reset | **Yes** | Backoff + jitter (tenacity) |
| Pydantic `ValidationError` (200 response) | **Yes** | Feedback loop / Instructor |
| 400 Bad Request | **No** | Your request is malformed — fix the code |
| 401 / 403 Auth | **No** | Your key is wrong/expired — fix the env |
| 404 Model not found | **No** | Wrong model string — fix the code |
| Content-policy block | **No** (usually) | Retrying identical content gets blocked again |

---

## 3. The Problem + The Fix

### The Problem (three flavors)

**Flavor 1 — the crash.** Your batch job processes 5,000 documents. Document 1,847 hits a transient 503. No retry logic. The whole job dies. You restart from zero.

**Flavor 2 — the thundering herd.** You add a naive retry: `for _ in range(5): try: ... except: continue`. Now 200 worker threads all hit the rate limit at once, all retry instantly with no delay, all hit it again. You've turned a brief throttle into a sustained self-inflicted DDoS. Your job is *slower* than with no retries.

**Flavor 3 — the wrong fix.** A validator rejects the model's output. You wrap it in tenacity with exponential backoff. Now you wait 1s, 2s, 4s between attempts — and get the *identical wrong output* every time, because at `temperature=0` the same prompt gives the same answer. You burned 7 seconds and 4 API calls to fail exactly as you would have on attempt 1.

### The Fix

**For transient failures** — tenacity with exponential backoff *and jitter*, a *specific* retry predicate (429 + 5xx + network errors only, never 4xx client errors), and a *capped* number of attempts:

```python
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception

@retry(
    retry=retry_if_exception(is_retryable),       # only transient errors
    wait=wait_random_exponential(multiplier=1, max=30),  # backoff WITH jitter
    stop=stop_after_attempt(5),                    # cap cost/latency
    reraise=True,                                  # re-raise original, not RetryError
)
def call_model(prompt): ...
```

**For validation failures** — a feedback loop that *changes the prompt* by appending the error (the Day 6 Lab 3 pattern), or the Instructor library which does it for you:

```python
client = instructor.from_genai(genai.Client())
review = client.create(response_model=Review, messages=[...], max_retries=3)
# Instructor catches ValidationError, appends it to the prompt, retries — automatically.
```

These two fixes are **layered, not merged**: validation feedback is the inner loop (content), transient backoff is the outer loop (infrastructure). Lab 2 shows them stacked correctly.

---

## 4. Concept → Implementation Map

| Concept | tenacity / Python pattern |
|---|---|
| Retry only transient errors | `retry=retry_if_exception(is_retryable)` with a custom predicate checking status codes |
| Retry on specific exception types | `retry=retry_if_exception_type((httpx.TimeoutException,))` |
| Exponential backoff with jitter | `wait=wait_random_exponential(multiplier=1, max=30)` |
| Cap number of attempts | `stop=stop_after_attempt(5)` |
| Cap total time spent | `stop=stop_after_delay(30)` |
| Combine stop conditions | `stop=stop_after_attempt(5) | stop_after_delay(30)` |
| Log before each retry | `before_sleep=before_sleep_log(logger, logging.WARNING)` |
| Re-raise the real exception (not `RetryError`) | `reraise=True` |
| Per-request timeout (so a hung call doesn't block forever) | `http_options=types.HttpOptions(timeout=30_000)` (milliseconds; varies by SDK version) |
| Validation feedback retry | Manual loop appending `str(validation_error)` to the prompt (Day 6 Lab 3) |
| Automatic validation retry | Instructor's `max_retries=N` |
| Fallback to a second model | `try: primary() / except RetryError: secondary()` |
| Circuit breaker | `pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)` or a manual counter |

---

## 5. Best Tools / Tech Stack

| Need | Tool | Why this one |
|---|---|---|
| General-purpose retry (transient errors) | **tenacity** | The Python standard. Decorator-based, composable, used far beyond AI (DB calls, HTTP, queues). ([docs](https://tenacity.readthedocs.io/)) |
| Lighter retry alternative | **backoff** | Smaller, decorator-based; fine but less composable than tenacity ([repo](https://github.com/litl/backoff)) |
| Automatic **validation** retries | **Instructor** | Catches `ValidationError`, appends it to the prompt, retries — the feedback loop as a library feature. Cross-provider. ([docs](https://python.useinstructor.com/)) |
| Circuit breaker | **pybreaker** | Mature Python implementation of the breaker pattern ([repo](https://github.com/danielfm/pybreaker)) |
| Provider SDK built-in retries | google-genai / OpenAI / Anthropic SDKs ship some retry on transient errors | Convenient, but coarse — you'll often want tenacity for explicit control over predicate, jitter, and caps |
| Observability for retries | **LangSmith** / **Langfuse** | Surface retry counts and failure reasons per call (Category 7) |

**Course default for Day 7:** `tenacity` for transient retries (`uv add tenacity`), the manual feedback loop for validation, and we *introduce* Instructor (`uv add instructor`) as the production shortcut for validation retries.

**Rule of thumb:**
- Transient/infra errors → **tenacity** (or your SDK's built-in, if its policy is good enough).
- Validation/content errors → **Instructor**, or a manual feedback loop if you want zero extra deps.
- Repeated total failures of a dependency → **circuit breaker** so you fail fast instead of timing out every request.

---

## 6. Lab Walkthroughs

### 6.1 Scaffolding (PowerShell)

```powershell
# From repo root
New-Item -ItemType Directory -Path "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries" -Force | Out-Null

New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\01_tenacity_basics.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\02_two_loops.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\03_error_recovery.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\expected_outputs.md"
```

Dependencies:

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
uv add tenacity
uv add instructor   # used in Lab 2's "production shortcut" section
```

### 6.2 Lab 1 — `01_tenacity_basics.py`

```python
"""
01_tenacity_basics.py

Goal
----
Two parts:
  Part A: the PRODUCTION-GRADE retry predicate and decorator you'd wrap a
          real Gemini call in. Retries 429 + 5xx + network errors only.
  Part B: a DETERMINISTIC simulation so you can SEE backoff+jitter timing
          without needing the real API to actually fail.

Key teaching points
-------------------
- You retry on STATUS CODE, not just exception class. 429 is a 4xx but is
  retryable; 400/401/403 are 4xx and are NOT. A blanket "retry all
  ClientError" is a bug.
- wait_random_exponential adds JITTER. Plain exponential backoff lets many
  clients retry in lockstep (thundering herd). Jitter de-synchronizes them.
  (AWS: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- Cap attempts (stop_after_attempt). Every retry costs money and latency.
- reraise=True makes tenacity re-raise the ORIGINAL exception after the cap,
  instead of wrapping it in RetryError.
"""

import os
import time
import logging
import httpx
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types, errors
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception,
    before_sleep_log,
)

load_dotenv()
console = Console()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("day07")

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# ----- The retry predicate: retry on status code, not blindly on class -----
RETRYABLE_STATUS = {429, 500, 502, 503, 504}

def is_retryable(exc: Exception) -> bool:
    # Network-level transient errors (the SDK uses httpx under the hood)
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError)):
        return True
    # API errors: retry ONLY on the retryable status codes. 400/401/403/404 -> no.
    if isinstance(exc, errors.APIError):
        return getattr(exc, "code", None) in RETRYABLE_STATUS
    return False


# ============================ PART A: real call ============================

@retry(
    retry=retry_if_exception(is_retryable),
    wait=wait_random_exponential(multiplier=1, max=30),
    stop=stop_after_attempt(5),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def generate(prompt: str) -> str:
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text

console.rule("[bold]Part A: real Gemini call, wrapped in production retry[/bold]")
answer = generate("In one sentence, what does exponential backoff protect against?")
console.print(answer.strip())


# ====================== PART B: deterministic simulation ======================
# We can't reliably force a real 503, so we simulate one to SEE the timing.

class SimulatedTransientError(Exception):
    """Stand-in for a 503 from the real API."""

class FlakyService:
    """Fails the first `fail_times` calls, then succeeds. Lets us watch retries."""
    def __init__(self, fail_times: int):
        self.fail_times = fail_times
        self.calls = 0
    def __call__(self) -> str:
        self.calls += 1
        if self.calls <= self.fail_times:
            raise SimulatedTransientError(f"simulated 503 (call #{self.calls})")
        return f"succeeded on call #{self.calls}"

flaky = FlakyService(fail_times=3)

@retry(
    retry=retry_if_exception_type := retry_if_exception(lambda e: isinstance(e, SimulatedTransientError)),
    wait=wait_random_exponential(multiplier=0.5, max=8),  # short waits so the demo is quick
    stop=stop_after_attempt(6),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def call_flaky() -> str:
    return flaky()

console.rule("[bold]Part B: simulated transient failures, watch the backoff[/bold]")
start = time.perf_counter()
result = call_flaky()
elapsed = time.perf_counter() - start
console.print(f"{result}  (total wall time: {elapsed:.1f}s across {flaky.calls} calls)")
console.print(
    "[dim]Notice the gaps between WARNING log lines grow roughly exponentially, "
    "but with random jitter — they aren't clean 1/2/4/8.[/dim]"
)
```

Run it:

```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\01_tenacity_basics.py
```

What to notice: Part A answers in one shot (the real API rarely fails). Part B fails 3 times, and you can watch the `before_sleep` warnings with growing-but-jittered gaps before it succeeds on call #4.

### 6.3 Lab 2 — `02_two_loops.py`

```python
"""
02_two_loops.py

Goal
----
Show the two retry concerns LAYERED correctly:
  - INNER loop: validation feedback (changes the prompt, fixes content)
  - OUTER decorator: transient retry (same call + backoff, fixes infra)

Then show the PRODUCTION SHORTCUT: the Instructor library collapses the
inner validation loop into one parameter (max_retries).

Key teaching point
------------------
Backoff on a validation error is useless: at temperature=0 you'd get the
identical wrong output. The inner loop works because it CHANGES THE PROMPT
(appends the error). The outer decorator works because it retries the SAME
call after a transient blip. Different problems, different fixes.
"""

import os
import logging
import httpx
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field, ValidationError, field_validator
from google import genai
from google.genai import types, errors
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception

load_dotenv()
console = Console()
logging.basicConfig(level=logging.WARNING)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
def is_retryable(exc: Exception) -> bool:
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError)):
        return True
    if isinstance(exc, errors.APIError):
        return getattr(exc, "code", None) in RETRYABLE_STATUS
    return False


class Review(BaseModel):
    product: str
    rating: int = Field(description="Star rating, integer 1-5 inclusive")

    @field_validator("rating")
    @classmethod
    def in_range(cls, v: int) -> int:
        if not 1 <= v <= 5:
            raise ValueError(f"rating must be 1-5, got {v}")
        return v


# OUTER concern: a single API call, retried on transient infra errors only.
@retry(
    retry=retry_if_exception(is_retryable),
    wait=wait_random_exponential(multiplier=1, max=20),
    stop=stop_after_attempt(4),
    reraise=True,
)
def _raw_call(prompt: str) -> Review:
    """One transient-resilient call. May still raise ValidationError (content)."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Review,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.parsed  # raises ValidationError if the validator rejects


# INNER concern: validation feedback. Changes the prompt across attempts.
def extract_review(text: str, max_validation_retries: int = 3) -> Review:
    base = f"Extract a product review (product, rating 1-5) from:\n\n{text}"
    last_error: str | None = None
    for attempt in range(1, max_validation_retries + 1):
        prompt = base
        if last_error:
            prompt += (
                f"\n\nYour previous answer failed validation: {last_error}\n"
                f"Correct it. If the source says 10/10, clamp to the max of 5."
            )
        try:
            review = _raw_call(prompt)   # transient retries happen INSIDE here
            console.print(f"[green]validation passed on attempt {attempt}[/green]")
            return review
        except ValidationError as e:
            last_error = str(e)
            console.print(f"[yellow]attempt {attempt} content invalid:[/yellow] {last_error}")
    raise RuntimeError(f"validation failed after {max_validation_retries} attempts")


TEXT = "The Anker 737 power bank is fantastic, I'd give it 10/10. Charges everything fast."

console.rule("[bold]Manual two-loop pattern[/bold]")
review = extract_review(TEXT)
console.print(f"product={review.product!r}  rating={review.rating}/5")


# ====================== PRODUCTION SHORTCUT: Instructor ======================
# Instructor collapses the INNER validation loop into max_retries. It still
# can't fix transient infra errors for free — for that you'd layer tenacity
# or rely on the underlying SDK. But for content/validation retries it's
# the cleanest option.
console.rule("[bold]Same thing with Instructor (validation loop as a library)[/bold]")
try:
    import instructor
    ic_client = instructor.from_genai(client)  # wraps your existing genai client
    review2 = ic_client.create(
        model=MODEL,
        response_model=Review,
        max_retries=3,           # <-- the inner feedback loop, as one parameter
        messages=[{"role": "user", "content": TEXT}],
    )
    console.print(f"[cyan]instructor[/cyan] product={review2.product!r} rating={review2.rating}/5")
except Exception as e:
    console.print(f"[dim]Instructor path skipped/failed: {e}[/dim]")
    console.print("[dim](API surface varies by instructor version; check docs if this errors.)[/dim]")
```

Run it:

```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\02_two_loops.py
```

> The Instructor `from_genai` / `create` surface has shifted across versions. If that block errors, the manual two-loop above is the canonical takeaway; treat Instructor as "here's the library that does this for you" and check [its docs](https://python.useinstructor.com/) for the exact current call.

### 6.4 Lab 3 — `03_error_recovery.py`

```python
"""
03_error_recovery.py

Goal
----
What happens when retries are EXHAUSTED? You don't just crash. You:
  1. Fall back to a different model.
  2. If that also fails, return a graceful default (with a needs_review flag).
  3. Use a simple circuit breaker so a sustained outage fails FAST instead of
     making every request wait through the full retry budget.

Key teaching point
------------------
Resilience isn't "retry forever." It's "retry a bounded amount, then degrade
gracefully." A user-facing system that returns a usable default in 200ms beats
one that throws an exception after 30 seconds of doomed retries.
"""

import os
import time
import logging
import httpx
from dataclasses import dataclass
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types, errors
from tenacity import retry, stop_after_attempt, wait_random_exponential, retry_if_exception, RetryError

load_dotenv()
console = Console()
logging.basicConfig(level=logging.WARNING)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

PRIMARY = "gemini-2.5-flash-lite"
FALLBACK = "gemini-2.5-flash"   # slower/pricier, used only when primary is down

RETRYABLE_STATUS = {429, 500, 502, 503, 504}
def is_retryable(exc: Exception) -> bool:
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError)):
        return True
    if isinstance(exc, errors.APIError):
        return getattr(exc, "code", None) in RETRYABLE_STATUS
    return False


@dataclass
class Answer:
    text: str
    source: str          # which model produced it, or "default"
    needs_review: bool    # True if we fell all the way back to a default


# --- A tiny circuit breaker: after N consecutive failures, fail fast for a cooldown ---
class CircuitBreaker:
    def __init__(self, fail_max: int = 3, reset_seconds: float = 30.0):
        self.fail_max = fail_max
        self.reset_seconds = reset_seconds
        self.consecutive_failures = 0
        self.opened_at: float | None = None

    def is_open(self) -> bool:
        if self.opened_at is None:
            return False
        if time.time() - self.opened_at >= self.reset_seconds:
            # cooldown elapsed -> half-open: allow one probe
            self.opened_at = None
            self.consecutive_failures = 0
            return False
        return True

    def record_success(self):
        self.consecutive_failures = 0
        self.opened_at = None

    def record_failure(self):
        self.consecutive_failures += 1
        if self.consecutive_failures >= self.fail_max:
            self.opened_at = time.time()


breaker = CircuitBreaker()


@retry(
    retry=retry_if_exception(is_retryable),
    wait=wait_random_exponential(multiplier=1, max=15),
    stop=stop_after_attempt(3),
    reraise=True,
)
def _call(model: str, prompt: str) -> str:
    resp = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text


def ask(prompt: str) -> Answer:
    if breaker.is_open():
        console.print("[red]circuit OPEN — failing fast to default[/red]")
        return Answer("Sorry, the service is temporarily unavailable.", "default", True)

    # 1) Try primary, with its own transient retries.
    try:
        text = _call(PRIMARY, prompt)
        breaker.record_success()
        return Answer(text, PRIMARY, False)
    except (RetryError, errors.APIError) as e:
        console.print(f"[yellow]primary exhausted: {type(e).__name__}[/yellow]")

    # 2) Fall back to the secondary model.
    try:
        text = _call(FALLBACK, prompt)
        breaker.record_success()
        return Answer(text, FALLBACK, False)
    except (RetryError, errors.APIError) as e:
        console.print(f"[yellow]fallback exhausted: {type(e).__name__}[/yellow]")
        breaker.record_failure()

    # 3) Graceful degradation.
    return Answer("Sorry, the service is temporarily unavailable.", "default", True)


console.rule("[bold]Normal path (primary succeeds)[/bold]")
ans = ask("In one sentence, what is graceful degradation?")
console.print(f"[{ans.source}] needs_review={ans.needs_review}")
console.print(ans.text.strip())
```

Run it:

```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day07-validation-retries\03_error_recovery.py
```

On a healthy API you'll see the primary path succeed. The value of Lab 3 is the *shape*: bounded retries → fallback model → graceful default, with a breaker that stops you from waiting through the full retry budget on every request during a real outage.

### 6.5 Expected outputs

`expected_outputs.md` (separate file):

```markdown
# Lab 1
- Part A: one-sentence answer about backoff (succeeds first try).
- Part B: 3 WARNING lines (simulated 503s) with growing+jittered gaps, then
  "succeeded on call #4". Total wall time a few seconds.

# Lab 2
- Manual loop: attempt 1 fails ("rating must be 1-5, got 10"), attempt 2 passes
  with rating=5.
- Instructor block: rating=5 (or a skip message if the API surface differs).

# Lab 3
- "[gemini-2.5-flash-lite] needs_review=False" + a one-sentence answer.
```

### 6.6 Commit

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
git add 02-prompt-engineering/day07-validation-retries/
git commit -m "Day 7: Validation, retries, error recovery — tenacity, two-loop pattern, fallback + circuit breaker"
git push
```

---

## 7. Production Notes

### Cost & latency
- **Every retry costs a full API call.** A 5-attempt cap with a 3-document-deep validation loop is up to 15 calls for one logical operation. Budget for it; cap attempts aggressively.
- **Backoff adds latency by design.** `wait_random_exponential(max=30)` can add tens of seconds before giving up. For user-facing paths, prefer tighter caps + fast fallback over long retry budgets.
- **Set per-request timeouts** (`http_options=types.HttpOptions(timeout=...)`) so a hung connection doesn't consume your whole retry budget on one dead call. Timeout units vary by SDK version — verify in the docs.

### The idempotency trap (important for agents, Day 21+)
- Pure LLM *reads* (generate text, extract data) are safe to retry — worst case you pay twice for the same answer.
- **Side-effecting tool calls are NOT.** If your agent calls a `charge_card(amount)` tool and the call times out *after* the charge went through but *before* you got the response, a naive retry charges the customer twice. Use **idempotency keys**: generate a unique key per logical operation, send it with the request, and have the downstream system dedupe. Retrying with the same key is safe.

### When NOT to retry
- 4xx client errors except 429: 400/401/403/404 are your bug or your config. Retrying wastes money and hides the real problem. Fail fast and log loudly.
- Content-policy refusals: retrying the identical blocked content just gets blocked again. Change the request or escalate, don't loop.
- Validation failures with **no feedback**: retrying the same prompt at `temperature=0` is pointless. Either add feedback (change the prompt) or raise temperature to get a different sample.

### Circuit breakers
- Use a breaker when a dependency is *down*, not just flaky. Without one, during a full provider outage **every** request waits through its entire retry budget before failing — you've multiplied your latency by the retry count across your whole traffic.
- The breaker's three states: closed (normal), open (fail fast for a cooldown), half-open (let one probe through to test recovery). `pybreaker` implements this; the Lab 3 version is a minimal hand-roll.

### Observability
- Log *which kind* of failure occurred (transient vs validation vs permanent) and the retry count per operation. "Retries spiked at 14:03" is your earliest signal of a provider degradation.
- Track a `needs_review` / degraded-response rate as a first-class metric. A rising graceful-degradation rate means your fallbacks are doing more work than they should.

### Tips & tricks
- `reraise=True` almost always — debugging a wrapped `RetryError` that hides the real 503 is miserable.
- Put the cheapest model in the primary slot and a stronger/different one in the fallback slot; an outage is often provider- or model-specific, so a *different* model is a better fallback than the same model again.
- Jitter is not optional at scale. `wait_exponential` (no jitter) re-creates the thundering herd; `wait_random_exponential` is the safe default.

---

## 8. Interview Questions

> These are the questions that test whether you actually own retry/resilience. The model answers lead with the crux.

### 🟢 Conceptual

<details>
<summary>Q1. There are two fundamentally different kinds of retry in an LLM pipeline. What are they, and why does the fix for one do nothing for the other?</summary>

**Crux:** Backoff fixes infrastructure; feedback fixes content. They are not interchangeable.

- **Transient retry** handles non-200 failures — 429, 5xx, timeouts. The *server* failed. You retry the **exact same request** with **exponential backoff + jitter** to give the server time to recover. Feeding error text into the prompt does nothing, because the server never read your prompt.

- **Validation/semantic retry** handles 200 responses whose *content* is wrong — failed a Pydantic validator or business rule. The *model* produced bad output. You retry a **modified request** that **feeds the error back** so the model corrects. Backoff does nothing, because at `temperature=0` waiting just reproduces the identical wrong answer.

The classic bug is wrapping a `ValidationError` in tenacity with exponential backoff: you wait 1/2/4/8 seconds to get the same wrong output four times. Diagnosing which kind of failure you have *first* is the whole skill.
</details>

<details>
<summary>Q2. What is jitter, what failure does it prevent, and why isn't plain exponential backoff enough?</summary>

**Crux:** Jitter de-synchronizes clients so they don't retry in lockstep.

Plain exponential backoff makes every client wait the *same* deterministic amount (1s, then 2s, then 4s). If N clients all hit a rate limit at the same instant, they all back off the same amount and all retry at the *same* next instant — re-creating the exact spike that caused the throttle. This is the **thundering herd**.

Jitter adds randomness to each wait (`wait_random_exponential`), spreading retries across a window so the load smooths out instead of pulsing. At any real scale, jitter isn't a nice-to-have — backoff without it is actively harmful. ([AWS: Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/))
</details>

<details>
<summary>Q3. Which HTTP errors should you retry, and which should you never retry? Why does a blanket "retry all client errors" rule break?</summary>

**Crux:** Retry on the *status code*, not the exception class.

Retry: **429** (rate limit — transient by definition), **500/502/503/504** (server-side blips), and network-level errors (timeouts, connection resets).

Never retry: **400** (your request is malformed), **401/403** (auth — your key is wrong/expired), **404** (wrong model string). These are *your* bug; retrying wastes money and time and hides the real cause.

The trap: 429 is a 4xx, same class as 400/401/403. A predicate like `retry_if_exception_type(ClientError)` retries the auth failures too, and a predicate like `retry_if_exception_type(ServerError)` *misses* the 429. The correct predicate checks the status code against an explicit retryable set: `{429, 500, 502, 503, 504}`.
</details>

### 🟡 Practical

<details>
<summary>Q4. Write a tenacity decorator for a Gemini call that retries correctly. Name every parameter choice.</summary>

**Crux:** correct predicate + jitter + capped attempts + reraise.

```python
RETRYABLE = {429, 500, 502, 503, 504}
def is_retryable(exc):
    if isinstance(exc, (httpx.TimeoutException, httpx.ConnectError, httpx.ReadError)):
        return True
    if isinstance(exc, errors.APIError):
        return getattr(exc, "code", None) in RETRYABLE
    return False

@retry(
    retry=retry_if_exception(is_retryable),               # only transient
    wait=wait_random_exponential(multiplier=1, max=30),   # backoff WITH jitter
    stop=stop_after_attempt(5),                            # cap cost & latency
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,                                          # surface the real error
)
def generate(prompt): ...
```

Each choice: predicate excludes 4xx-except-429 so we don't retry our own bugs; `wait_random_exponential` for jitter; `stop_after_attempt(5)` because retries cost money; `reraise=True` so I debug a `503`, not a `RetryError` wrapping it.
</details>

<details>
<summary>Q5. A validator keeps rejecting the model's output. You wrapped the call in tenacity with backoff and it still fails identically every time. What's wrong and how do you fix it?</summary>

**Crux:** You applied a transient fix to a content problem.

The output failed *validation* — the call returned 200, the content was just wrong. tenacity retries the **same request**; at `temperature=0` the same prompt yields the same output, so you get the identical failure 5 times, slower.

The fix is a **feedback loop**, not backoff: catch the `ValidationError`, append its text to the prompt ("your previous answer failed: rating must be 1-5, got 10 — correct it"), and re-call. The *changed prompt* is what produces a different, valid answer. Or use Instructor's `max_retries`, which does exactly this loop for you. Backoff is irrelevant here.
</details>

<details>
<summary>Q6. How do you layer transient retries and validation retries together without them interfering?</summary>

**Crux:** Validation feedback is the inner loop (changes the prompt); transient backoff is the outer concern (same call). Nest, don't merge.

```python
@retry(retry=retry_if_exception(is_retryable), wait=wait_random_exponential(...), stop=stop_after_attempt(4), reraise=True)
def _raw_call(prompt) -> Review:
    return client.models.generate_content(...).parsed   # may raise ValidationError

def extract(text, max_validation_retries=3):
    last_error = None
    for _ in range(max_validation_retries):
        prompt = base if not last_error else base + f"\nPrevious failed: {last_error}\nFix it."
        try:
            return _raw_call(prompt)        # transient retries happen INSIDE
        except ValidationError as e:
            last_error = str(e)
    raise RuntimeError("validation failed")
```

The transient decorator handles 503s on each individual call; the feedback loop handles content correction across calls. A `ValidationError` is NOT in the transient predicate, so it propagates straight to the feedback loop — they never fight.
</details>

### 🔴 System design

<details>
<summary>Q7. Design resilience for a customer-facing LLM endpoint with a p95 latency budget of 2 seconds. How do retries fit?</summary>

**Crux:** For user-facing paths, prefer fast fallback over long retry budgets — a usable default in 200ms beats a correct answer after 30s of doomed retries.

Design:
- **Tight transient retry**: 1–2 attempts max with short backoff. A 5-attempt, 30s-max policy is for batch jobs, not a 2s budget.
- **Per-request timeout** well under budget so a hung call can't blow p95.
- **Fast fallback chain**: primary model → cached/cheaper model → graceful default with a `needs_review` flag. The default returns instantly.
- **Circuit breaker** so that during a provider outage you fail fast (and serve defaults) instead of every request burning its full retry budget.
- **Async/queue the slow path**: if a high-quality answer genuinely needs a reasoning model that exceeds budget, return an immediate acknowledgment and deliver the full answer via callback/notification.

Metric to watch: graceful-degradation rate. If it climbs, your budget or your provider is the problem, and users are silently getting worse answers.
</details>

<details>
<summary>Q8. Your agent retries a tool call after a timeout and a customer gets charged twice. What went wrong, and how do you make retries safe for side-effecting operations?</summary>

**Crux:** LLM reads are idempotent and safe to retry; side-effecting tool calls are not. Use idempotency keys.

What happened: the `charge_card` call succeeded server-side, but the response timed out before your client saw it. Your retry logic, which is correct for *reads*, re-issued the charge — and the payment system, having no way to know it was the same logical operation, charged again.

Fix: **idempotency keys**. Generate a unique key per logical operation (e.g., a UUID tied to the order), send it with the request, and require the downstream system to dedupe on it — a second request with the same key returns the original result instead of re-executing. Then retrying is safe by construction.

Broader rule: classify every tool as idempotent (safe to retry freely) or non-idempotent (retry only with an idempotency key, or not at all). Never apply your read-path retry policy blindly to write operations.
</details>

<details>
<summary>Q9. When is a circuit breaker the right tool, and what does it protect that retries-with-backoff alone do not?</summary>

**Crux:** Backoff handles *flaky*; a breaker handles *down*. Without a breaker, a full outage makes every request pay the entire retry budget before failing.

Retries + backoff assume the dependency will probably recover *soon* — right for transient blips. But during a sustained outage, every single incoming request dutifully retries 5 times with growing backoff before giving up. You've multiplied your latency by the retry count across *all* traffic, and you keep hammering a service that's already down.

A circuit breaker detects the sustained failure (N consecutive failures), **opens** (fails fast, serving fallbacks immediately for a cooldown), then goes **half-open** to let a single probe test recovery before **closing** again. It converts "every request times out slowly" into "requests fail instantly and cheaply until the dependency is back." Use it for any dependency whose outage you can't afford to wait on per-request.
</details>

---

## End of Day 7

The one thing to carry forward: **diagnose the failure kind before you pick the fix.** Transient → backoff + jitter (tenacity). Validation → feedback loop (manual or Instructor). Exhausted → fallback + graceful degradation. Down → circuit breaker. Side-effecting → idempotency keys.

**Next:** Day 8 — Self-consistency, ReAct, and prompt chaining. We start composing these techniques into multi-step reasoning workflows, which is the on-ramp to agents (Category 4).

Run the three labs and push back on anything before we move on.
