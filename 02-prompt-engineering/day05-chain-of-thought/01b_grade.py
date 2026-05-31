"""Day 5 Experiment 1 grader.
Loads the model responses produced by 01_cot_vs_no_cot.py and compares them
to the answer key. The answer key lives ONLY in this file — the model never
saw it. This is how real ML benchmarks (GSM8K, MMLU) prevent test-set
contamination."""
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

# Ground-truth answers — kept entirely separate from the question file.
# Key = question_index from 01_cot_vs_no_cot.py (1-based, matching QUESTIONS list order)
ANSWER_KEY = {
    1: 119,     # 47 + 24 + 48 (bakery loaves)
    2: "4:00",  # 22.5 mi head start / 15 mph closure rate = 1.5 hr from 2:30 PM
    3: 3,       # Sarah=4T, 4T+6 = 2(T+6) → T=3
    4: 28,      # 0.8 × 0.9 = 0.72, so 28% total discount
    5: 7.2,     # 3 workers × 12 days = 36 worker-days; 36 / 5 = 7.2 days
}


def normalize(answer) -> str:
    """Normalize answers for comparison.
    Handles '3' vs '3.0' vs ' 3 ' vs '3.', and case differences on strings."""
    s = str(answer).strip().strip(".")
    try:
        # Try numeric comparison — '3' and '3.0' both become '3.0'
        return str(float(s))
    except (ValueError, TypeError):
        # Non-numeric (like '4:00') — case-insensitive string compare
        return s.lower()


def main() -> None:
    responses_path = Path(__file__).parent / "responses.json"
    if not responses_path.exists():
        console.print("[red]No responses.json found. Run 01_cot_vs_no_cot.py first.[/red]")
        return

    results = json.loads(responses_path.read_text())

    table = Table(title="Day 5 Lab 1 — Grading Results", show_lines=True)
    table.add_column("#", width=3)
    table.add_column("Truth", width=10)
    table.add_column("No-CoT", style="red", width=18)
    table.add_column("CoT", style="green", width=18)

    no_cot_correct = cot_correct = 0
    for r in results:
        idx = r["question_index"]
        truth = ANSWER_KEY[idx]
        no_cot = r["no_cot_response"]
        cot = r["cot_extracted_answer"]

        no_cot_ok = normalize(no_cot) == normalize(truth)
        cot_ok = normalize(cot) == normalize(truth)
        no_cot_correct += int(no_cot_ok)
        cot_correct += int(cot_ok)

        table.add_row(
            str(idx),
            str(truth),
            f"{no_cot} {'✓' if no_cot_ok else '✗'}",
            f"{cot} {'✓' if cot_ok else '✗'}",
        )

    console.print(table)
    console.print(f"\n[bold red]No-CoT score: {no_cot_correct}/{len(results)}[/bold red]")
    console.print(f"[bold green]CoT score:    {cot_correct}/{len(results)}[/bold green]")
    console.print()
    console.print("[bold]What to look for:[/bold]")
    console.print("• CoT should beat no-CoT by 1-3 problems out of 5")
    console.print("• If both scored 5/5, Gemini's pretraining is too strong for these problems")
    console.print("  — try harder problems or a smaller model to see the gap")


if __name__ == "__main__":
    main()