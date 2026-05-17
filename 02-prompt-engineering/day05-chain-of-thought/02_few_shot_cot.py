"""Day 5 Experiment 2: Few-shot CoT — examples teach reasoning STYLE."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

TEST_PROBLEM = (
    "Alice, Bob, and Carol each ordered one of: pizza, salad, sushi. "
    "Alice didn't order salad. Bob didn't order sushi. Carol ordered sushi. "
    "What did Alice order?"
)


def _ask(system: str, contents: str) -> str:
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system, temperature=0.0,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    ).text.strip()


def zero_shot() -> str:
    return _ask("Answer the logic puzzle. Just give the final answer.", TEST_PROBLEM)


def zero_shot_cot() -> str:
    return _ask("Solve the puzzle step by step, then give the final answer.", TEST_PROBLEM)


def few_shot_cot() -> str:
    prompt = """Example 1:
Puzzle: "Tom, Sam, and Joe each like one of: red, blue, green. Tom doesn't like blue. Sam likes red. What does Joe like?"
Reasoning:
- Sam likes red (given).
- Tom doesn't like blue, so Tom likes red or green. Sam has red, so Tom likes green.
- That leaves blue for Joe.
Final answer: Joe likes blue.

Example 2:
Puzzle: "Three people have one of: cat, dog, fish. Anna has fish. Beth doesn't have a cat. What does Carl have?"
Reasoning:
- Anna has fish (given).
- Beth doesn't have cat, so Beth has dog or fish. Anna has fish, so Beth has dog.
- That leaves cat for Carl.
Final answer: Carl has cat.

Now solve this:
Puzzle: "{problem}"
Reasoning:""".format(problem=TEST_PROBLEM)
    return _ask("Solve logic puzzles step by step, in the style of the examples.", prompt)


def main() -> None:
    console.print(Panel.fit(
        f"[bold]Logic puzzle (correct: pizza):[/bold]\n[cyan]{TEST_PROBLEM}[/cyan]",
        border_style="cyan",
    ))
    for label, fn, color in [
        ("Zero-shot (no reasoning)", zero_shot, "red"),
        ("Zero-shot CoT (think, no examples)", zero_shot_cot, "yellow"),
        ("Few-shot CoT (reasoning examples)", few_shot_cot, "green"),
    ]:
        console.print()
        console.print(Panel(fn(), title=f"[{color}]{label}[/{color}]", border_style=color))


if __name__ == "__main__":
    main()