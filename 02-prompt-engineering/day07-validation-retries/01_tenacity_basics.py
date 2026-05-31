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