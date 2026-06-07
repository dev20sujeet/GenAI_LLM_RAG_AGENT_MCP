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