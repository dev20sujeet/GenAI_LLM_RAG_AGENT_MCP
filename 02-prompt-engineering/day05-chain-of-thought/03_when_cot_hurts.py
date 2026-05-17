"""Day 5 Experiment 3: When CoT is wasted — token cost without benefit."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SIMPLE_QUERIES = [
    "What is the capital of France?",
    "Translate 'hello' to Spanish.",
    "Is 'I loved it!' positive or negative sentiment?",
    "What is 2 + 2?",
]


def ask(query: str, use_cot: bool) -> dict:
    system = "Think step by step before answering." if use_cot else "Answer directly and concisely."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
        config=types.GenerateContentConfig(
            system_instruction=system, temperature=0.0,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )
    return {
        "answer": response.text.strip()[:60],
        "tokens": response.usage_metadata.candidates_token_count,
    }


def main() -> None:
    table = Table(title="Simple queries — direct vs CoT", show_lines=True)
    table.add_column("Query", width=35)
    table.add_column("Direct (tokens)", style="red")
    table.add_column("CoT (tokens)", style="yellow")
    table.add_column("Overhead", style="bold")

    total_direct = total_cot = 0
    for q in SIMPLE_QUERIES:
        d = ask(q, use_cot=False)
        c = ask(q, use_cot=True)
        overhead = c["tokens"] / max(d["tokens"], 1)
        total_direct += d["tokens"]
        total_cot += c["tokens"]
        table.add_row(q, str(d["tokens"]), str(c["tokens"]), f"{overhead:.1f}x")

    console.print(table)
    console.print(f"\n[bold]Total direct:[/bold] {total_direct} tokens")
    console.print(f"[bold]Total CoT:[/bold]    {total_cot} tokens")
    console.print(f"[bold yellow]CoT used {total_cot/max(total_direct,1):.1f}x more tokens for no accuracy gain.[/bold yellow]")


if __name__ == "__main__":
    main()