# 🦅 Day 10 — Welcome to RAG: Why It Exists, the Hallucination Problem & Embeddings

*Category 3 · RAG · Day 10 of 53 · Models: `gemini-2.5-flash-lite` (chat) + `gemini-embedding-2` (embeddings)*

> [!IMPORTANT]
> 🎯 **The big idea, in one breath:** A plain AI answers from **memory** — and memory can be wrong, out of date, or simply never included *your* documents. **RAG** gives the AI an **open book**: before it answers, you *fetch the relevant pages and hand them over*, so it answers from real text instead of guessing. Today is the *why* and the one new building block that makes it possible: **embeddings**.

---

## 🦅 Eagle View — the whole RAG idea before we zoom in

You asked for the bird's-eye picture first. Here it is. **RAG** stands for **R**etrieval-**A**ugmented **G**eneration ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401)):

| Letter | Word | In plain English |
|:-:|:--|:--|
| **R** | Retrieval | **Find** the documents relevant to the question |
| **A** | Augmented | **Add** those documents into the prompt |
| **G** | Generation | The AI **writes** the answer using those documents |

> 🧒 **The master analogy (we'll reuse it all category):** It's the difference between a **closed-book exam** (answer from memory — you might misremember) and an **open-book exam** (look up the right page first, then answer). RAG turns every question into an open-book exam.

The full system has **two phases**. Don't worry about the details yet — just see the shape:

```text
📥  INDEXING  (do this ONCE, ahead of time)
    Your documents ──► split into chunks ──► turn each chunk into an EMBEDDING ──► store in a Vector DB

❓  ANSWERING  (every time someone asks a question)
    Question ──► turn it into an EMBEDDING ──► find the chunks with the closest embeddings ──► put them in the prompt ──► AI answers from them
```

> [!NOTE]
> 🧭 **Where today fits:** see the word **EMBEDDING** in *both* phases? That's the gear that makes RAG turn. **Day 10 is entirely about embeddings.** Then:
> - **Day 11** → choosing a Vector DB (the storage)
> - **Day 12** → splitting documents into chunks + storing them
> - **Day 13** → the actual retrieve-and-answer
>
> 📺 *The eagle-view pipeline is drawn as a diagram in the chat — open it beside this.*

---

## 📚 1. Vocabulary (skim now — it clicks after Section 2)

| 🔤 Term | 💭 Plain-English meaning |
|:--|:--|
| **RAG** | Fetching relevant documents and adding them to the prompt so the AI answers from them. |
| **Hallucination** | When the AI states something false **confidently**, as if it were a fact. |
| **Knowledge cutoff** | The date the AI's training stopped — it knows nothing that happened after. |
| **Embedding** | A list of numbers that captures the **meaning** of a piece of text. |
| **Vector** | Just the technical word for "a list of numbers," e.g. `[0.12, -0.4, 0.9, …]`. |
| **Dimensions** | How many numbers are in the vector (varies by model; `gemini-embedding-2` = 3072 by default, shrinkable to 768 or 1536). |
| **Semantic similarity** | Closeness in **meaning** — what we actually want to search by. |
| **Cosine similarity** | The standard score for how aligned two vectors are: **1.0 = same meaning, 0 = unrelated**. |
| **Embedding model** | A *special* model whose only job is to turn text into embeddings (different from a chat model). |
| **Retrieval** | The step where you find the most relevant chunks for a question. |
| **Grounding** | Making the AI answer *from provided text* instead of from memory. |

---

## 🧭 2. The Concepts, Step by Step (the heart of the day)

### 🚩 The Problem: three things a plain AI simply cannot do

A plain LLM is like a brilliant student who **memorized the whole internet up to a certain day** and then walked into an exam with **no books and no phone**. Three problems follow:

| 🚫 Problem | What goes wrong | Tiny example |
|:--|:--|:--|
| **1. Hallucination** | It would rather make up a confident answer than say "I don't know." | "Cite a study about X" → it invents a real-sounding but fake paper. |
| **2. Knowledge cutoff** | It stopped learning on a fixed date; anything newer is invisible. | "Who won the match last night?" → it can't possibly know. |
| **3. No access to *your* data** | It never read your company handbook, your notes, your private files. | "What's our refund window?" → it has literally never seen your policy. |

> 🧒 **Analogy:** Asking a plain AI about your private handbook is like asking a stranger on the street what *your* house rules are. They'll either admit they don't know — or, worse, confidently guess. Neither helps you.

> [!CAUTION]
> 🚨 **Why hallucination is dangerous, not just annoying:** the AI sounds *equally confident* whether it's right or making things up. There's no "uncertain" tone to warn you. That's exactly why we need to **ground** it in real text.

### 💡 The Fix: RAG = hand it the open book

Instead of hoping the AI *remembers* the right answer, you **find the relevant text first and paste it into the prompt**. Now the AI isn't recalling — it's **reading**. It can quote your actual policy, use today's data, and say "the document doesn't mention that" instead of inventing.

But this raises one hard question… 👇

### 🔢 The New Tool: Embeddings (today's real lesson)

To "find the relevant text," you need to search your documents **by meaning**, not by exact words. Why not exact words? Because a user asks *"How do I reset my password?"* but your doc says *"Steps to recover your login credentials"* — **zero words in common**, same meaning. Keyword search misses it. **Embeddings** fix this.

#### ❓ What is an embedding?

An **embedding** turns a piece of text into a **list of numbers (a vector)** so that **texts with similar meaning get similar numbers**.

> 🧒 **The map analogy (this is the whole concept):** Imagine a giant map where every sentence is a **dot**. Sentences about *dogs* sit together in one neighborhood; sentences about *taxes* sit far away in another. An embedding is just the **map coordinates** of a sentence. Similar meaning → dots **close together**. Different meaning → dots **far apart**.
>
> Real embeddings don't have 2 coordinates (like a real map) — they have **hundreds or thousands** (768, 1536, or 3072 numbers, *varies by model*). We can't picture 768-D space, so we *imagine* it as a 2-D map. 📺 *The "meaning map" visual in chat shows exactly this.*

#### ❓ How do we measure "closeness"? → Cosine similarity

Once two sentences are dots in space, we measure how close their **directions** are using **cosine similarity**:

| Score | Meaning |
|:--|:--|
| **≈ 1.0** | Same direction → **very similar meaning** ✅ |
| **≈ 0.0** | At right angles → **unrelated** |
| **≈ −1.0** | Opposite directions → **opposite meaning** |

> 🧒 **Analogy:** Two people pointing in *almost the same direction* (small angle) ≈ they agree → score near 1. Pointing at *right angles* ≈ unrelated → score near 0. Cosine similarity measures that **angle**, not the distance walked.

> [!NOTE]
> 🧠 **Why an embedding *model*?** Turning text into meaning-aware numbers is itself a learned skill. So there's a **separate** model (`gemini-embedding-2`) whose only job is embeddings — it's not the same as the chat model (`gemini-2.5-flash-lite`). One writes numbers (meaning), the other writes words (answers).

#### ❓ When do I use embeddings?

Anytime you need to **search or compare text by meaning**: RAG retrieval (our main use), finding duplicate questions, grouping similar reviews, recommendation ("more like this"). You do **not** need them for tasks with no search/compare step.

> [!TIP]
> 🎯 **Carry this away:** an **embedding** = text turned into meaning-coordinates; **cosine similarity** = how aligned two of those coordinates are. RAG works by embedding your docs once, embedding each question, and retrieving the chunks whose coordinates sit closest to the question's. That's the entire trick.

---

## 🔧 3. Failure → Fix, in practice (closed book vs open book)

| 🚩 Closed book (plain AI) | ✅ Open book (RAG) |
|:--|:--|
| "What's our remote-work limit?" → invents "15 days" | We retrieve the real handbook line and paste it → it answers "8 days" correctly |
| Confidently wrong, no warning | Answers from the supplied text, or says "not in the document" |
| Can't use today's data or your files | Uses whatever you retrieve and hand it |

You'll *see* this exact contrast in Lab 1 (closed book fails) → Lab 3 (open book succeeds).

---

## 🗺️ 4. Concept → Code Map

| 💭 Idea | 💻 Code pattern |
|:--|:--|
| Turn text into an embedding | `client.models.embed_content(model="gemini-embedding-2", contents=text, config=types.EmbedContentConfig(output_dimensionality=768))` |
| Get the actual numbers | `result.embeddings[0].values` → a list of 768 floats |
| Measure meaning-closeness | cosine similarity = `dot(a,b) / (norm(a) * norm(b))` (we use `numpy`) |
| Retrieve the best chunk | embed the question, score it against every chunk, pick the highest |
| Ground the answer | paste the retrieved chunk into the prompt, then ask the chat model |

---

## 🧰 5. Best Tools / Tech Stack

| 🎯 Need | 🛠️ Tool | 💬 Why |
|:--|:--|:--|
| Make embeddings | **`gemini-embedding-2`** | Current Gemini embedding model; sizes 768/1536/3072 ([docs](https://ai.google.dev/gemini-api/docs/embeddings)) |
| Math on vectors | **NumPy** | The standard Python library for number-lists; one line of cosine similarity |
| Store + search embeddings (Day 11+) | **Chroma** (local), then **Pinecone/Qdrant** (production) | Today we search by hand to learn; a Vector DB does it fast at scale |
| Alternative embedding models | OpenAI `text-embedding-3-small` (1536-D) | If you're on OpenAI instead of Gemini |

> [!NOTE]
> 🎒 **Today we do retrieval BY HAND** (loop + cosine similarity) so you understand what a Vector DB automates. On Day 11 we hand that job to **Chroma**. Add NumPy now:
> ```powershell
> Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
> uv add numpy
> ```

---

## 🧪 6. Lab Walkthroughs

> [!NOTE]
> 🔑 Every script reads your key with `os.getenv("GOOGLE_API_KEY")` and prints with `rich`.

### 📁 6.1 Make the folder and files (PowerShell)

```powershell
New-Item -ItemType Directory -Path "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings" -Force | Out-Null

New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\01_show_hallucination.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\02_embeddings_and_similarity.py"
New-Item -ItemType File "E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\03_babys_first_rag.py"
```

> [!NOTE]
> 📂 New top-level folder `03-rag/` — we've graduated out of `02-prompt-engineering/`. Category 3 begins here.

### 🚩 6.2 Lab 1 — `01_show_hallucination.py` (see the closed-book problem)

```python
"""
01_show_hallucination.py  🚩  Show WHY we need RAG: the AI can't know your private data.

We ask about a made-up company handbook the AI has never seen. Watch it either guess
(hallucinate) or admit it can't know. Either way, the lesson is the same: a plain AI
cannot answer questions about documents it was never given.
"""

import os                                    # to read the API key from the environment
from dotenv import load_dotenv               # loads variables from your .env file
from rich.console import Console             # colorful terminal printing
from google import genai                     # the Gemini SDK
from google.genai import types               # config objects for the SDK

load_dotenv()                                # make GOOGLE_API_KEY available
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
CHAT_MODEL = "gemini-2.5-flash-lite"         # the model that writes answers

# A question about a PRIVATE document the AI has never seen. There is no way it can
# know the real answer — so any confident number it gives is invented (a hallucination).
QUESTION = (
    "According to the internal TechCorp 2026 Employee Handbook, how many days per month "
    "may an employee work remotely? Answer with just the number."
)

resp = client.models.generate_content(
    model=CHAT_MODEL,
    contents=QUESTION,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),   # no hidden reasoning
        temperature=0.0,                                           # steady answer
    ),
)

console.rule("[bold]Closed-book (no documents given)[/bold]")
console.print(f"[yellow]Question:[/yellow] {QUESTION}")
console.print(f"[red]AI's answer:[/red] {resp.text.strip()}")
console.print(
    "\n[dim]The AI has NEVER seen TechCorp's handbook. So it either makes up a number "
    "(hallucination) or admits it can't know. This is the problem RAG solves: in Lab 3 "
    "we'll hand it the real handbook line and it will answer correctly.[/dim]"
)
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\01_show_hallucination.py
```

### 🔢 6.3 Lab 2 — `02_embeddings_and_similarity.py` (the meaning map, for real)

```python
"""
02_embeddings_and_similarity.py  🔢  Turn sentences into number-lists, then measure meaning.

We embed a few sentences, then use cosine similarity to score how close in MEANING they
are. You'll see: a question matches the right doc even with NO shared words, and unrelated
sentences score low. This is the engine of retrieval.
"""

import os
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
import numpy as np                           # NumPy: fast math on lists of numbers
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
EMBED_MODEL = "gemini-embedding-2"           # the model whose ONLY job is making embeddings

def embed(text: str) -> list[float]:
    """Turn one piece of text into its embedding (a list of 768 numbers)."""
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,                                       # the text to embed
        config=types.EmbedContentConfig(
            output_dimensionality=768,                       # ask for 768 numbers (smaller = cheaper)
        ),
    )
    # .embeddings is a list (one entry per input); [0].values is the actual number-list.
    return result.embeddings[0].values

def cosine_similarity(a: list[float], b: list[float]) -> float:
    """How aligned are two vectors? 1.0 = same meaning, 0 = unrelated.
       Formula: dot product divided by the product of their lengths."""
    a = np.array(a)                          # turn the list into a NumPy array (so math is easy)
    b = np.array(b)
    # np.dot(a, b)        = multiply matching numbers and add them up
    # np.linalg.norm(a)   = the "length" of vector a
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# One "question" and several candidate sentences. Notice doc #1 shares NO words with the
# question ("work from home" vs "work remotely") — yet it should still score highest,
# because embeddings compare MEANING, not spelling.
QUESTION = "How many days can I work from home each month?"
DOCS = [
    "Employees may work remotely up to 8 days per month.",      # same meaning, different words
    "The office cafeteria serves lunch from 12pm to 2pm.",      # unrelated
    "Annual leave must be requested two weeks in advance.",     # unrelated-ish
    "Parking permits are available at the front desk for $20.", # unrelated
]

# Step 1: embed the question once.
q_vec = embed(QUESTION)

# Step 2: embed every doc and score it against the question.
table = Table(title="Meaning-similarity to the question")
table.add_column("similarity")
table.add_column("sentence")

scored = []                                  # we'll collect (score, sentence) pairs
for doc in DOCS:
    score = cosine_similarity(q_vec, embed(doc))   # how close in meaning?
    scored.append((score, doc))

# Step 3: sort highest-similarity first, then show the table.
scored.sort(reverse=True)                    # biggest score at the top
for score, doc in scored:
    table.add_row(f"{score:.3f}", doc)

console.print(f"[yellow]Question:[/yellow] {QUESTION}\n")
console.print(table)
console.print(
    "\n[dim]Top row is the remote-work sentence — even though it shares no words with the "
    "question. That's semantic similarity: matching by meaning, not by spelling.[/dim]"
)
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\02_embeddings_and_similarity.py
```
📺 The **meaning-map visual in chat** shows these sentences as dots and the question finding its nearest neighbors.

### ✅ 6.4 Lab 3 — `03_babys_first_rag.py` (open book — the whole RAG idea in 40 lines)

```python
"""
03_babys_first_rag.py  ✅  The smallest possible RAG: retrieve the right line, then answer.

This stitches Lab 1's problem and Lab 2's tool together:
  1) embed the question,
  2) find the most similar document line (RETRIEVAL),
  3) paste it into the prompt (AUGMENT),
  4) ask the chat model (GENERATION).
Same question that failed in Lab 1 — now it answers correctly, because it's reading, not guessing.
"""

import os
from dotenv import load_dotenv
from rich.console import Console
import numpy as np
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
EMBED_MODEL = "gemini-embedding-2"
CHAT_MODEL = "gemini-2.5-flash-lite"

# Our tiny "knowledge base" — pretend this is the TechCorp handbook, split into lines.
DOCS = [
    "Employees may work remotely up to 8 days per month.",
    "The office cafeteria serves lunch from 12pm to 2pm.",
    "Annual leave must be requested two weeks in advance.",
    "Parking permits are available at the front desk for $20.",
]

def embed(text: str) -> list[float]:
    """Text -> embedding (list of 768 numbers)."""
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768),
    )
    return result.embeddings[0].values

def cosine_similarity(a, b) -> float:
    """1.0 = same meaning, 0 = unrelated."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

QUESTION = "How many days can I work from home each month?"

# ---- STEP 1 + 2: RETRIEVAL — find the doc line closest in meaning to the question ----
q_vec = embed(QUESTION)                          # embed the question
best_doc = None                                  # will hold the winning line
best_score = -1.0                                # start lower than any real score
for doc in DOCS:                                 # check every line...
    score = cosine_similarity(q_vec, embed(doc)) # ...how close in meaning?
    if score > best_score:                       # keep the closest one so far
        best_score = score
        best_doc = doc

console.print(f"[blue]Retrieved (score {best_score:.3f}):[/blue] {best_doc}")

# ---- STEP 3: AUGMENT — build a prompt that INCLUDES the retrieved line ----
# The rule "only use the context" is what stops the AI from making things up.
prompt = (
    "Answer the question using ONLY the context below. "
    "If the answer isn't in the context, say you don't know.\n\n"
    f"Context: {best_doc}\n\n"
    f"Question: {QUESTION}"
)

# ---- STEP 4: GENERATION — let the chat model answer from the supplied context ----
resp = client.models.generate_content(
    model=CHAT_MODEL,
    contents=prompt,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        temperature=0.0,
    ),
)

console.rule("[bold]Open-book (RAG)[/bold]")
console.print(f"[yellow]Question:[/yellow] {QUESTION}")
console.print(f"[green]Grounded answer:[/green] {resp.text.strip()}")
console.print(
    "\n[dim]Same question that failed in Lab 1 — but now the AI READ the answer from the "
    "retrieved line instead of guessing. That's RAG: Retrieve -> Augment -> Generate.[/dim]"
)
```

▶️ **Run it:**
```powershell
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\03-rag\day10-why-rag-and-embeddings\03_babys_first_rag.py
```

### 🧾 6.5 What you should see

```text
🚩 Lab 1: the AI invents a number (or admits it can't know) — it never saw the handbook.
🔢 Lab 2: the remote-work sentence scores highest (~0.7+), unrelated ones much lower.
✅ Lab 3: it retrieves the remote-work line and answers "8 days" — correct, from the text.
```

### 💾 6.6 Save your work

```powershell
Set-Location E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP
git add 03-rag/day10-why-rag-and-embeddings/
git commit -m "Day 10: why RAG, hallucination, embeddings + baby's-first-RAG"
git push
```

---

## 🚀 7. Production Notes (what matters in the real world)

### 💰 Cost & speed
- Embeddings are **cheap and fast** compared to chat calls — but you embed *every chunk* of *every document*, so for big corpora it adds up. You **embed documents once** and store them; you only re-embed when documents change.
- Smaller `output_dimensionality` (768 vs 3072) = **less storage and faster search**, with little quality loss thanks to Matryoshka training. Start at 768.

### 🛡️ Do this right
> [!IMPORTANT]
> 🧠 **Query and document embeddings should use a matching `task_type`.** `gemini-embedding-2` accepts a `task_type` (e.g. `RETRIEVAL_QUERY` for questions, `RETRIEVAL_DOCUMENT` for stored text). We skipped it today for simplicity, but setting it improves retrieval quality. We'll use it properly when we build the real pipeline.

> [!CAUTION]
> 🚨 **Always tell the model to use ONLY the context** (like Lab 3's prompt) and to say "I don't know" otherwise. Without that instruction it may *blend* the context with its memory — and slip a hallucination back in.

- 🔁 **Searching by hand (a `for` loop) is fine for a few dozen lines** but far too slow for thousands. That's the entire reason Vector DBs exist (Day 11) — they find nearest neighbors in milliseconds.
- 🌐 **Pick one embedding model and stick with it** for a given store. You can't compare embeddings made by *different* models — their "maps" don't line up.

---

## 🎤 8. Interview Questions (the crux of the day)

> [!NOTE]
> 🎯 Answer these in your own words and you own the day. Each answer leads with the one-sentence **crux**.

### 🟢 Conceptual

<details>
<summary>🟢 Q1. Why does RAG exist? What three problems does it solve?</summary>

> 🎯 **Crux:** A plain LLM answers from memory, which can (1) hallucinate, (2) be out of date past its knowledge cutoff, and (3) never include your private data — RAG fixes all three by retrieving real text and letting the model answer from it.

It's a closed-book exam vs an open-book exam. RAG = Retrieve the relevant docs → Augment the prompt with them → Generate the answer from them. The model stops recalling and starts reading. ([Lewis et al. 2020](https://arxiv.org/abs/2005.11401))
</details>

<details>
<summary>🟢 Q2. What is an embedding, in one sentence?</summary>

> 🎯 **Crux:** An embedding is a list of numbers (a vector) that captures a text's meaning, so texts with similar meaning get numerically similar vectors.

Picture every sentence as a dot on a giant map of meaning: similar meanings sit close together, different meanings far apart. The embedding is just that dot's coordinates — typically hundreds to thousands of numbers (varies by model).
</details>

<details>
<summary>🟢 Q3. Why search by embeddings instead of by keywords?</summary>

> 🎯 **Crux:** Keyword search needs shared words; embedding search matches by meaning, so "reset my password" finds "recover your login credentials" despite zero shared words.

Users rarely phrase questions the way your documents are written. Meaning-based (semantic) search bridges that gap, which is why retrieval is built on embeddings, not keyword matching.
</details>

<details>
<summary>🟢 Q4. What does cosine similarity tell you?</summary>

> 🎯 **Crux:** How aligned two vectors' *directions* are — 1.0 means same meaning, 0 means unrelated, −1 means opposite.

It measures the **angle** between two vectors, not the distance between them. Small angle → near 1 → very similar meaning. Right angle → near 0 → unrelated. It's the standard score for ranking which chunks are most relevant to a question.
</details>

### 🟡 Practical

<details>
<summary>🟡 Q5. Write the two functions at the heart of retrieval: embed and cosine similarity.</summary>

> 🎯 **Crux:** Embed turns text into numbers; cosine similarity scores two number-lists by meaning.

```python
def embed(text):
    r = client.models.embed_content(
        model="gemini-embedding-2", contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768))
    return r.embeddings[0].values

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
```
Retrieval = embed the question, score it against every chunk, keep the highest.
</details>

<details>
<summary>🟡 Q6. Walk through the four steps of a minimal RAG call.</summary>

> 🎯 **Crux:** Embed the question → find the most similar chunk (Retrieve) → paste it into the prompt (Augment) → ask the model with "use only this context" (Generate).

```python
q = embed(question)                                   # 1. embed the question
best = max(DOCS, key=lambda d: cosine_similarity(q, embed(d)))  # 2. retrieve
prompt = f"Use ONLY this context.\nContext: {best}\nQuestion: {question}"  # 3. augment
answer = chat_model(prompt)                           # 4. generate
```
The "use ONLY this context" instruction is what prevents the model from slipping back into hallucination.
</details>

### 🔴 System design

<details>
<summary>🔴 Q7. When does searching embeddings with a for-loop break, and what replaces it?</summary>

> 🎯 **Crux:** A for-loop scores the query against *every* chunk — fine for dozens, hopeless for thousands/millions; a Vector DB finds nearest neighbors in milliseconds.

At scale you can't re-embed and compare everything per query. A Vector DB (Chroma, Pinecone, Qdrant — Day 11) stores embeddings in an index built for fast nearest-neighbor search, so retrieval stays fast no matter how big the corpus grows. You also embed documents once and store them, rather than re-embedding on every query.
</details>

<details>
<summary>🔴 Q8. Your RAG system retrieves the right document but the answer is still wrong/made-up. What are the likely causes?</summary>

> 🎯 **Crux:** Either the prompt didn't force "use only the context," or the model blended context with memory — grounding is a prompt-discipline problem, not just a retrieval problem.

Check: (1) Does the prompt explicitly say "answer using ONLY the context, otherwise say you don't know"? (2) Is the retrieved chunk actually complete enough to contain the answer (a too-small chunk may cut it off — chunking, Day 12)? (3) Are query and document embeddings made by the *same* model with matching task types? Fix grounding in the prompt first; it's the cheapest lever.
</details>

---

## 🏁 End of Day 10 — RAG has begun! 🎉

> [!IMPORTANT]
> 🎯 **The whole day in one line:** a plain AI guesses from memory (hallucination, cutoff, no access to your files); **RAG** hands it the open book instead. The gear that makes it work is the **embedding** — text turned into meaning-coordinates — and **cosine similarity** finds the closest ones. You just built a tiny end-to-end RAG by hand.

➡️ **Next: Day 11 — choosing a Vector Database.** That `for`-loop search you wrote today won't survive thousands of documents. A Vector DB (we'll start with **Chroma**) stores all your embeddings and finds the nearest ones instantly — the storage half of the eagle-view pipeline.
