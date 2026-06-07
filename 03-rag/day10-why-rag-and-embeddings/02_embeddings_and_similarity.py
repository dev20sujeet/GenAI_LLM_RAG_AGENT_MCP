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