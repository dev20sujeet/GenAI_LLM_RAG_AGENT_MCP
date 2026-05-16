"""Day 2 (Gemini) — first real LLM call, with token counting and cost calculation."""
import os
import time
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.table import Table

load_dotenv()
console = Console()

# Model + pricing (gemini-2.5-flash is free tier; pricing shown for cost math)
MODEL = "gemini-2.5-flash"
INPUT_PRICE_PER_1M = 0.075   # USD per 1M input tokens (paid tier)
OUTPUT_PRICE_PER_1M = 0.30   # USD per 1M output tokens (paid tier)


def calculate_cost(input_tokens: int, output_tokens: int) -> float:
    """Calculate what this call WOULD cost on the paid tier."""
    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_1M
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_1M
    return input_cost + output_cost


def main() -> None:
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = "Explain what an LLM token is in exactly 3 sentences."
    console.print(f"[cyan]Prompt:[/cyan] {prompt}\n")

    # --- Count tokens BEFORE sending (Gemini's tokenizer, no pre-call needed) ---
    predicted = client.models.count_tokens(model=MODEL, contents=prompt)
    console.print(f"[cyan]Predicted input tokens:[/cyan] {predicted.total_tokens}")

    # --- Make the call ---
    console.print(f"\n[yellow]Calling {MODEL}...[/yellow]")
    start = time.perf_counter()
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )
    elapsed = time.perf_counter() - start

    # --- Read the response ---
    answer = response.text
    actual_input_tokens = response.usage_metadata.prompt_token_count
    actual_output_tokens = response.usage_metadata.candidates_token_count
    cost = calculate_cost(actual_input_tokens, actual_output_tokens)

    console.print(f"\n[green]Response:[/green]\n{answer}\n")

    # --- Pretty report ---
    table = Table(title="Day 2 — Cost & Token Report (Gemini)", show_lines=True)
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="white")
    table.add_row("Model", MODEL)
    table.add_row("Predicted input tokens", str(predicted.total_tokens))
    table.add_row("Actual input tokens (from API)", str(actual_input_tokens))
    table.add_row("Actual output tokens", str(actual_output_tokens))
    table.add_row("Total tokens", str(actual_input_tokens + actual_output_tokens))
    table.add_row("Simulated cost (USD, paid tier)", f"${cost:.6f}")
    table.add_row("Simulated cost (millicents)", f"{cost * 100_000:.3f}")
    table.add_row("Latency (seconds)", f"{elapsed:.2f}")
    table.add_row("Actual cost charged", "$0.00 (free tier)")
    console.print(table)


if __name__ == "__main__":
    main()