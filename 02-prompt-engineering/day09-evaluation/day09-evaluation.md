# 📏 Day 9 — How to KNOW a Prompt Got Better: Versioning, A/B Testing & Evaluation

*Category 2 · Prompt Engineering · Day 9 of 53 (the last one!) · Model: `gemini-2.5-flash-lite`*

> [!IMPORTANT]
> 🎯 **The big idea, in one breath:** Up to now, when you changed a prompt you just *felt* it got better. Today you learn to **prove it with a number** — so you stop guessing and start measuring. This is the single habit that turns prompt "fiddling" into prompt *engineering*.

Here's the whole day as a simple story before any jargon:

| 🧩 Piece | What it really means | Everyday analogy |
|:--|:--|:--|
| 🧪 **Eval set** | A small bundle of test questions where you *already know* the right answers. | A teacher's answer key for a quiz. |
| 📏 **Metric** | The rule for scoring (e.g., "how many did it get right?"). | Marking the quiz: 8 out of 10. |
| ⚖️ **A/B test** | Run prompt A and prompt B on the *same* quiz and see which scores higher. | Two students take the same test; compare marks. |
| 🏷️ **Versioning** | Labeling your prompts (v1, v2, v3) so you can compare and go back. | Saving drafts of an essay: draft1, draft2… |
| 🏭 **Evaluation harness** | The little program that runs all of the above automatically. | An automatic marking machine. |

> [!TIP]
> 📺 We've got an **interactive A/B scoreboard in the chat** for this day — watch a vague prompt and a clear prompt take the same quiz and get scored live. Keep it open beside this file.

---

## 📚 1. Vocabulary (just skim — it clicks after Section 2)

Read once, don't memorize. Come back after the explanations.

| 🔤 Term | 💭 Plain-English meaning |
|:--|:--|
| **Evaluation (eval)** | Measuring how good a prompt's outputs are, using examples. |
| **Eval set / test set** | The collection of example inputs + their known-correct answers. |
| **Ground truth** | The "correct answer" you compare the AI's answer against. |
| **Metric** | A number that scores quality (accuracy, pass rate, a 1–5 judge score…). |
| **Accuracy** | The simplest metric: (number it got right) ÷ (total). |
| **A/B test** | Comparing two versions on the same eval set to see which wins. |
| **Prompt version** | One specific saved wording of a prompt, labeled (v1, v2…). |
| **Regression** | When a change makes things *worse* — your score drops. You want to catch these! |
| **Evaluation harness** | The reusable code that runs your prompt on the eval set and reports the score. |
| **LLM-as-judge** | Using a second AI call to score outputs that have no single "right" answer. |
| **Test-set contamination** | The mistake of letting the AI see the answer key — it cheats, and your score is fake. |

---

## 🧭 2. The Whole Idea, Step by Step (the heart of the day)

Today's pieces aren't separate tricks — they're **one workflow** built up one step at a time. Let's walk it like a story.

---

### 🚩 The problem: "vibes-based" prompting

Right now your loop is probably: *write a prompt → read one output → "yeah that looks better" → ship it.*

> 🧒 **Analogy (just an analogy):** That's like a chef tasting a dish *once* and declaring it the best recipe ever. Maybe that spoonful was good by luck. Maybe the next bite is awful. One taste isn't proof.

The danger word here is **regression** — a change that quietly makes things *worse*. You "improve" the prompt for one example, ship it, and it silently breaks five others you didn't check. You'd never know, because you were going on vibes.

> [!IMPORTANT]
> 🎯 **The fix for vibes is measurement.** Everything below is just *how to measure*.

---

### 🧪 Step 1 — Build an Eval Set (your answer key)

#### ❓ What is it?
An **eval set** (also called a *test set*) is a small bundle of example inputs where **you already know the correct answer** for each. The known-correct answer is called the **ground truth**.

> 📦 **Concrete example (used in our labs):** support messages we want to sort into `billing`, `technical`, or `general`:
> | Message | Correct category (ground truth) |
> |:--|:--|
> | "I was charged twice this month" | `billing` |
> | "The app crashes when I open settings" | `technical` |
> | "What are your business hours?" | `general` |
> | "My subscription renewed but I wanted to cancel" | `billing` |
> | "I can't log in, password is wrong" | `technical` |

#### ❓ Why does it exist?
Because without known-correct answers, you have **nothing to compare the AI's output to**. The eval set is the ruler. No ruler, no measuring.

> [!CAUTION]
> 🚨 **The #1 rookie mistake — test-set contamination.** The answer key must **never** end up inside the prompt the AI sees. If the AI can see the correct answer, it just copies it — it "passes" by cheating, and your score is a lie. **In our labs we keep the questions and the answer key in two separate files** so the answers physically cannot leak into the prompt. (You caught a past coach on exactly this — we won't repeat it.)

#### ❓ When do I use it?
Always, before you trust *any* prompt change. Even 5–10 good examples beat zero.

---

### 📏 Step 2 — Pick a Metric (how to score)

#### ❓ What is it?
A **metric** is the rule that turns "the AI's answers" into "a number." The simplest one is **accuracy**:

```text
            number the AI got right
accuracy = ──────────────────────────
                total questions
```

> 📦 **Example:** the AI labels 4 of our 5 messages correctly → accuracy = 4 ÷ 5 = **0.80 = 80%**.

#### ❓ Why does it exist?
Because "better" is an opinion, but **85% vs 72%** is a fact. A metric turns arguments into evidence.

> [!NOTE]
> 🧠 **Two flavors of metric, depending on the task:**
> - ✅ **Exact match** — when there's *one* right answer (a category, a number). Easy: did `predicted == expected`?
> - 🧑‍⚖️ **LLM-as-judge** — when there's *no single* right answer (a summary, an email). You ask a *second* AI to score the output on a rubric. (We try this in Lab 3; it gets a whole day on Day 46.)

---

### ⚖️ Step 3 — A/B Test (compare two versions fairly)

#### ❓ What is it?
An **A/B test** is dead simple: take **prompt version A** and **prompt version B**, run them **on the exact same eval set**, and compare their scores. Higher score wins.

> 🧒 **Analogy (just an analogy):** Two students sit the *same* exam. Whoever scores higher is genuinely better at *that* exam — because the test was identical and fair.

> 📦 **Concrete example (Lab 2):**
> - **v1 (vague):** *"Categorize this message."* → scores 60% (it invents categories, misreads some)
> - **v2 (clear):** *"Categorize into exactly one of: billing, technical, general. billing = payments/charges; technical = bugs/login; general = everything else. Reply with one word."* → scores 100%
> Now you don't *think* v2 is better — you can **prove** v2 beats v1 by 40 points on the same test.

#### ❓ Why does it exist?
To make change **safe**. Before/after scores on the same set tell you instantly whether your edit helped (score up 📈), did nothing (flat ➖), or caused a **regression** (score down 📉).

#### ❓ When do I use it?
Every time you're tempted to "improve" a prompt. A/B it against the current version first.

---

### 🏷️ Step 4 — Version Your Prompts (so you can go back)

#### ❓ What is it?
**Versioning** means saving each wording of your prompt with a **label** — `v1`, `v2`, `v3` — instead of editing one prompt in place and losing the old one.

> 🧒 **Analogy (just an analogy):** Like saving `essay_draft1`, `essay_draft2`… If draft3 turns out worse, you can go back to draft2. If you'd overwritten it, it's gone forever.

> 📦 **Tiny example:** keep them in a dictionary you can pick from:
> ```python
> PROMPTS = {
>     "v1": "Categorize this message.",
>     "v2": "Categorize into exactly one of: billing, technical, general. ...",
> }
> ```

#### ❓ Why does it exist?
So you can **compare** versions (Step 3 needs at least two!) and **roll back** instantly if a new version regresses. Your `git` repo already version-controls these files for free — versioning *inside* the file (v1/v2 labels) just makes A/B testing easy.

---

### 🏭 Putting it together: the Evaluation Harness

#### ❓ What is it?
An **evaluation harness** is just the little program that does all four steps automatically: load the eval set → run a prompt version on every example → score with a metric → print the result. Run it once and get a number.

> 🧒 **Analogy (just an analogy):** An automatic exam-marking machine. Feed it the answer key and the student's answers; it spits out the grade. You build it once, then reuse it for every prompt change forever.

> [!TIP]
> 🎯 **Carry this away:** **eval set** (the ruler) + **metric** (the number) + **A/B test** (fair comparison) + **versioning** (so you can compare and undo) = a **harness** that replaces guessing with proof. Lab 1 builds the harness; Lab 2 uses it to A/B test; Lab 3 handles fuzzy tasks with an AI judge.

---

## 🔧 3. Failure → Fix, in practice

| 🚩 Without today's habit | ✅ With it |
|:--|:--|
| You tweak a prompt, eyeball one output, ship it. | You run both versions on the eval set; the score decides. |
| A change quietly breaks 5 other cases (a **regression**). | The harness catches the score drop *before* you ship. |
| Team argues "v2 feels better." | "v2 scores 92% vs v1's 78%." Argument over. |
| Fuzzy task ("is this summary good?") feels unmeasurable. | An **LLM-as-judge** scores it 1–5 on a rubric. |

---

## 🗺️ 4. Concept → Code Map

| 💭 Idea | 💻 Code pattern |
|:--|:--|
| 🧪 Load the eval set safely | read `questions.json` and `answer_key.json` from **separate files** |
| 📏 Exact-match score | `correct += (predicted == expected)` then `correct / total` |
| 🏷️ Hold multiple prompt versions | a dict: `PROMPTS = {"v1": "...", "v2": "..."}` |
| ⚖️ A/B test | run the harness once per version, compare the two accuracy numbers |
| 🏭 The harness | a function: `evaluate(prompt) -> accuracy` |
| 🧑‍⚖️ LLM-as-judge | a second AI call that returns a `score` (1–5) + `reason` |

---

## 🧰 5. Best Tools / Tech Stack

| 🎯 Need | 🛠️ Tool | 💬 Why |
|:--|:--|:--|
| Learn the mechanics | **Raw Python** (our labs) | Build the harness by hand so you understand what tools automate |
| Industry-standard prompt testing | **Promptfoo** | The standard CLI tool: write test cases in a YAML file, it runs + scores + A/B tests for you ([promptfoo.dev](https://www.promptfoo.dev/)) |
| Richer eval metrics | **DeepEval** | "Unit tests for LLMs," many built-in metrics ([repo](https://github.com/confident-ai/deepeval)) |
| See every run | **LangSmith** / **Langfuse** | Trace and store eval runs over time (Category 7) |

> [!NOTE]
> 🎒 **Course plan:** today we hand-build a harness in plain Python so the idea is crystal clear. In real projects you'd graduate to **Promptfoo** — a tiny taste:
> ```yaml
> # promptfooconfig.yaml — Promptfoo runs your prompts against tests and scores them
> prompts: [prompt_v1.txt, prompt_v2.txt]   # the two versions to compare
> providers: [google:gemini-2.5-flash-lite] # which model to use
> tests:
>   - vars: { message: "I was charged twice" }
>     assert: [{ type: equals, value: billing }]  # the ground-truth check
> ```
> Then `promptfoo eval` shows both versions side by side, scored. Same idea as our Lab — just automated.

---

## 🧪 6. Lab Walkthroughs

> [!NOTE]
> 🔑 Every script reads your key with `os.getenv("GOOGLE_API_KEY")` and prints with `rich`. We'll add one tiny helper, `rich`'s `Table`, to make results pretty.

### 📁 6.1 Make the folder and files (PowerShell)

```powershell
# main day folder
New-Item -ItemType Directory -Path "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation" -Force | Out-Null
# a sub-folder to hold the eval set (kept SEPARATE from the answer key inside it)
New-Item -ItemType Directory -Path "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\eval_set" -Force | Out-Null

New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\eval_set\questions.json"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\eval_set\answer_key.json"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\01_measure_one_prompt.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\02_ab_test.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\03_llm_as_judge.py"
```

### 📄 6.2 The eval set — two separate files

> [!CAUTION]
> 🚨 Notice: **questions** live in one file, **answers** in another. The code below only ever puts the *question* into the prompt. The answer key is opened *after* the AI has answered, just to mark the score. That's how we avoid cheating (test-set contamination).

`eval_set/questions.json` — **inputs only, no answers:**
```json
[
  { "id": "q1", "message": "I was charged twice this month" },
  { "id": "q2", "message": "The app crashes when I open settings" },
  { "id": "q3", "message": "What are your business hours?" },
  { "id": "q4", "message": "My subscription renewed but I wanted to cancel" },
  { "id": "q5", "message": "I can't log in, it says my password is wrong" }
]
```

`eval_set/answer_key.json` — **the correct categories, in a DIFFERENT file:**
```json
[
  { "id": "q1", "category": "billing" },
  { "id": "q2", "category": "technical" },
  { "id": "q3", "category": "general" },
  { "id": "q4", "category": "billing" },
  { "id": "q5", "category": "technical" }
]
```

### 📏 6.3 Lab 1 — `01_measure_one_prompt.py` (build the harness, score ONE prompt)

```python
"""
01_measure_one_prompt.py  📏  Measure how good ONE prompt is, with a real number.

The plan:
  1) load the test questions (inputs only),
  2) ask the AI to categorize each one,
  3) load the answer key (from a SEPARATE file) and count how many it got right,
  4) print the accuracy.

Why separate files? So the correct answers never touch the prompt. If the AI saw the
answer, it would just copy it and "pass" by cheating. That cheating is called
test-set contamination, and it makes your score meaningless.
"""

import os                                    # to read environment variables (the API key)
import json                                  # to read our .json data files
from pathlib import Path                     # a clean way to build file paths
from dotenv import load_dotenv               # loads variables from .env
from rich.console import Console             # colorful printing
from rich.table import Table                 # pretty results table
from google import genai                     # Gemini SDK
from google.genai import types               # config objects

load_dotenv()                                # make GOOGLE_API_KEY available
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# Path(__file__) is THIS script's location. .parent is the folder it lives in.
# We build paths from here so the script works no matter which folder you run it from.
HERE = Path(__file__).parent
EVAL_DIR = HERE / "eval_set"                 # the sub-folder with our data

# Open the QUESTIONS file (inputs only) and turn the JSON text into a Python list.
with open(EVAL_DIR / "questions.json", encoding="utf-8") as f:
    questions = json.load(f)                 # e.g. [{"id":"q1","message":"..."}, ...]

# Open the ANSWER KEY file (the correct categories) — a DIFFERENT file.
with open(EVAL_DIR / "answer_key.json", encoding="utf-8") as f:
    answer_list = json.load(f)               # e.g. [{"id":"q1","category":"billing"}, ...]

# Turn the answer list into a fast lookup dictionary: id -> correct category.
# (So we can ask "what's the right answer for q3?" instantly.)
answer_key = {item["id"]: item["category"] for item in answer_list}

# The prompt we are testing. {message} is a placeholder we fill in for each question.
PROMPT = (
    "Categorize this support message into exactly one of: billing, technical, general.\n"
    "Reply with only the one category word, in lowercase.\n\n"
    "Message: {message}"
)

def classify(message: str) -> str:
    """Send ONE message to the AI and return its category guess (cleaned up)."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=PROMPT.format(message=message),   # fill the {message} placeholder
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),  # no hidden reasoning
            temperature=0.0,                        # steady, repeatable answers
        ),
    )
    # .strip() removes spaces/newlines; .lower() makes "Billing" match "billing".
    return resp.text.strip().lower()

# Build a results table to show each question's outcome.
table = Table(title="Prompt evaluation")
table.add_column("id")
table.add_column("AI said")
table.add_column("correct answer")
table.add_column("right?")

correct = 0                                  # running count of how many we got right
for q in questions:                          # go through every test question
    predicted = classify(q["message"])       # the AI's guess
    expected = answer_key[q["id"]]           # the ground-truth answer for this id
    is_right = (predicted == expected)       # True if they match exactly
    correct += is_right                      # True counts as 1, False as 0
    mark = "✅" if is_right else "❌"
    table.add_row(q["id"], predicted, expected, mark)

console.print(table)

# Accuracy = how many right, divided by the total. This is our METRIC.
accuracy = correct / len(questions)
console.print(f"\nScore: [bold green]{correct}/{len(questions)} = {accuracy:.0%}[/bold green]")
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\01_measure_one_prompt.py
```
You now have a **number** for this prompt. That number is the whole point.

### ⚖️ 6.4 Lab 2 — `02_ab_test.py` (compare TWO prompt versions)

```python
"""
02_ab_test.py  ⚖️  Run TWO prompt versions on the SAME eval set and see which wins.

This reuses the harness idea from Lab 1, but now we test two versions:
  v1 = vague   ("categorize this")
  v2 = clear   (lists the categories and what each means)
Whichever scores higher is the better prompt — proven, not guessed.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

HERE = Path(__file__).parent
EVAL_DIR = HERE / "eval_set"
with open(EVAL_DIR / "questions.json", encoding="utf-8") as f:
    questions = json.load(f)
with open(EVAL_DIR / "answer_key.json", encoding="utf-8") as f:
    answer_key = {x["id"]: x["category"] for x in json.load(f)}

# 🏷️ VERSIONING: we keep both prompt versions in a dictionary, labeled v1 and v2.
# Old versions aren't lost — we can compare them and roll back any time.
PROMPTS = {
    "v1": "Categorize this message.\n\nMessage: {message}",   # vague on purpose
    "v2": (                                                    # clear and specific
        "Categorize this support message into exactly one of: billing, technical, general.\n"
        "Definitions: billing = payments, charges, refunds, subscriptions; "
        "technical = bugs, crashes, errors, login problems; "
        "general = anything else.\n"
        "Reply with only the one category word, lowercase.\n\n"
        "Message: {message}"
    ),
}

def classify(prompt_template: str, message: str) -> str:
    """Run one message through a given prompt version; return the cleaned guess."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt_template.format(message=message),
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text.strip().lower()

def evaluate(prompt_template: str) -> float:
    """THE HARNESS: run a prompt version on the whole eval set, return its accuracy."""
    correct = 0
    for q in questions:
        predicted = classify(prompt_template, q["message"])
        if predicted == answer_key[q["id"]]:    # compare to ground truth
            correct += 1
    return correct / len(questions)             # the accuracy number

# Run the harness once per version and remember each score.
scores = {}
for version, template in PROMPTS.items():
    scores[version] = evaluate(template)
    console.print(f"{version}: [cyan]{scores[version]:.0%}[/cyan]")

# Declare the winner: whichever version has the higher score.
winner = max(scores, key=scores.get)            # the key (version) with the biggest value
console.print(f"\n🏆 Winner: [bold green]{winner}[/bold green] "
              f"({scores[winner]:.0%} vs {min(scores.values()):.0%}) — proven, not guessed.")
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\02_ab_test.py
```
📺 The **A/B scoreboard visual in chat** shows this exact comparison: vague v1 vs clear v2, scored side by side.

### 🧑‍⚖️ 6.5 Lab 3 — `03_llm_as_judge.py` (score fuzzy tasks with an AI judge)

```python
"""
03_llm_as_judge.py  🧑‍⚖️  Score outputs that have NO single right answer.

Exact-match works for categories. But how do you score a SUMMARY? There's no one
"correct" summary to match. The trick: ask a SECOND AI (the "judge") to rate the
summary against the original on a 1-5 scale, with a reason. (Big topic on Day 46.)
Reference: Zheng et al. 2023, "Judging LLM-as-a-Judge" (https://arxiv.org/abs/2306.05685).
"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# A paragraph we want summarized, and a summary the "worker" AI produced.
ORIGINAL = (
    "Our new app update improves battery life by 20%, adds a dark mode, and fixes the "
    "crash that happened when opening Settings. It is rolling out to all users this week."
)

def make_summary(text: str) -> str:
    """The 'worker' AI: produce a one-sentence summary."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=f"Summarize this in one sentence:\n\n{text}",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text.strip()

# The shape of the JUDGE's verdict. Forcing a number + reason makes it usable as a metric.
class Verdict(BaseModel):
    score: int = Field(description="Quality from 1 (poor) to 5 (excellent)")
    reason: str = Field(description="One-sentence reason for the score")

def judge(original: str, summary: str) -> Verdict:
    """The 'judge' AI: rate the summary against the original, 1-5, with a reason."""
    prompt = (
        "You are grading a summary. Score 1 (poor) to 5 (excellent) based on whether the "
        "summary is accurate and captures the key points of the original.\n\n"
        f"ORIGINAL:\n{original}\n\n"
        f"SUMMARY:\n{summary}"
    )
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # the judge replies as JSON...
            response_schema=Verdict,                 # ...matching our Verdict shape
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.parsed

# 1) worker produces a summary  2) judge scores it.
summary = make_summary(ORIGINAL)
verdict = judge(ORIGINAL, summary)

console.print(f"[bold]Summary:[/bold] {summary}")
console.print(f"[bold]Judge score:[/bold] [green]{verdict.score}/5[/green] — {verdict.reason}")
console.print("[dim]Now you can A/B-test summary prompts by comparing their average judge scores.[/dim]")
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\03_llm_as_judge.py
```

### ✅ 6.6 What you should see

```text
📏 Lab 1: a table of 5 rows with ✅/❌, ending in a score like "5/5 = 100%".
⚖️ Lab 2: v1 prints a lower % than v2; winner = v2.
🧑‍⚖️ Lab 3: a one-sentence summary plus a judge score like "5/5 — accurate and complete".
```

### 💾 6.7 Save your work

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
git add 02-prompt-engineering/day09-evaluation/
git commit -m "Day 9: evaluation — eval sets, accuracy metric, A/B testing, prompt versioning, LLM-as-judge"
git push
```

---

## 🚀 7. Production Notes (what matters in the real world)

### 💰 Cost & speed
- Each eval run = one AI call per example. A 100-example set = 100 calls per version. A/B testing two versions = 200 calls. Budget for it; run examples concurrently (async) to save time.
- LLM-as-judge **doubles** calls (one to produce, one to grade). Worth it for fuzzy tasks; overkill for exact-match ones.

### 🛡️ Do this right
> [!CAUTION]
> 🚨 **Keep the answer key out of the prompt — always.** Separate files (like our labs) make accidental leakage almost impossible. A "100%" score from a contaminated test is worse than no test, because it lies to you.

> [!WARNING]
> 📉 **Re-run your eval set on EVERY prompt change.** The whole point is catching regressions before users do. A change that helps one case often hurts another — only the full set reveals it.

- 🧪 **Grow your eval set over time.** Every time a real user hits a bug, add that example (with its correct answer) to the set. Your harness gets smarter with every failure.
- 🧑‍⚖️ **Judge prompts need evaluating too.** An AI judge can be biased (e.g., preferring longer answers). Spot-check its scores against your own judgment now and then.

---

## 🎤 8. Interview Questions (the crux of the day)

> [!NOTE]
> 🎯 Answer these in your own words and you own the day. Each answer leads with the one-sentence **crux**.

### 🟢 Conceptual

<details>
<summary>🟢 Q1. Why do you need an eval set? What's wrong with just eyeballing one output?</summary>

> 🎯 **Crux:** One output is anecdote; an eval set is evidence — and it's the only way to catch a change that quietly makes other cases worse (a regression).

Eyeballing one output is like a chef tasting one spoonful and declaring the recipe perfect — the next bite could be terrible. An eval set is a bundle of inputs with known-correct answers (ground truth), so you can score the prompt on many cases at once and compare versions fairly.
</details>

<details>
<summary>🟢 Q2. What is test-set contamination and why is it dangerous?</summary>

> 🎯 **Crux:** It's letting the AI see the answer key, so it "passes" by copying — giving you a fake score that's worse than no score because it lies to you.

The fix is to keep the questions and the answer key in separate files (or otherwise ensure the correct answer never enters the prompt). The AI sees only the question; the answer key is used afterward, purely to mark the score.
</details>

<details>
<summary>🟢 Q3. When do you use exact-match vs an LLM-as-judge metric?</summary>

> 🎯 **Crux:** Exact-match when there's one right answer (a category, a number); LLM-as-judge when there isn't (a summary, an email) and you need a second AI to rate quality on a rubric.

Exact-match is `predicted == expected` — cheap and objective. LLM-as-judge asks a second model to score 1–5 with a reason — flexible but costs an extra call and can be biased, so spot-check it. ([Zheng 2023](https://arxiv.org/abs/2306.05685))
</details>

<details>
<summary>🟢 Q4. What does an A/B test prove that "this feels better" doesn't?</summary>

> 🎯 **Crux:** Run both versions on the *same* eval set; the higher score is genuine proof one prompt is better at that task — turning opinion into a fact like "92% vs 78%."

Same test, fair comparison. It also tells you the *direction* of a change: score up (improvement), flat (no effect), or down (regression you just avoided shipping).
</details>

### 🟡 Practical

<details>
<summary>🟡 Q5. Sketch a minimal evaluation harness in Python.</summary>

> 🎯 **Crux:** Load questions + answer key (separate files), run the prompt on each, count matches, divide by total.

```python
def evaluate(prompt_template):
    correct = 0
    for q in questions:                       # questions.json (inputs only)
        guess = classify(prompt_template, q["message"])
        if guess == answer_key[q["id"]]:      # answer_key.json (separate file)
            correct += 1
    return correct / len(questions)           # accuracy
```
A/B testing is just calling `evaluate()` once per prompt version and comparing the numbers.
</details>

<details>
<summary>🟡 Q6. How do you "version" prompts so you can A/B test and roll back?</summary>

> 🎯 **Crux:** Store each wording with a label (v1, v2…) instead of editing in place, so old versions survive for comparison and rollback.

```python
PROMPTS = {"v1": "Categorize this message.",
           "v2": "Categorize into exactly one of: billing, technical, general. ..."}
```
Your `git` history versions the files too; the in-file labels just make running an A/B test trivial.
</details>

### 🔴 System design

<details>
<summary>🔴 Q7. Design a process so prompt changes can't silently break production.</summary>

> 🎯 **Crux:** Treat the eval set like a test suite — every prompt change must pass it (no score regression) before it ships, and the set grows from real failures.

- Keep an eval set in the repo (questions + answer key, separate).
- A harness runs it on every change; block the change if accuracy drops vs the current version (a regression).
- For fuzzy outputs, add LLM-as-judge metrics; spot-check the judge.
- When a real user hits a bug, add that case (with ground truth) to the set so it can never regress again.
- Trace runs (LangSmith/Langfuse) so you can see scores over time.

This is just continuous integration (CI) applied to prompts.
</details>

<details>
<summary>🔴 Q8. Your eval shows 100% but production users still complain. What likely went wrong?</summary>

> 🎯 **Crux:** Either your eval set doesn't reflect real inputs, or it's contaminated — a perfect score on the wrong (or cheated) test means nothing.

Check: (1) Is the answer key leaking into the prompt (contamination)? (2) Does the eval set actually contain the kinds of messages real users send, or just easy ones? (3) Is the metric measuring what users care about? Fix by adding real, varied, failing user cases to the set and re-checking for leakage.
</details>

---

## 🏁 End of Day 9 — and the end of Prompt Engineering! 🎉

> [!IMPORTANT]
> 🎯 **The whole day in one line:** stop guessing — build an **eval set** (the ruler), score with a **metric**, **A/B test** versions on the same set, and **version** your prompts so you can compare and roll back. That's an **evaluation harness**, and it's how pros change prompts without fear.

You've now finished **Category 2: Prompt Engineering** (Days 3–9). You can make a model talk well, output clean data, recover from errors, combine calls into bigger workflows, and *measure* whether any of it actually works.

➡️ **Next: Day 10 — welcome to 📚 RAG (Retrieval-Augmented Generation).** This is the big one: teaching the AI to look things up in *your* documents so it stops making facts up. Everything you learned about structured output, chaining, and evaluation feeds straight into it.
