"""Day 4 Experiment 3: Few-shot gone wrong — biased examples lead to biased outputs."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

TEST_REVIEW = "The food was okay. Service was a bit slow but the staff was friendly."


def biased_few_shot() -> str:
    """All 3 examples are negative — model will likely classify ANYTHING as negative."""
    system = "You classify restaurant reviews as POSITIVE, NEGATIVE, or NEUTRAL."

    prompt = """Examples:

Review: "Worst meal of my life. Sent it back."
Classification: NEGATIVE

Review: "The waiter was rude and forgot our drinks."
Classification: NEGATIVE

Review: "Food was cold by the time it arrived."
Classification: NEGATIVE

Now classify this:
Review: "{review}"
Classification:""".format(review=TEST_REVIEW)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.0,
        ),
    )
    return response.text.strip()


def balanced_few_shot() -> str:
    """Same task, but examples cover all 3 categories."""
    system = "You classify restaurant reviews as POSITIVE, NEGATIVE, or NEUTRAL."

    prompt = """Examples:

Review: "Loved every bite. Coming back next week!"
Classification: POSITIVE

Review: "Worst meal of my life. Sent it back."
Classification: NEGATIVE

Review: "It was fine. Nothing special, nothing bad."
Classification: NEUTRAL

Now classify this:
Review: "{review}"
Classification:""".format(review=TEST_REVIEW)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.0,
        ),
    )
    return response.text.strip()


def main() -> None:
    console.print(Panel.fit(
        f"[bold]Test review (genuinely mixed/neutral):[/bold]\n[cyan]{TEST_REVIEW}[/cyan]",
        border_style="cyan",
    ))
    console.print()

    console.print("[yellow]Biased examples (all 3 are NEGATIVE)...[/yellow]")
    biased = biased_few_shot()
    console.print(Panel(biased, title="[red]BIASED result[/red]", border_style="red"))
    console.print()

    console.print("[yellow]Balanced examples (one of each class)...[/yellow]")
    balanced = balanced_few_shot()
    console.print(Panel(balanced, title="[green]BALANCED result[/green]", border_style="green"))
    console.print()

    console.print("[bold yellow]Lesson:[/bold yellow] "
                  "Your examples ARE the lesson. Skewed examples → skewed model behavior.")


if __name__ == "__main__":
    main()