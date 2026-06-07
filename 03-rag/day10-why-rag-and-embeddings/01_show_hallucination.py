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