# 🧩 Day 8 — Three Ways to Combine AI Calls: Self-Consistency, ReAct & Prompt Chaining

*Category 2 · Prompt Engineering · Day 8 of 53 · Model: `gemini-2.5-flash-lite`*

> [!IMPORTANT]
> 🎯 **The big idea, in one breath:** Until now you've been getting **one** AI call to behave. Today you learn the **three ways to combine several calls** into something smarter than any single call — and these three combinations are exactly what real **AI agents** are built from.

Think of today as learning three "moves." Here they are in plain words before any jargon:

| Move | What it really means | Everyday analogy |
|:--|:--|:--|
| 🟦 **Self-consistency** | Ask the AI the same hard question several times, then go with the most common answer. | Asking 7 friends a riddle and trusting the answer most of them gave. |
| 🟩 **Prompt chaining** | Break one big job into small steps and feed each step's result into the next. | A kitchen assembly line: chop → cook → plate, each station does one thing. |
| 🟪 **ReAct** | The AI thinks, asks for a tool, sees the real result, thinks again — in a loop. | A detective who reasons, checks a clue, reasons again, until the case is solved. |

> [!TIP]
> 📺 We've got **three interactive visuals in the chat** for this day — the loop step-through, the three-moves map, and the voting demo. Keep them open beside this file.

---

## 🗺️ The map of the day (read this first)

There are exactly **three shapes** of composition. Everything else is a remix of these.

```text
  🟦 PARALLEL                 🟩 SERIAL                    🟪 LOOP
  Self-consistency            Prompt chaining              ReAct
  ──────────────────          ──────────────────           ──────────────────
        ┌─ sample 1 ─┐         ┌────┐  ┌────┐  ┌────┐         ┌──────────┐
   Q ───┼─ sample 2 ─┼─► 🗳️    │ S1 │─►│ S2 │─►│ S3 │         │ 🧠 think  │◄─┐
        ├─ sample 3 ─┤  vote   └────┘  └────┘  └────┘         └────┬─────┘  │
        └─ sample 4 ─┘   │     extract→decide→write           ⚙️ act+observe┘
                         ▼                                         │
                    ✅ answer                                  ✅ when done
```

| Shape | Technique | 🎯 One-line essence |
|:--|:--|:--|
| 🟦 **Parallel** | Self-consistency | Sample many reasoning paths, **vote** — correct paths converge, errors scatter. |
| 🟩 **Serial** | Prompt chaining | Break one hard task into a **sequence** of easy, individually-reliable calls. |
| 🟪 **Loop** | ReAct | **Reason → act → observe**, repeat — ground the model in real data so it stops hallucinating. |

> [!TIP]
> 📺 **See it live:** I've rendered the *three shapes* and a step-through of the *self-consistency vote* as interactive visuals in our chat. Open them next to this file.

---

## 📚 1. Vocabulary (skim now — it'll click after Section 2)

Don't memorize this yet. Read it once, move on, and come back after the explanations below.

| 🔤 Term | 💭 Plain-English meaning |
|:--|:--|
| **Self-consistency** | Run the same question several times and take the majority answer. |
| **Sample** | One single run / one single answer from the AI. (7 runs = 7 samples.) |
| **Majority vote** | The answer that showed up the most across your samples. |
| **Temperature** | A dial (covered Day 2) that controls how "varied" the AI's answers are. `0` = always the same answer; above `0` = each run can differ a little. |
| **Prompt chaining** | Splitting a task into a sequence of small AI calls, each feeding the next. |
| **Stage** | One step in a chain (e.g., the "extract" stage, the "decide" stage). |
| **ReAct** | A loop where the AI alternates **Re**asoning and **Act**ing (calling tools). |
| **Tool** | A function *you* write that the AI can ask to run (a lookup, a calculator, a web search). The AI requests it by name; your code runs it. |
| **Thought / Action / Observation** | The three parts of one ReAct turn: the AI's reasoning, the tool it asks for, and the result your code hands back. |
| **Max-steps guard** | A safety limit so a confused AI can't loop forever. |

---

## 🧭 2. The Three Techniques — explained for a beginner

This is the heart of the day. Each technique gets its own section. Under each, three questions, answered plainly: **What is it? · Why does it exist? · When do I use it?**

---

### 🟦 Technique 1 — Self-Consistency

#### ❓ What is it?

You ask the AI the **same question several times** (say, 7 times), let it think **freshly each time**, collect all 7 answers, and keep the answer that appeared **most often**. That "most common answer" is called the *majority vote*.

> 🧒 **Analogy (just an analogy):** Imagine a hard riddle. You ask 7 smart friends *separately*. A couple might slip up, but if 5 of them independently say *"the answer is 10,"* you'd trust 10 far more than if you'd asked only one friend who might have had an off day. Self-consistency does this with one AI instead of 7 friends.

> 📦 **Concrete example (the snail puzzle from Lab 1):**
> *"A snail climbs a 12 m well: +3 m each day, −2 m each night. Which day does it reach the top?"*
> - Ask **once** → the AI might say **"12 days"** (a common trap answer).
> - Ask **7 times** → 5 runs say **"10 days"**, 2 say "12 days."
> - You keep **10** (the majority). Bonus: "5 out of 7 agreed" also tells you *how confident* to be.
>
> *(The right answer is 10: the snail gains 1 m net per day, but on day 10 it climbs from 9 m to 12 m and escapes before it can slide back at night.)*

#### ❓ Why does it exist? (the problem it solves)

On a **hard** problem, the AI doesn't always get it right on the first try — and worse, **you can't tell** whether the single answer you got is a good one or a slip-up. Asking once is like flipping a coin.

Self-consistency fixes this: across many tries, **correct reasoning tends to land on the same answer**, while **mistakes are random and scatter**. So the right answer piles up votes; the wrong ones don't agree with each other.

> [!WARNING]
> ⚙️ **One setting you must get right:** for the 7 runs to differ, the AI must be allowed to vary a little — that's the **temperature** dial set **above 0** (we use `0.7`). If you leave temperature at `0`, all 7 runs are identical and voting is pointless. This is the #1 beginner mistake here.

#### ❓ When do I use it / skip it?

| ✅ Use it when… | 🚫 Skip it when… |
|:--|:--|
| The problem is genuinely **hard** (math, logic) | The problem is **easy** (one try is already right) |
| Getting it **right matters more than speed/cost** | You're in a hurry or on a tight budget |
| You'd like a **confidence number** for free | There's no single "correct" answer (e.g., writing a poem) |

> 💰 **The catch:** asking 7 times costs ~7× the money and time. Use it where accuracy is worth that.

---

### 🟩 Technique 2 — Prompt Chaining

#### ❓ What is it?

Instead of asking the AI to do **one big complicated job** in a single instruction, you break the job into a **few small simple steps**, and run them **one after another** — handing the result of step 1 into step 2, step 2 into step 3.

> 🧒 **Analogy (just an analogy):** A kitchen assembly line. One station chops, the next cooks, the next plates. Each station does exactly one simple thing, and the dish moves down the line. Much easier to run — and to spot which station messed up — than one cook trying to do everything at once.

> 📦 **Concrete example (the support email from Lab 3):** An angry customer emails about a broken power bank. The big job is *"read this, figure out the problem, decide what to do, and write a reply."* Chained, it becomes three small steps:
> - **Step 1 — Extract:** pull out the plain facts → *product: power bank · problem: won't charge · mood: angry · urgency: high*
> - **Step 2 — Decide:** look at those facts and choose an action → *refund* (recent purchase, urgent, angry)
> - **Step 3 — Write:** use the facts + the decision to write the actual reply.
>
> Each arrow hands the previous result to the next step.

#### ❓ Why does it exist? (the problem it solves)

If you cram everything into **one giant instruction** and the reply comes out bad, you have **no idea which part broke** — did it misread the email? pick the wrong action? just write badly? It's a sealed black box.

Chaining gives you two wins:
1. 👀 **You can look at the result of each step** and instantly see where it went wrong.
2. ✅ **Each small step is simpler**, so the AI does each one **more reliably** than the all-in-one version.

> [!NOTE]
> 🧠 **Bonus you'll appreciate later:** because each step is separate, you can use a **cheap** model for the easy steps (extract, format) and a **stronger** model only for the hard step (decide). Cheaper *and* often better.

#### ❓ When do I use it / skip it?

| ✅ Use it when… | 🚫 Skip it when… |
|:--|:--|
| The job has **natural stages** | It's a genuine **one-step** task |
| You want to **check the work in the middle** | Splitting would lose important context |
| You want to **mix cheap + strong** models | — |

---

### 🟪 Technique 3 — ReAct (Reason + Act)

#### ❓ What is it?

ReAct is a **loop** where the AI alternates between **thinking** and **doing**:

1. 🧠 The AI **thinks**: *"I need fact X."*
2. 🎯 The AI **asks for a tool**: *"please look up X."* (It only asks — it does not run anything.)
3. ⚙️ **Your program runs the tool** and hands back the real result.
4. 👁️ The AI **sees that real result** and **thinks again**.
5. 🔁 Repeat — think, ask, see, think — until the AI has enough to give the final answer ✅.

> 🚨 **The one thing beginners get wrong — read this twice:**
> **The AI is the brain. It never runs anything itself.** It can only *say* "please look up the distance to the Sun" — like a manager writing an instruction on a sticky note. **Your program is the hands**: it reads that note, *actually* does the lookup, and hands the real number back. Then the brain continues.

Here's exactly who does what in each part of the loop. The third column ("What actually happens") is the part that makes it click:

| # | 🪜 Part of the loop | 🤔 Who does it | 💡 What actually happens (the snail of detail) |
|:-:|:--|:--|:--|
| 1 | 🧠 **Thought** | **The AI (brain)** | It reasons about the next move: *"I need the Sun–Earth distance first."* |
| 2 | 🎯 **Action** | **The AI (brain)** | It only **names** a tool + input: `lookup("earth_sun_distance_m")`. It does **NOT** execute anything — it's just a request. |
| 3 | ⚙️ **Tool runs** | **Your code (hands)** | Your Python reads that request, actually runs the function, and gets back `149,600,000,000`. |
| 4 | 👁️ **Observation** | **Your code (hands)** | Your code feeds that real number back into the AI's next prompt. |
| 5 | 🔁 **Repeat** | **both, taking turns** | The brain reasons on the new fact; the hands fetch the next one. Back and forth. |
| 6 | ✅ **Finish** | **The AI (brain)** | When it has enough, the AI stops asking for tools and writes the final answer. |

> 📦 **Concrete example (the light question from Lab 2):** *"How many seconds does light take to travel from the Sun to the Earth?"*
> 1. 🧠 AI thinks: *"I need the Sun–Earth distance."* → 🎯 asks `lookup("earth_sun_distance_m")`
> 2. ⚙️ Your code returns `149,600,000,000` m → 👁️ fed back
> 3. 🧠 AI thinks: *"Now I need the speed of light."* → 🎯 asks `lookup("speed_of_light_m_per_s")`
> 4. ⚙️ Your code returns `299,792,458` m/s → 👁️ fed back
> 5. 🧠 AI thinks: *"Divide distance by speed."* → 🎯 asks `calculate("149600000000 / 299792458")` *(it uses a calculator tool because AIs are bad at big-number arithmetic)*
> 6. ⚙️ Your code returns `499.0` → 👁️ fed back
> 7. ✅ AI answers: *"About 499 seconds."*

#### ❓ Why does it exist? (the problem it solves)

A plain AI, asked that light question, would just answer **from memory** — and it might **make up** the distance or **botch** the giant division, because it has no way to *check* anything.

> 🧒 **Analogy (just an analogy):** It's like a student taking a quiz from memory, with no calculator and no textbook — they'll guess and sometimes guess wrong. ReAct hands that student a **calculator** and a **reference book**. Now they can look facts up and compute exactly, instead of guessing.

So ReAct exists to **ground the AI in real information and exact computation** instead of relying on its (fallible) memory.

#### ❓ When do I use it / skip it?

| ✅ Use it when… | 🚫 Skip it when… |
|:--|:--|
| Answering needs **outside info** (current data, a database, web search) | It's **pure reasoning** with nothing to look up |
| Answering needs **exact math** the AI can't do in its head | The back-and-forth loop would be **too slow** |

> [!TIP]
> 🎯 **Carry this away:** 🧠 the AI **reasons and decides** · ⚙️ your code **acts and reports** · ReAct is the **conversation between them**. This is the seed of every AI *agent* you'll build in Category 4.

---

## 🔧 3. Each technique's failure → fix, in practice

Section 2 told you *what* each technique is. This section shows the **before/after** — the concrete failure you'd hit without it, and the fix.

### 🟦 Self-consistency

> [!CAUTION]
> ❌ **Without it:** You ask the snail puzzle once. The AI says "12." You ship it. It's wrong, and you never knew the answer was a coin-flip.

> [!TIP]
> ✅ **With it:** You ask 7 times and vote. 5 say "10," 2 say "12." You ship "10" — and the 5/7 split warns you it wasn't a slam dunk. → 🧪 Lab 1.

### 🟩 Prompt chaining

> [!CAUTION]
> ❌ **Without it (mega-prompt):** *"Read this email, decide what to do, write a reply"* in one shot. The reply is off — but you can't tell whether it misread the email, picked the wrong action, or just wrote poorly. Black box.

> [!TIP]
> ✅ **With it:** Three steps. You can read the extracted facts and the chosen action *before* the reply is written, so you see exactly where any problem starts. → 🧪 Lab 3.

### 🟪 ReAct

> [!CAUTION]
> ❌ **Without it:** Ask the light question to a plain AI. It invents a distance and fumbles the division. Confident, wrong.

> [!TIP]
> ✅ **With it:** Give it a `lookup` tool and a `calculate` tool and run the loop. It fetches the real numbers and does exact math. Confident *and* right. → 🧪 Lab 2.

---

## 🗺️ 4. Concept → Code Map

A quick lookup table from "the idea" to "the line of code that does it."

| 💭 Idea | 💻 Code pattern |
|:--|:--|
| 🟦 Run the same prompt N times | a `for` loop making N calls at `temperature=0.7` (must be > 0) |
| 🟦 Read each answer reliably | structured output (`response_schema`) with an `answer` field — *from Day 6* |
| 🟦 Take the majority | `Counter(answers).most_common(1)[0]` |
| 🟦 Confidence number | `votes_for_winner / N` |
| 🟪 One ReAct turn | a `ReActStep` model with `thought`, `action`, `action_input` |
| 🟪 The loop | `for step in range(MAX_STEPS):` → read step → run tool → add observation |
| 🟪 Pick which tool to run | a simple `if action == "lookup": ...` table |
| 🟪 Safety limit | `MAX_STEPS` cap + a `finish` action the AI can choose |
| 🟩 A chain | `out1 = step1(x); out2 = step2(out1); out3 = step3(out2)` |
| 🟩 Pass data between steps | each step returns a typed object the next step reads |

---

## 🧰 5. Best Tools / Tech Stack

| 🎯 Need | 🛠️ Tool | 💬 Why |
|:--|:--|:--|
| 🟦 Self-consistency | **Roll your own** (a loop + `Counter`) | It's ~10 lines; no library does it for you |
| 🟦🟩 Read AI output reliably | **Pydantic v2** | The Day 6 tool — typed fields beat fragile text-parsing |
| 🟪 ReAct (to learn) | **Raw Python loop** | Build it by hand so it's not "magic" later |
| 🟪 ReAct (in production) | **LangGraph** | The 2026 standard agent framework (Day 25) |
| 🟩 Chaining (to learn) | **Raw Python functions** | A chain is just functions calling functions |
| 🟩 Chaining (in production) | **LangChain (LCEL)** / **LangGraph** | Compose chains with state and branching |
| 👁️ Watch what happened | **LangSmith** / **Langfuse** | See every step and loop turn (Category 7) |

> [!NOTE]
> 🎒 **Today we use raw Python + Pydantic for all three.** We deliberately build them by hand so that when LangGraph runs a ReAct loop *for* you later, you already know what's under the hood.

---

## 🧪 6. Lab Walkthroughs

> [!NOTE]
> 🔑 Every script reads your key with `os.getenv("GOOGLE_API_KEY")` and prints with `rich`. No new installs needed.

### 📁 6.1 Make the folder and files (PowerShell)

```powershell
New-Item -ItemType Directory -Path "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition" -Force | Out-Null

New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\01_self_consistency.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\02_react_loop.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\03_prompt_chaining.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\expected_outputs.md"
```

### 🟦 6.2 Lab 1 — `01_self_consistency.py` (ask 7 times, vote)

```python
"""
01_self_consistency.py  🟦  Ask the SAME hard question many times, take the majority answer.

The idea: one run is a coin-flip on a tricky problem. Seven runs + a vote is stable,
because correct reasoning agrees with itself while mistakes scatter.
Reference: Wang et al. 2022 (https://arxiv.org/abs/2203.11171).
"""

import os                                    # lets us read environment variables (the API key)
from collections import Counter              # counts how many times each answer appeared (the vote)
from dotenv import load_dotenv               # loads variables from your .env file into the program
from rich.console import Console             # gives us colorful terminal printing
from pydantic import BaseModel, Field        # lets us define the exact shape of the AI's answer
from google import genai                     # the Gemini SDK
from google.genai import types               # config objects for the SDK

load_dotenv()                                # read .env so GOOGLE_API_KEY becomes available
console = Console()                          # make one printer we reuse everywhere
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))   # connect to Gemini using your key
MODEL = "gemini-2.5-flash-lite"              # the cheap, fast model we default to

# Define the shape of ONE answer. Because we ask for this shape, Gemini returns a clean
# object we can read directly (resp.parsed) instead of digging an answer out of free text.
class Solution(BaseModel):
    reasoning: str = Field(description="Step-by-step reasoning")             # the AI's working-out
    answer: int = Field(description="The final day number, integer only")   # the value we vote on

# The puzzle. The trap answer is 12; the correct answer is 10.
PROBLEM = (
    "A snail is at the bottom of a 12-meter well. Each day it climbs up 3 meters, "
    "but each night it slides back down 2 meters. On which day does it first reach "
    "the top of the well?"
)

def sample_once() -> Solution | None:
    """Run the question ONE time and return the AI's answer object."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=PROBLEM + "\n\nThink step by step, then give the final day number.",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # ask Gemini to reply as JSON, not prose
            response_schema=Solution,                # the JSON must match our Solution shape
            thinking_config=types.ThinkingConfig(
                thinking_budget=0,                   # turn off the model's hidden reasoning so we
            ),                                       #   are testing our OWN prompt, not its built-in mode
            temperature=0.7,                         # ⚠️ ABOVE 0 so each run reasons a bit differently
        ),                                           #   (at 0 you'd get 7 identical answers = no vote)
    )
    return resp.parsed                               # a ready-to-use Solution object

def self_consistency(n: int = 7) -> None:
    """Run the question n times, then take the majority answer."""
    answers: list[int] = []                          # we'll collect each run's answer here
    for i in range(1, n + 1):                        # do n separate runs
        sol = sample_once()                          # one run
        if sol is None:                              # if a run came back unreadable, skip it
            console.print(f"[red]sample {i}: unreadable, skipped[/red]")
            continue
        answers.append(sol.answer)                   # record this run's vote
        console.print(f"sample {i}: answer = [cyan]{sol.answer}[/cyan]")

    if not answers:                                  # nothing usable came back at all
        console.print("[red]No valid samples.[/red]")
        return

    tally = Counter(answers)                         # e.g. Counter({10: 5, 12: 2})
    winner, votes = tally.most_common(1)[0]          # the answer with the most votes
    confidence = votes / len(answers)                # how many runs agreed, as a fraction

    console.rule("[bold]Result[/bold]")
    console.print(f"All votes:       [yellow]{dict(tally)}[/yellow]")
    console.print(f"Majority answer: [bold green]{winner}[/bold green] "
                  f"({votes}/{len(answers)} runs agreed = {confidence:.0%} confidence)")

if __name__ == "__main__":
    self_consistency(n=7)
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\01_self_consistency.py
```
📺 The **voting visual in chat** shows this exact run: watch 7 answers come in and "10" win.

### 🟪 6.3 Lab 2 — `02_react_loop.py` (think → act → observe → repeat)

```python
"""
02_react_loop.py  🟪  The AI thinks and asks for tools; YOUR CODE runs the tools.

Remember the split: the AI is the brain (it reasons and NAMES a tool); your code is the
hands (it runs the tool and hands the result back). This loop repeats until the AI finishes.
Reference: Yao et al. 2022 (https://arxiv.org/abs/2210.03629).
"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from typing import Literal                       # lets us restrict a field to a fixed set of words
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# ⚙️ THE TOOLS — these belong to YOUR CODE. The AI can only ask for them by name.
# A tiny fact book the AI can look things up in. (A real agent would use a database or web search.)
KNOWLEDGE = {
    "speed_of_light_m_per_s": 299_792_458,        # speed of light, meters per second
    "earth_sun_distance_m": 149_600_000_000,      # Sun–Earth distance, meters
    "earth_moon_distance_m": 384_400_000,         # Earth–Moon distance, meters
}

def run_tool(action: str, action_input: str) -> str:
    """Your code runs the tool the AI asked for, and returns the result as text."""
    if action == "lookup":                                  # the AI asked to look a fact up
        key = action_input.strip()
        # If the key exists, return its value; if not, tell the AI clearly so it can fix its next guess.
        return str(KNOWLEDGE.get(key, f"KEY NOT FOUND. Valid keys: {list(KNOWLEDGE)}"))
    if action == "calculate":                               # the AI asked to do exact math
        try:
            # 🚨 Bare eval is DANGEROUS on untrusted text. We block builtins here for the lab only;
            #    in real code use a safe math parser (e.g. the simpleeval library), never bare eval.
            return str(eval(action_input, {"__builtins__": {}}, {}))
        except Exception as e:
            return f"CALC ERROR: {e}"                       # tell the AI the math failed, so it retries
    return f"UNKNOWN ACTION: {action}"

# 🧠 THE AI'S TURN — one structured step. Forcing this shape (Day 6) makes the loop reliable to read.
class ReActStep(BaseModel):
    thought: str = Field(description="Your reasoning about the next move")
    action: Literal["lookup", "calculate", "finish"] = Field(  # the AI must pick one of these three
        description="lookup a fact, calculate an expression, or finish with the answer"
    )
    action_input: str = Field(
        description="For lookup: a key. For calculate: a math expression. For finish: the final answer."
    )

# The instructions we give the AI: the rules of the loop and the tools available to it.
SYSTEM = f"""You answer questions using a Reason+Act loop.
Each step, output a Thought, an Action, and an action_input.
Actions you may use:
  - lookup(key): read a fact. Valid keys: {list(KNOWLEDGE)}
  - calculate(expression): do exact math, e.g. "149600000000 / 299792458"
  - finish(answer): stop and give the final answer
Use only the valid keys. When you have enough, use finish."""

def react(question: str, max_steps: int = 8) -> str:
    """Run the loop: ask the AI for a step, run the tool, feed back the result, repeat."""
    transcript = f"Question: {question}\n"          # the running history the AI sees each turn

    for step in range(1, max_steps + 1):            # 🛡️ max_steps stops a confused AI looping forever
        # Ask the AI for its NEXT step, given everything so far.
        resp = client.models.generate_content(
            model=MODEL,
            contents=SYSTEM + "\n\n" + transcript + "\nWhat is the next step?",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ReActStep,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                temperature=0.0,                    # steady, repeatable reasoning steps
            ),
        )
        s: ReActStep = resp.parsed                  # the AI's {thought, action, action_input}

        console.print(f"[bold]Step {step}[/bold]")
        console.print(f"  🧠 [magenta]Thought:[/magenta] {s.thought}")
        console.print(f"  🎯 [blue]Action:[/blue] {s.action}({s.action_input})")

        if s.action == "finish":                    # the AI decided it has enough → done
            console.print(f"  ✅ [green]Answer:[/green] {s.action_input}")
            return s.action_input

        # Your code runs the requested tool and reports the result back.
        observation = run_tool(s.action, s.action_input)
        console.print(f"  👁️ [yellow]Observation:[/yellow] {observation}")

        # Add this turn to the history so the AI's next thought can use the new fact.
        transcript += (f"\nThought: {s.thought}"
                       f"\nAction: {s.action}({s.action_input})"
                       f"\nObservation: {observation}\n")

    return "Stopped: hit the max step limit without finishing."   # the safety guard fired

if __name__ == "__main__":
    QUESTION = "How many seconds does light take to travel from the Sun to the Earth? Round to the nearest second."
    console.rule("[bold]ReAct loop[/bold]")
    answer = react(QUESTION)
    console.rule("[bold]Done[/bold]")
    console.print(f"Final answer: [bold green]{answer}[/bold green]   (expected ~499 seconds)")
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\02_react_loop.py
```
📺 The **loop step-through visual in chat** walks this exact example, colored by 🧠 AI vs ⚙️ your code.

### 🟩 6.4 Lab 3 — `03_prompt_chaining.py` (one big job → three small steps)

```python
"""
03_prompt_chaining.py  🟩  Break one job into three steps; each step's output feeds the next.

The job: read an angry support email, decide what to do, write a reply.
As a chain, you can INSPECT the result of each step and see exactly where any problem starts.
Related: Zhou et al. 2022, "Least-to-Most Prompting" (https://arxiv.org/abs/2205.10625).
"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from typing import Literal
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# A small helper so we don't repeat the same config three times.
def call(prompt: str, schema, temperature: float = 0.0):
    """Make one structured call. `schema` is the shape the answer must match."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # reply as JSON...
            response_schema=schema,                  # ...in this shape
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=temperature,                 # 0 for facts/logic; higher when writing prose
        ),
    )
    return resp.parsed                               # a typed object the next step can use

# Step 1's output shape: the plain facts pulled from the email.
class Complaint(BaseModel):
    product: str = Field(description="What product the customer is unhappy about")
    issue: str = Field(description="The core problem, one sentence")
    sentiment: Literal["calm", "frustrated", "angry"] = Field(description="The customer's mood")
    urgency: Literal["low", "medium", "high"] = Field(description="How time-sensitive it is")

# Step 2's output shape: the decision, based on Step 1's facts.
class Resolution(BaseModel):
    action: Literal["refund", "replacement", "troubleshoot", "escalate"] = Field(
        description="The single best action to take"
    )
    rationale: str = Field(description="Why this action fits, one sentence")

# Step 3's output shape: the actual reply to send.
class Reply(BaseModel):
    subject: str = Field(description="Email subject line")
    body: str = Field(description="Polite, concise reply under 120 words")

def step1_extract(email_text: str) -> Complaint:
    """🟩 Step 1: messy email -> plain facts (you can read this and check it)."""
    return call(f"Extract the key facts from this support email:\n\n{email_text}", Complaint)

def step2_decide(complaint: Complaint) -> Resolution:
    """🟩 Step 2: facts -> a decision. Note the input is STEP 1's output object."""
    # model_dump_json() turns the Step 1 object back into text the AI can read.
    return call(
        "Given these complaint facts, choose the single best action.\n"
        f"Facts: {complaint.model_dump_json()}",
        Resolution,
    )

def step3_write(complaint: Complaint, resolution: Resolution) -> Reply:
    """🟩 Step 3: facts + decision -> the reply. Slightly higher temp for natural wording."""
    return call(
        "Write a customer support reply.\n"
        f"Facts: {complaint.model_dump_json()}\n"
        f"Decision: {resolution.model_dump_json()}\n"
        "Be warm, acknowledge the problem, and clearly state what you'll do.",
        Reply,
        temperature=0.6,
    )

if __name__ == "__main__":
    EMAIL = (
        "Subject: This is ridiculous!! The Anker power bank I bought THREE WEEKS ago already "
        "won't hold a charge past 20%. I have a flight tomorrow and need this working. "
        "Either fix it or give me my money back."
    )

    console.rule("[bold]🟩 Step 1 — extract the facts[/bold]")
    complaint = step1_extract(EMAIL)                # run step 1
    console.print(complaint.model_dump())            # 👀 you can INSPECT step 1's output here

    console.rule("[bold]🟩 Step 2 — decide the action[/bold]")
    resolution = step2_decide(complaint)            # step 1's output goes INTO step 2
    console.print(resolution.model_dump())           # 👀 inspect step 2's output

    console.rule("[bold]🟩 Step 3 — write the reply[/bold]")
    reply = step3_write(complaint, resolution)      # both feed into step 3
    console.print(f"[bold]Subject:[/bold] {reply.subject}")
    console.print(reply.body)
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\03_prompt_chaining.py
```

### ✅ 6.5 What you should see (`expected_outputs.md`)

```markdown
🟦 Lab 1: per-run answers vary (mostly 10, sometimes 12). Majority = 10, ~5/7.
🟪 Lab 2: lookup distance -> lookup speed -> calculate -> finish ≈ 499 seconds.
🟩 Lab 3: Step1 = power bank / angry / high; Step2 = refund or replacement; Step3 = warm reply.
```

### 💾 6.6 Save your work

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
git add 02-prompt-engineering/day08-composition/
git commit -m "Day 8: combining AI calls — self-consistency, ReAct, prompt chaining"
git push
```

---

## 🚀 7. Production Notes (what bites you in the real world)

### 💰 Cost & speed
- 🟦 Self-consistency costs ~**N times** as much (7 runs = ~7× money and time). Run the samples at the same time (async) to save the time, and only use it where accuracy is worth the money.
- 🟪 ReAct cost grows with **how many loop turns** it takes. Each turn is one AI call + one tool call. Watch the average turn count.
- 🟩 Chaining costs **one call per step** — but you can put a cheap model on the easy steps, which often makes the whole chain cheaper than one big call.

### 🛡️ Safety (do not skip these)
> [!WARNING]
> 🟦 **Temperature must be above 0** for self-consistency, or all your runs are identical and the vote is meaningless.

> [!WARNING]
> 🟪 **Always set a max-steps limit** on a ReAct loop. A confused AI can otherwise loop forever, burning money. (We go deeper on this on Day 30.)

> [!CAUTION]
> 🚨 **Never run `eval()` on the AI's output with untrusted input.** Our calculator uses a locked-down `eval` for teaching only. In real code, use a safe math parser. A malicious input could otherwise run dangerous code on your machine.

---

## 🎤 8. Interview Questions (the crux of the day, in Q&A form)

> [!NOTE]
> 🎯 If you can answer these in your own words, you've got the day. Each answer leads with the one-sentence **crux**.

### 🟢 Conceptual

<details>
<summary>🟢 Q1. What is self-consistency, and why does voting beat a single answer?</summary>

> 🎯 **Crux:** Correct reasoning agrees with itself; mistakes scatter — so across many runs the right answer collects the most votes.

You run the same question several times (temperature above 0 so they differ), collect the answers, and keep the majority. One run on a hard problem is a coin-flip; the vote is stable, and the vote ratio (e.g. 5/7) is a free confidence signal. It costs N×, so it's for hard, high-value problems. ([Wang 2022](https://arxiv.org/abs/2203.11171))
</details>

<details>
<summary>🟢 Q2. In ReAct, who reasons and who runs the tools?</summary>

> 🎯 **Crux:** The AI is the brain — it reasons and *names* a tool. Your code is the hands — it *runs* the tool and returns the result. The AI never runs anything itself.

The loop: 🧠 Thought (AI reasons) → 🎯 Action (AI names a tool) → ⚙️ your code runs it → 👁️ Observation (your code returns the result) → repeat → ✅ Finish (AI answers). Thinking the AI "executes" tools is the most common beginner mistake.
</details>

<details>
<summary>🟢 Q3. Why chain prompts instead of writing one big instruction?</summary>

> 🎯 **Crux:** Small steps are more reliable and you can see which step broke; one big instruction is an opaque black box.

A chain feeds each step's output into the next. You can inspect the middle, test each step alone, and even use a cheap model for easy steps. The trade-off is more calls, so don't chain one-step tasks. ([Zhou 2022](https://arxiv.org/abs/2205.10625))
</details>

<details>
<summary>🟢 Q4. How do these three relate, and what do they have to do with agents?</summary>

> 🎯 **Crux:** They're the three ways to combine calls — parallel (vote), serial (chain), loop (ReAct) — and an AI agent is built by combining them.

An agent is essentially a ReAct loop with more tools and memory, often using chains for sub-tasks and voting on critical decisions.
</details>

### 🟡 Practical

<details>
<summary>🟡 Q5. Implement self-consistency. What's the one setting people get wrong?</summary>

> 🎯 **Crux:** `temperature` must be above 0, or every run is identical and the vote does nothing.

```python
from collections import Counter
def self_consistency(prompt, n=7):
    answers = []
    for _ in range(n):
        resp = client.models.generate_content(
            model="gemini-2.5-flash-lite", contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json", response_schema=Solution,
                temperature=0.7,   # <-- must be > 0
            ),
        )
        answers.append(resp.parsed.answer)
    return Counter(answers).most_common(1)[0]   # (winning answer, vote count)
```
</details>

<details>
<summary>🟡 Q6. Sketch a ReAct loop. What two safety rules are non-negotiable?</summary>

> 🎯 **Crux:** A max-steps cap (so it can't loop forever) and never running tool input through bare `eval` (so it can't execute dangerous code).

```python
def react(q, max_steps=8):
    transcript = f"Question: {q}\n"
    for _ in range(max_steps):               # safety rule 1: bounded loop
        step = ask_ai(SYSTEM + transcript)    # {thought, action, action_input}
        if step.action == "finish":
            return step.action_input
        obs = run_tool(step.action, step.action_input)  # safety rule 2: run_tool sandboxes input
        transcript += f"\nThought:{step.thought}\nAction:{step.action}({step.action_input})\nObservation:{obs}\n"
    return "hit max steps"
```
</details>

<details>
<summary>🟡 Q7. In a chain, how do you pass data between steps and test the middle step alone?</summary>

> 🎯 **Crux:** Each step returns a typed object the next step reads — so you can hand-build that object and test the middle step on its own.

```python
facts = step1_extract(email)        # returns a Complaint object
decision = step2_decide(facts)      # reads facts.model_dump_json() in its prompt
```
To test step 2 alone, build a `Complaint(...)` by hand and call `step2_decide` — no email, no step 1 needed.
</details>

### 🔴 System design

<details>
<summary>🔴 Q8. Design a system that flags risky contracts for legal review. Where do these fit?</summary>

> 🎯 **Crux:** Chain to decompose, vote (self-consistency) on the final risky/not-risky call, and send low-confidence cases to a human.

Chain: extract clauses (cheap) → score each clause (cheap) → overall flag (strong). Vote on the final flag and use the vote ratio as confidence. High-confidence + low-risk → auto; otherwise → human review. Only run the expensive voting path on cases the cheap chain marked unclear. Trace everything for audit.
</details>

<details>
<summary>🔴 Q9. Your ReAct agent runs 30+ steps and never finishes. What's wrong and how do you fix it?</summary>

> 🎯 **Crux:** No bound + no progress check = it spins. Add a step cap, detect repeated actions, and make tool errors informative so the AI self-corrects.

Common causes: no max-steps; the AI repeats a failing action because the error was vague (fix: return "KEY NOT FOUND. Valid keys: [...]"); no clear finish rule (fix: sharpen the instructions and the `finish` action). Production hardening on Day 30.
</details>

<details>
<summary>🔴 Q10. When would you NOT use each technique?</summary>

> 🎯 **Crux:** Don't pay for combining calls when one call already does the job.

🟦 Skip self-consistency on easy or creative tasks and tight budgets. 🟪 Skip ReAct when nothing needs looking up. 🟩 Skip chaining for true one-step jobs. Each technique trades extra cost/time for accuracy, visibility, or grounding — use it only where that trade pays off.
</details>

---

## 🏁 End of Day 8

> [!IMPORTANT]
> 🎯 **The whole day in one line:** 🟦 **vote** when one answer might be a fluke · 🟩 **chain** when one job is really several · 🟪 **loop (ReAct)** when the AI needs to look things up. Combine all three and you get an **agent** — which is exactly where Category 4 takes us.

➡️ **Next: Day 9** — how to *measure* whether a prompt change actually helped (versioning, A/B tests, evaluation). It's the last Prompt Engineering day before we start **RAG**.
