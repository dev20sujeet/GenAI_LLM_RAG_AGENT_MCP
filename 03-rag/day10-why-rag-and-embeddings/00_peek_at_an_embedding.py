"""
00_peek_at_an_embedding.py  🔍  See what an embedding ACTUALLY looks like when printed.

Before trusting "text becomes numbers," let's just print the numbers and inspect them.
We embed a question and a document, then look at:
  - how MANY numbers there are (the dimensions),
  - what a few of those numbers look like,
  - the vector's "length" (magnitude),
  - and the cosine similarity between the two.
"""

import os                                    # to read the API key from the environment
from dotenv import load_dotenv               # loads variables from your .env file
from rich.console import Console             # colorful terminal printing
import numpy as np                           # fast math on lists of numbers
from google import genai                     # the Gemini SDK
from google.genai import types               # config objects for the SDK

load_dotenv()                                # make GOOGLE_API_KEY available
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
EMBED_MODEL = "gemini-embedding-2"           # the model whose only job is making embeddings


def embed(text: str) -> list[float]:
    """Turn one piece of text into its embedding (a list of 768 numbers)."""
    result = client.models.embed_content(
        model=EMBED_MODEL,
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768),  # ask for 768 numbers
    )
    return result.embeddings[0].values        # the actual list of floats


def peek(label: str, text: str) -> list[float]:
    """Embed `text`, then PRINT what its embedding looks like, and return it."""
    vec = embed(text)                          # the raw embedding (768 floats)

    console.rule(f"[bold]{label}[/bold]")
    console.print(f'[yellow]Text:[/yellow] "{text}"')

    # 1) HOW MANY numbers? This is the "dimensions" — the size of the meaning-space.
    console.print(f"Total numbers (dimensions): [cyan]{len(vec)}[/cyan]")

    # 2) WHAT do the numbers look like? Show the first 8 so it isn't a wall of text.
    first_8 = [round(x, 4) for x in vec[:8]]   # round so it's readable
    console.print(f"First 8 numbers: [green]{first_8}[/green]")
    console.print("[dim]...and 760 more just like them.[/dim]")

    # 3) The vector's "length" (magnitude). np.linalg.norm = sqrt(sum of squares).
    #    gemini-embedding-2 normalizes 768-dim vectors, so this will be ~1.0.
    length = float(np.linalg.norm(vec))
    console.print(f"Vector length (magnitude): [magenta]{length:.4f}[/magenta]")
    console.print()
    return vec


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """1.0 = same meaning, 0 = unrelated. dot product / (length a * length b)."""
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


# Embed and inspect a question and two documents — one related, one not.
question = peek("THE QUESTION", "How many days can I work from home each month?")
doc_good = peek("RELATED DOCUMENT", "Employees may work remotely up to 8 days per month.")
doc_bad  = peek("UNRELATED DOCUMENT", "The office cafeteria serves lunch from 12pm to 2pm.")

# Now compare meanings. The related doc should score MUCH higher than the unrelated one,
# even though the related doc shares almost no words with the question.
console.rule("[bold]Meaning comparison (cosine similarity)[/bold]")
console.print(f"question  vs  related doc:   [bold green]{cosine_similarity(question, doc_good):.3f}[/bold green]")
console.print(f"question  vs  unrelated doc: [bold red]{cosine_similarity(question, doc_bad):.3f}[/bold red]")
console.print(
    "\n[dim]Notice: the numbers themselves look like meaningless noise to a human — but the "
    "MODEL arranged them so that similar meanings point the same way. That hidden arrangement "
    "is the whole magic. You can't read an embedding; you can only compare it.[/dim]"
)