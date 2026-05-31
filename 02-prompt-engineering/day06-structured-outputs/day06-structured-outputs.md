# Day 6 — Structured Outputs

**Category:** Prompt Engineering (02)
**Prereqs:** Days 3 (system prompts), 4 (few-shot), 5 (CoT) shipped and run.
**Default model:** `gemini-2.5-flash-lite` with `thinking_budget=0`.

> Day 5 made the model produce good **text**. Day 6 makes it produce typed **objects** your downstream code can use without parsing. This is the bridge between prompt engineering and real software.

---

## 1. Vocabulary

| Term | Concept | Code / API |
|---|---|---|
| **Structured output** | Model output constrained to a typed schema (instead of free-form text), parsed into a native object. | `resp.parsed` returns a Pydantic model instance |
| **JSON Schema** | A spec for describing the shape of JSON: types, fields, required vs optional, enums, nested objects. ([spec](https://json-schema.org/)) | `model.model_json_schema()` |
| **JSON mode (legacy)** | First-generation feature (~late 2023): guarantees the output is **valid JSON** but does NOT guarantee it matches your schema. ([OpenAI blog, Nov 2023](https://openai.com/index/new-models-and-developer-products-announced-at-devday/)) | `response_format={"type": "json_object"}` (legacy OpenAI) |
| **Structured Outputs (modern)** | Second-generation feature (Aug 2024 for OpenAI, similar for Gemini): guarantees the output **matches your schema** via constrained decoding. ([OpenAI blog, Aug 2024](https://openai.com/index/introducing-structured-outputs-in-the-api/)) | `response_mime_type="application/json"` + `response_schema=YourModel` |
| **Constrained decoding** | Technique where the sampler is restricted at each step to only tokens that keep the partial output valid per a grammar (finite-state machine over the JSON schema). | Implemented inside the provider; you don't touch it directly |
| **Pydantic v2 `BaseModel`** | The Python class you subclass to define a schema. Pydantic v2 is the universal AI-ecosystem standard (FastAPI, LangChain, LlamaIndex, Instructor all use it). ([docs](https://docs.pydantic.dev/latest/)) | `class Person(BaseModel): name: str` |
| **Field description** | Documentation attached to a field that the LLM reads as part of the schema. This is one of the highest-ROI prompt-engineering moves available. | `name: str = Field(description="The person's full legal name")` |
| **`Literal[...]`** | Python typing primitive that pins a value to a fixed set of options. Simplest way to constrain a string field. | `status: Literal["paid", "unpaid", "overdue"]` |
| **`Enum`** | Alternative to `Literal` when you need richer behavior (methods, iteration). For pure string-set constraints, `Literal` is lighter. | `class Status(str, Enum): PAID = "paid"` |
| **`ValidationError`** | Pydantic's exception when input data doesn't satisfy the schema (wrong type, missing required field, custom validator failed). | `from pydantic import ValidationError` |
| **Field validator** | A custom function attached to a field that runs after type-checking. Catches semantic violations that the JSON schema can't express. | `@field_validator("rating")` |
| **Instructor** | The dominant cross-provider library for structured outputs in Python. Wraps OpenAI/Anthropic/Gemini/Cohere with a unified Pydantic-based API and adds automatic validation retries. Created by Jason Liu. ([docs](https://python.useinstructor.com/)) | `client = instructor.from_genai(client)` then `client.messages.create(response_model=Person, ...)` |
| **Tool / function calling** | A related but distinct pattern: the model emits a JSON object describing a "call" to a named function. Used for agents (Day 22). Internally also uses constrained decoding. | `tools=[my_tool]` |

> **Style flag:** When people say "the LLM **reads** the schema," that's the metaphor. The real mechanism: the provider takes your Pydantic model, runs `model_json_schema()`, and either (a) injects that schema into the system prompt OR (b) compiles a finite-state machine that constrains decoding. Most production providers in 2026 do both — schema in the prompt for context, FSM at sampling time for the guarantee.

---

## 2. What / Why / When

### What it is
You declare the shape of the answer as a Pydantic class. The provider takes that class, generates JSON that matches it (using constrained decoding for guarantees), and you get back a typed Python object — no parsing, no try/except around `json.loads`, no regex.

```python
class Person(BaseModel):
    name: str
    age: int
    occupation: str

resp = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="Extract info: John Doe is a 32-year-old engineer.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Person,
    ),
)

person: Person = resp.parsed      # already a typed Pydantic object
print(person.name, person.age)    # "John Doe" 32
```

### Why it exists

Three reasons, in order of importance:

1. **Composability.** Free-form text is a dead end for software. To hand the model's output to a database, an API call, or another function, you need a typed object. Structured outputs collapse the "model → text → parser → object" pipeline into "model → object."

2. **Reliability.** Before structured outputs, you used regex or fragile prompt instructions ("output JSON only, no preamble"). The model would mostly comply, then occasionally wrap the JSON in markdown fences, add a chatty preamble, or hallucinate fields. Constrained decoding makes this category of failure impossible.

3. **Documentation as code.** Your schema IS the contract. Field descriptions guide the model. Type hints catch bugs. The schema is checkable, diffable, and reusable across calls. It's prompt engineering that lives in your type system.

### When to USE structured outputs

| Task | Good fit? | Why |
|---|---|---|
| Information extraction (resume parsing, invoice parsing, web scraping cleanup) | **Strongly yes** | This is what the feature was built for |
| Multi-label classification with confidence scores | **Yes** | `class Result: labels: list[Label]; confidence: float` |
| Tool/function input generation in agents | **Yes** | All major agent frameworks rely on this |
| RAG with citations (Day 14) | **Yes** | `class Answer: text: str; citations: list[Citation]` |
| Form filling, data cleanup, normalization | **Yes** | Typed normalization is the point |
| Multi-step reasoning where you want the reasoning AND the answer | **Yes** | `class Result: reasoning: str; answer: int` — CoT in a schema |

### When to SKIP structured outputs

| Task | Skip? | Why |
|---|---|---|
| Chat with humans | **Yes, skip** | Humans read prose, not JSON |
| Creative writing, brainstorming | **Skip** | Forcing structure on creativity wastes the model |
| One-token classification ("positive/negative") | **Probably skip** | Adds schema overhead for a single token; just parse the word |
| Tasks where you want to chain to ANOTHER LLM call | **Sometimes skip** | Text → text → text composes naturally; structure → text is a translation step |
| When you only need a single value with no metadata | **Skip** | Overkill; ask for the value, parse it |

### Structured outputs vs JSON mode vs tool calling

| Feature | Guarantees | Best for |
|---|---|---|
| **JSON mode (legacy)** | Valid JSON only — schema is a hope, not a guarantee | Don't use it in new code; superseded by structured outputs |
| **Structured outputs** | Output matches your Pydantic/JSON schema | Pure extraction, data tasks, single-call structured responses |
| **Tool / function calling** | Output is one of N named "tools" with typed args | Agents, multi-tool workflows, when the model picks WHICH thing to call |

The line blurs because both structured outputs and tool calling use constrained decoding under the hood — the difference is mostly API ergonomics and intent.

---

## 3. The Problem + The Fix

### The Problem

You're processing 10,000 customer reviews. For each one, you need to extract: product name, star rating (1–5), whether shipping was mentioned, and a one-line summary. You ask the model:

> "Extract product name, rating 1-5, shipping mentioned (yes/no), and a short summary. Output as JSON."

The model usually obliges. But across 10,000 calls:
- 47 wrap the JSON in ` ```json ... ``` ` markdown fences → `json.loads` fails
- 132 add a preamble: `"Sure! Here's the JSON: {...}"` → `json.loads` fails
- 9 use `"rating": "five"` instead of an integer → your downstream code crashes
- 213 omit the `shipping_mentioned` field entirely → `KeyError`
- A handful invent an extra field `"vibe": "good"` → silently swallowed but unexpected
- 4 hallucinate a non-existent rating like `"rating": 7` → silently bad data

You write defensive code. Regex to strip fences. Try/except around `json.loads`. Default-value lookups for missing keys. Type-coercion for `"five"` → `5`. It's 80 lines of glue, it's buggy, and it doesn't catch the hallucinated rating because that's still a valid integer.

### The Fix

Declare the shape in Pydantic. Hand it to the provider:

```python
from pydantic import BaseModel, Field, field_validator
from typing import Literal

class ReviewInfo(BaseModel):
    product_name: str = Field(description="The product being reviewed, as named in the text")
    rating: int = Field(description="Star rating, integer 1-5")
    shipping_mentioned: Literal["yes", "no"]
    summary: str = Field(description="One sentence under 20 words")

    @field_validator("rating")
    @classmethod
    def rating_in_range(cls, v):
        if not 1 <= v <= 5:
            raise ValueError("rating must be 1-5")
        return v

resp = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"Extract info from this review:\n\n{review_text}",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ReviewInfo,
    ),
)
info: ReviewInfo = resp.parsed
```

What you eliminated:
- No markdown fences (constrained decoding never emits them)
- No preamble (output starts with `{`, must end with `}`)
- `rating` is guaranteed to be an int (not a string)
- All required fields are present (constrained decoding can't end the JSON early)
- The rating range is caught by the field validator → you handle it explicitly with a retry (Lab 3)

80 lines of glue → one schema declaration.

---

## 4. Concept → Implementation Map

| Concept | Pydantic / Gemini pattern |
|---|---|
| Required string field | `name: str` |
| Optional field with default | `nickname: str \| None = None` |
| Constrained string set | `status: Literal["active", "inactive"]` |
| Field with description (LLM reads this) | `name: str = Field(description="Full legal name")` |
| Integer with range | `age: int` + `@field_validator("age")` checking range |
| Nested object | `address: Address` where `Address(BaseModel)` is defined separately |
| List of objects | `items: list[LineItem]` |
| Enum (when you need methods) | `class Status(str, Enum): ...; status: Status` |
| Date / datetime | `created_at: datetime` — auto-parses ISO strings |
| Configure Gemini for structured output | `response_mime_type="application/json"` + `response_schema=Model` |
| Get the typed object | `resp.parsed` (Gemini), or `resp.choices[0].message.parsed` (OpenAI) |
| Get the raw JSON | `resp.text` (Gemini) |
| Validate manually | `Model.model_validate(json_dict)` |
| Re-emit as JSON | `model_instance.model_dump_json()` |
| Inspect the JSON schema | `Model.model_json_schema()` |

---

## 5. Best Tools / Tech Stack

| Need | Tool | Why this one |
|---|---|---|
| Schema definition (universal) | **Pydantic v2** | The Python AI ecosystem's de facto standard. FastAPI, LangChain, LlamaIndex, Instructor, Anthropic SDK all use it. ([docs](https://docs.pydantic.dev/latest/)) |
| Single-provider structured output (Gemini) | Native `google-genai` SDK with `response_schema` | Zero dependencies beyond what you already have. Use this for Day 6 labs. |
| Single-provider structured output (OpenAI) | Native OpenAI SDK with `response_format=ModelClass` ([docs](https://platform.openai.com/docs/guides/structured-outputs)) | Same story — use the native API if you're committed to one provider |
| Cross-provider structured output | **Instructor** | Jason Liu's library; the industry-standard wrapper. One API across OpenAI/Anthropic/Gemini/Cohere/Mistral, automatic validation retries, streaming support. ([docs](https://python.useinstructor.com/)) |
| Open-source / self-hosted constrained decoding | **Outlines** | The reference open-source library for constrained generation; used by Hugging Face inference, vLLM. ([repo](https://github.com/dottxt-ai/outlines)) |
| Prompt-level evaluation of structured outputs | **Promptfoo** | YAML-defined assertions including JSON schema validation ([docs](https://www.promptfoo.dev/)) |
| Schema visualization / docs | `model.model_json_schema()` + any JSON Schema viewer | Pydantic emits canonical JSON Schema; pipe it into [json-schema-viewer.vercel.app](https://json-schema-viewer.vercel.app/) when debugging |

**Course default for Day 6 labs:** Pydantic v2 + native `google-genai` SDK. We'll introduce **Instructor** explicitly in Day 7 (retries) and use it once we go cross-provider.

**Rule of thumb:**
- Locked to one provider → native API
- Multi-provider, want consistent retries and DX → Instructor
- Self-hosting open models → Outlines (inside vLLM / TGI)

---

## 6. Lab Walkthroughs

### 6.1 Folder and file scaffolding (PowerShell)

```powershell
# From repo root E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
New-Item -ItemType Directory -Path "02-prompt-engineering\day06-structured-outputs" -Force | Out-Null
Set-Location ".\02-prompt-engineering\day06-structured-outputs"

New-Item -ItemType File 01_basic_structured.py
New-Item -ItemType File 02_nested_and_enums.py
New-Item -ItemType File 03_validation_retries.py
New-Item -ItemType File expected_outputs.md
```

Also make sure Pydantic is on your project:

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
uv add pydantic
```

(If your `pyproject.toml` already has `pydantic`, this is a no-op.)

### 6.2 Lab 1 — `01_basic_structured.py`

```python
"""
01_basic_structured.py

Goal
----
Extract a typed Person object from a paragraph. Show that:
  - resp.parsed returns a Pydantic instance directly
  - Pydantic does the type-checking for you
  - Field descriptions guide the model

Key teaching points
-------------------
- response_mime_type="application/json" + response_schema=ModelClass is the
  two-line incantation for Gemini structured output.
- The Field(description=...) text is part of the schema and is visible to
  the model. Write it like a prompt, not like internal documentation.
- We still set thinking_budget=0 to keep the teaching loop fast and cheap.
  In production with reasoning models, leave it on for hard extraction tasks.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-lite"


class Person(BaseModel):
    name: str = Field(description="The person's full name as it appears in the text")
    age: int = Field(description="Age in years; integer only")
    occupation: str = Field(description="Their job title or role")
    company: str | None = Field(
        default=None,
        description="Employer name if mentioned, otherwise null",
    )


TEXT = (
    "Sujeet Kumar is a 41-year-old senior software engineer at Anthropic, "
    "currently focused on AI agent infrastructure."
)

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Person,
    thinking_config=types.ThinkingConfig(thinking_budget=0),
    temperature=0.0,
)

resp = client.models.generate_content(
    model=MODEL,
    contents=f"Extract the person's information from this text:\n\n{TEXT}",
    config=config,
)

# Two ways to look at the output:
print("Raw JSON returned by the model:")
print(resp.text)
print()

# resp.parsed is already a validated Pydantic Person object.
person: Person = resp.parsed
print(f"Typed object: {person!r}")
print(f"  .name      = {person.name}")
print(f"  .age       = {person.age}     (type: {type(person.age).__name__})")
print(f"  .company   = {person.company}")

# Bonus: see what the model actually received as the schema.
# This is what you should mentally treat as part of your prompt.
import json
print("\nJSON schema that the model conditioned on:")
print(json.dumps(Person.model_json_schema(), indent=2))
```

Run it:

```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day06-structured-outputs\01_basic_structured.py
```

What to notice:
- `resp.text` is clean JSON — no markdown fences, no preamble.
- `resp.parsed` is a real Python object. Autocomplete works. `mypy` works.
- The schema you see at the bottom is what the model conditioned on. Read it. That's your prompt.

### 6.3 Lab 2 — `02_nested_and_enums.py`

```python
"""
02_nested_and_enums.py

Goal
----
Show that:
  - Nested Pydantic models work transparently (Address inside Customer)
  - Lists of objects work transparently (line items inside Invoice)
  - Literal[...] constrains a string field to a fixed set (status)
  - Field descriptions on the inner classes ALSO get read by the model

This is the shape of most real extraction tasks: hierarchical data with
constrained enumerated fields.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-lite"


class Address(BaseModel):
    street: str = Field(description="Street address including number")
    city: str
    state: str = Field(description="Two-letter US state code, e.g. IA")
    zip: str = Field(description="US ZIP code, 5 or 9 digits")


class LineItem(BaseModel):
    description: str = Field(description="What was purchased")
    quantity: int = Field(description="Number of units, integer >= 1")
    unit_price: float = Field(description="Price per unit in USD")


class Invoice(BaseModel):
    invoice_number: str
    customer_name: str
    billing_address: Address
    line_items: list[LineItem] = Field(description="One entry per distinct line on the invoice")
    status: Literal["paid", "unpaid", "overdue"] = Field(
        description="Payment status; pick the single most accurate one"
    )
    total: float = Field(description="Total amount due in USD")


# A messy real-world-ish invoice paragraph. Note the deliberate noise:
# extra context, informal phrasing, the status is implied not stated.
INVOICE_TEXT = """
Invoice #INV-2026-0418 for Sujeet Kumar, billing to 1234 River Dr,
Bettendorf IA 52722. Two items: 3 units of "Adjustable Standing Desk"
at $349 each, and 1 unit of "Ergonomic Chair" at $480. Total comes to
$1527. The customer paid by ACH on the 22nd of April so this one's
settled.
"""

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Invoice,
    thinking_config=types.ThinkingConfig(thinking_budget=0),
    temperature=0.0,
)

resp = client.models.generate_content(
    model=MODEL,
    contents=f"Extract a structured invoice from this text:\n\n{INVOICE_TEXT}",
    config=config,
)

invoice: Invoice = resp.parsed
print(f"Invoice #{invoice.invoice_number}")
print(f"  Customer: {invoice.customer_name}")
print(f"  Status:   {invoice.status}")
print(f"  Address:  {invoice.billing_address.street}, "
      f"{invoice.billing_address.city}, "
      f"{invoice.billing_address.state} {invoice.billing_address.zip}")
print(f"  Items ({len(invoice.line_items)}):")
for item in invoice.line_items:
    line_total = item.quantity * item.unit_price
    print(f"    - {item.quantity}x {item.description} @ ${item.unit_price:.2f} = ${line_total:.2f}")
print(f"  Total:    ${invoice.total:.2f}")

# Sanity check: does the sum of line items match the reported total?
# This is exactly the kind of cross-field check structured output makes trivial.
computed = sum(i.quantity * i.unit_price for i in invoice.line_items)
if abs(computed - invoice.total) > 0.01:
    print(f"\nWARNING: line items sum to ${computed:.2f} but invoice says ${invoice.total:.2f}")
else:
    print("\nLine items match the reported total.")
```

Run it:

```powershell
uv run python .\02_nested_and_enums.py
```

What to notice:
- The model picked `status="paid"` from natural-language context ("this one's settled"), constrained by `Literal["paid", "unpaid", "overdue"]`.
- `invoice.billing_address` is itself a typed `Address` object — full dot-access, not a dict.
- `invoice.line_items` is a `list[LineItem]` — you can iterate, sum, filter.
- The cross-field check (sum of line items = total) is the kind of validation worth doing post-hoc; the schema can't enforce it but your code can.

### 6.4 Lab 3 — `03_validation_retries.py`

```python
"""
03_validation_retries.py

Goal
----
Show that schemas alone aren't enough. Pydantic field validators catch
SEMANTIC violations the JSON schema can't express (range, regex, custom
rules). When validation fails, retry with the error fed back to the model.

This is the manual version of what the Instructor library does for free.
We do it manually first so you understand the loop. Day 7 will introduce
tenacity for general retry policy with backoff.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError, field_validator
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-lite"


class Review(BaseModel):
    product: str
    rating: int = Field(description="Star rating, integer between 1 and 5 inclusive")
    summary: str = Field(description="One-sentence summary under 20 words")

    @field_validator("rating")
    @classmethod
    def rating_in_range(cls, v: int) -> int:
        if not 1 <= v <= 5:
            raise ValueError(f"rating must be between 1 and 5, got {v}")
        return v

    @field_validator("summary")
    @classmethod
    def summary_word_count(cls, v: str) -> str:
        wc = len(v.split())
        if wc > 20:
            raise ValueError(f"summary must be under 20 words, got {wc}")
        return v


# Deliberately hostile input: the user rated "10/10" — the model is likely
# to faithfully emit rating=10, which the validator will reject.
REVIEW_TEXT = (
    "The new Logitech MX Master 4 mouse is unbelievable. I rate it 10/10! "
    "Build quality is top tier, the scroll wheel is smooth, battery lasts forever, "
    "and the customizable buttons saved me hours on my workflow this week."
)


def extract_review(text: str, max_retries: int = 3) -> Review:
    """Extract a Review with validation-feedback retries."""

    base_prompt = f"Extract a structured product review from this text:\n\n{text}"
    last_error: str | None = None

    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Review,
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        temperature=0.0,
    )

    for attempt in range(1, max_retries + 1):
        # On retries, append the previous error so the model can correct itself.
        prompt = base_prompt
        if last_error:
            prompt += (
                f"\n\nYour previous response failed validation with this error:\n"
                f"{last_error}\n"
                f"Re-emit the JSON correcting this issue. Stay faithful to the "
                f"source text — if the source says 10/10, clamp to 5 (the max)."
            )

        resp = client.models.generate_content(model=MODEL, contents=prompt, config=config)

        try:
            # resp.parsed runs Pydantic validation, including custom validators.
            review: Review = resp.parsed
            print(f"[attempt {attempt}] succeeded")
            return review
        except ValidationError as e:
            last_error = str(e)
            print(f"[attempt {attempt}] ValidationError:\n  {last_error}\n")

    raise RuntimeError(f"All {max_retries} attempts failed. Last error: {last_error}")


review = extract_review(REVIEW_TEXT)
print()
print(f"Product:  {review.product}")
print(f"Rating:   {review.rating} / 5")
print(f"Summary:  {review.summary}")
```

Run it:

```powershell
uv run python .\03_validation_retries.py
```

What you'll typically see:
- Attempt 1: model emits `rating=10` (faithful to source), validator rejects.
- Attempt 2: model reads the error feedback, clamps to 5.
- Final output is a valid `Review` with `rating=5`.

> Note: with `temperature=0.0`, the model's first response is deterministic per the input. The retry succeeds only because the retry **prompt is different** (it includes the error feedback). That difference is doing all the work, not random variation.

### 6.5 Expected outputs

In `expected_outputs.md` (keep separate from your scripts):

```markdown
# Lab 1 expected
- person.name      = "Sujeet Kumar"
- person.age       = 41
- person.occupation contains "software engineer"
- person.company   = "Anthropic"

# Lab 2 expected
- invoice.invoice_number = "INV-2026-0418"
- invoice.status         = "paid"
- 2 line items
- line items sum matches total (1527.00)

# Lab 3 expected
- Attempt 1 fails with "rating must be between 1 and 5, got 10"
- Attempt 2 succeeds with rating=5
- Summary is <= 20 words
```

### 6.6 Commit

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
git add 02-prompt-engineering/day06-structured-outputs/
git commit -m "Day 6: Structured outputs — Pydantic schemas, nested types, validation/retries"
git push
```

---

## 7. Production Notes

### Cost & performance
- Structured output adds tokens to the **input** side: the provider serializes your schema into the request internally. A complex schema (5+ nested models, many fields) can add several hundred prompt tokens. Keep schemas tight.
- The **output** side is usually similar in length to free-form JSON, sometimes shorter because the constrained decoder won't waste tokens on preamble or fences.
- Constrained decoding has a small per-token latency overhead (the sampler does extra FSM checks). In practice, varies by provider; typically negligible for most schemas. For massive schemas it can become measurable.
- Field descriptions cost prompt tokens. Worth it — a well-described field saves a retry. Don't write essays in `Field(description=...)`; one clear sentence is the sweet spot.

### Reliability & failure modes
- Constrained decoding **can guarantee JSON shape** but **cannot guarantee semantic correctness**. The model can still emit a perfectly typed but factually wrong answer. Field validators are your second line of defense; cross-field business rules are your third.
- When `resp.parsed` is `None`, the model couldn't produce valid output even with constrained decoding (rare with modern providers, but happens with adversarial inputs or a schema that's impossible to satisfy). Always check.
- Beware "infinite null" schemas: if every field is `str | None = None`, the model can satisfy the schema with all nulls. Make fields required when you actually need them.
- Recursive schemas (`class Node: children: list[Node]`) work in Pydantic but can confuse the model into infinite or near-infinite nesting. Bound the depth with a `max_depth` post-validator if you allow recursion.

### Schema design
- **Required by default.** Only mark a field optional if "missing" is a meaningful signal. Optional everything = mush.
- **Descriptions on every field that's even slightly ambiguous.** This is one of the highest-ROI prompt engineering moves available — the model literally reads them.
- **Prefer `Literal[...]` over `Enum` for simple string sets.** Lighter syntax, easier to read.
- **Avoid `Any` and `dict[str, Any]`.** They defeat the purpose. If you can't name the shape, you don't yet understand the data.
- **Date and datetime fields** auto-parse ISO 8601 strings. Use them — don't store dates as `str`.
- **Order fields by logical priority.** Some providers' models produce better answers when the most important field comes first (the model commits to it earliest in decoding).

### Security & safety
- Structured outputs do NOT protect against prompt injection in the input data. A user-supplied document can still instruct the model to lie about extracted fields. Treat extracted data as untrusted user input downstream.
- For PII extraction in regulated environments, pair structured output with a PII redactor (Microsoft Presidio, AWS Comprehend) — see Day 50.
- The model can output fields you didn't ask for if the schema is loose (`extra="allow"`). Default Pydantic config rejects unknown fields, but if you've overridden it, you've opened a back door.

### When to use Instructor vs native
| You are | Use |
|---|---|
| Locked to one provider, one SDK | Native API (`response_schema` for Gemini, `response_format` for OpenAI) |
| Building a product that may swap providers | **Instructor** — uniform API, easier to A/B test models |
| Need automatic validation retries with backoff | **Instructor** — built-in (or roll your own as in Lab 3) |
| Need streaming partial structured output | **Instructor** with `Partial[Model]` |
| Self-hosting open models | **Outlines** or vLLM's native structured output |

### Tips & tricks
- When the model misbehaves on a specific field, **first try improving the description**, then add a validator, then add few-shot examples in the prompt, only THEN reach for a stronger model.
- `model.model_json_schema()` is your debug tool — print it before sending to see exactly what the model conditions on.
- For very long input + extraction, put the schema **before** the input text in the prompt. The model can plan its decoding while reading.
- For free-tier Gemini quotas, `gemini-2.5-flash-lite` (15 RPM) handles Day 6 labs comfortably; if you bump up to Flash, pace with `time.sleep(13)` between calls.

---

## 8. Interview Questions

### 🟢 Conceptual

<details>
<summary>Q1. What's the difference between "JSON mode" and "Structured Outputs"?</summary>

Both make the model emit JSON, but they guarantee different things.

- **JSON mode** (OpenAI ~late 2023): the output is guaranteed to be syntactically valid JSON — it'll parse. It is **not** guaranteed to match your schema; fields can be missing, extra, or the wrong type. You still need defensive parsing.

- **Structured Outputs** (OpenAI Aug 2024, Gemini around the same time): the output is guaranteed to match a schema you provide (typically a Pydantic model or JSON Schema). Implemented via **constrained decoding** — at each sampling step, the provider restricts the token vocabulary to tokens that keep the partial output valid per the schema's finite-state machine.

In new code, you should never use JSON mode. Structured Outputs supersedes it in every way. ([OpenAI announcement, Aug 2024](https://openai.com/index/introducing-structured-outputs-in-the-api/))
</details>

<details>
<summary>Q2. Why do Field(description=...) values matter? Aren't they just for human readers?</summary>

They look like Python docstrings, but they're not just for humans — they get serialized into the JSON Schema (`description` field per the JSON Schema spec), and the provider passes that schema to the model. The model reads the descriptions as part of its prompt context.

In practice, a one-sentence description like `Field(description="Star rating, integer between 1 and 5 inclusive")` reliably outperforms an undescribed `rating: int` field on tasks where the model has to interpret natural language inputs.

This is one of the highest-ROI prompt engineering moves available: it's compact, it lives with your type definitions, and it survives refactors better than free-form prompt instructions.
</details>

<details>
<summary>Q3. What is constrained decoding, and why does it matter?</summary>

Constrained decoding is the technique that makes "Structured Outputs" actually guaranteed. At each sampling step, the provider:

1. Compiles your JSON schema into a finite-state machine (FSM) over token sequences.
2. When the model picks the next token, the sampler filters the vocabulary to only tokens that keep the partial output on a valid path through the FSM.
3. The model picks the highest-probability allowed token.

Result: the output cannot be invalid JSON, cannot be missing required fields, cannot have wrong types — by construction. The model isn't "trying" to follow the schema; it's prevented from violating it.

This matters because it converts schema conformance from a **best-effort hope** into a **mechanical guarantee**. The whole class of "the model wrapped JSON in markdown fences" bugs disappears.

Reference implementations: Outlines (OSS), llguidance (Microsoft), and OpenAI/Gemini's internal versions.
</details>

<details>
<summary>Q4. What's the difference between structured outputs and tool calling?</summary>

Both emit JSON via constrained decoding, but the intent differs.

- **Structured output**: "Here is a schema. Fill it in based on the input." The model produces ONE object matching ONE schema. Used for extraction, classification, single typed answers.

- **Tool calling**: "Here are N tools, each with its own input schema. Pick zero, one, or more to call, and produce arguments for each." The model both **decides which** tool(s) to call AND **fills in** the arguments. Used for agents.

Mechanically they're very similar under the hood. API-wise, tool calling exposes the model's choice of tool as a separate field; structured output doesn't. We'll come back to tool calling in Day 22.
</details>

### 🟡 Practical

<details>
<summary>Q5. Write a Pydantic schema for a job posting that includes a list of requirements, a salary range, and a remote/hybrid/onsite enum.</summary>

```python
from pydantic import BaseModel, Field
from typing import Literal

class SalaryRange(BaseModel):
    min_usd: int = Field(description="Annual minimum salary in USD")
    max_usd: int = Field(description="Annual maximum salary in USD")

class JobPosting(BaseModel):
    title: str = Field(description="Job title")
    company: str
    location: str = Field(description="City and state, or 'Remote'")
    work_mode: Literal["remote", "hybrid", "onsite"]
    requirements: list[str] = Field(
        description="Bulleted requirements, each as a separate string"
    )
    salary: SalaryRange | None = Field(
        default=None,
        description="Pay range if disclosed in the posting, otherwise null",
    )
```

Notes I would mention out loud in an interview:
- `salary` is `| None` because many postings don't disclose pay.
- `work_mode` uses `Literal` (not `Enum`) — lighter, equivalent power for fixed string sets.
- `requirements` is a list of strings, not one concatenated string — preserves structure for downstream filtering.
- Cross-field validation (max ≥ min) would go in a `@model_validator(mode="after")`.
</details>

<details>
<summary>Q6. Given a Pydantic schema, write a Gemini call that returns the typed object.</summary>

```python
from google import genai
from google.genai import types

resp = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=f"Extract a job posting from this text:\n\n{job_text}",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=JobPosting,
        temperature=0.0,
    ),
)
posting: JobPosting = resp.parsed
```

Three things I'd call out:
1. `response_mime_type` and `response_schema` must both be set.
2. `resp.parsed` does the validation; if it raises, your schema or the model output is the problem.
3. `temperature=0.0` makes extraction reproducible. For creative tasks where you want variation, raise it.
</details>

<details>
<summary>Q7. Write a retry loop that catches Pydantic ValidationError and feeds the error back to the model.</summary>

```python
from pydantic import ValidationError

def extract_with_retry(prompt: str, schema, max_retries: int = 3):
    base = prompt
    last_error: str | None = None
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=schema,
    )
    for attempt in range(max_retries):
        full = base
        if last_error:
            full += f"\n\nPrevious attempt failed validation: {last_error}\nFix the JSON."
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=full, config=config
        )
        try:
            return resp.parsed
        except ValidationError as e:
            last_error = str(e)
    raise RuntimeError(f"Failed after {max_retries} attempts: {last_error}")
```

What I'd say next: "In production I'd use Instructor, which does this loop automatically with backoff. Doing it manually first taught me why it works."
</details>

### 🔴 System design

<details>
<summary>Q8. You're building a system that extracts structured data from 1M unstructured PDFs (invoices, contracts, resumes). Design the pipeline.</summary>

Three big design choices:

1. **Per-document-type schema**: define a Pydantic schema per document class — `Invoice`, `Contract`, `Resume`. Cross-type fields go in a base model. Schemas live in version control; changes go through code review.

2. **Tiered model strategy** by document complexity:
   - Easy/templated docs → `gemini-2.5-flash-lite` (cheap, 15 RPM free; in production: paid Flash-Lite scale).
   - Complex docs (long contracts, ambiguous resumes) → Flash or Pro with `thinking_budget > 0`, only when triggered by confidence or document length thresholds.
   - Track per-tier accuracy; rebalance.

3. **Validation pipeline** for every extraction:
   - Constrained decoding guarantees shape.
   - Pydantic field validators catch semantic violations (totals, dates, ranges).
   - **Cross-field business rules** catch domain violations (line items sum = total; signature date >= contract date).
   - Failures go to a retry queue with error feedback (Lab 3 pattern) for up to N attempts.
   - Persistent failures escalate to a human-review queue.

Other concerns:
- **PII handling**: redact before extraction or use a model with the right data-residency guarantees.
- **Cost tracking**: log per-document input/output tokens; cost-per-document is your single most important ops metric.
- **Schema versioning**: stored extractions need to know which schema version produced them. Add `_schema_version: str` to your storage layer.
- **Eval set**: hold out 500 documents with human-labeled ground truth; CI runs extraction against them on every schema or prompt change, blocks merges on accuracy regression.

I would NOT roll my own constrained-decoding stack. I'd use the provider's native structured outputs (Gemini's `response_schema` or OpenAI's `response_format=ModelClass`), wrapped in Instructor if I want provider portability.
</details>

<details>
<summary>Q9. Your structured-output extractions are accurate but slow — p95 latency is 4 seconds. Where would you look?</summary>

Four likely culprits, in order:

1. **Schema bloat.** Every nested model and field description goes into the provider's internal serialized schema, inflating the input the model conditions on. Look at `Model.model_json_schema()` — if it's hundreds of lines, simplify. Common offenders: deeply nested optional fields, fields with multi-paragraph descriptions, recursive types.

2. **Input length.** Structured output latency scales roughly with input + output tokens. If you're stuffing entire PDFs into the prompt, retrieval-first (Day 13) and pass only the relevant chunks.

3. **Output bloat.** Long `summary` or `notes` fields make the model decode many more tokens. If a field doesn't have a strict character cap, the model will often over-elaborate. Add `max_length` validators or word-count constraints in descriptions.

4. **Wrong model tier.** Pro/reasoning models are slower than Flash. If accuracy doesn't actually need them, downshift. Run A/B on accuracy vs latency before assuming you need the bigger model.

Sneakier ones: a high `thinking_budget` on reasoning models inflates latency dramatically; constrained-decoding FSM compilation has a per-request fixed cost that hurts you on low-latency / high-QPS workloads (mostly disappears with provider caching).
</details>

<details>
<summary>Q10. Your team is split between using native Gemini structured outputs vs the Instructor library. Make the case for each.</summary>

**Case for native Gemini:**
- One fewer dependency. Smaller attack surface, simpler upgrades, fewer mystery bugs to debug across abstraction layers.
- Always first to support new provider features (multimodal structured outputs, new model variants, etc.). Instructor is a wrapper — it lags.
- For a team committed to Gemini for the long haul, abstraction over provider APIs is overhead with no payoff.

**Case for Instructor:**
- Provider portability. The day you want to A/B test Claude Sonnet vs Gemini 2.5 Flash, your code changes one line.
- Validation retries built in — not your code, not your bug.
- Stronger streaming story for partial structured outputs (`Partial[Model]`).
- Adopted broadly enough that new engineers will recognize the patterns.

**My honest take:** if I'm building a one-team product where Gemini is the chosen provider, native. If I'm building a platform that needs to support multiple LLM backends, or a library other teams will consume, Instructor. The split-the-difference answer — "wrap the native SDK in our own thin abstraction" — usually becomes a worse Instructor over time. Don't do it unless you have a very specific reason.
</details>

---

## End of Day 6

You now have:
- A working mental model of structured outputs vs JSON mode vs tool calling
- Three labs covering basic extraction, nested+enum schemas, and validation+retry
- The schema-design discipline that makes downstream code clean
- The 2026 industry context (Pydantic v2, Instructor, native APIs, Outlines for OSS)

**Next:** Day 7 — Output validation, retries, error recovery with **tenacity**. We'll take the manual retry loop from Lab 3 and replace it with the standard Python retry library that real teams use everywhere, not just for LLMs.

Run the labs and ping me with anything that surprises you, breaks, or smells wrong before we move on.
