"""Day 4 Experiment 2: Few-shot for tone matching — harder than format."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Task: rewrite formal corporate emails in a punchy startup-founder tone
# This is a tone task — almost impossible to nail with instructions alone.

TEST_EMAIL = (
    "Dear team, I would like to inform you that we will be implementing "
    "a new policy regarding remote work attendance, effective the first "
    "of next month. Please review the attached document at your earliest convenience."
)


def zero_shot() -> str:
    """Try to describe the tone in words."""
    system = (
        "You are an editor. Rewrite the user's formal corporate email "
        "in a punchy, casual, energetic startup-founder tone. "
        "Be direct, use short sentences, and avoid corporate jargon."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=TEST_EMAIL,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.5,
        ),
    )
    return response.text.strip()


def few_shot() -> str:
    """Show the tone with 2 examples instead of describing it."""
    system = "You are an editor. Rewrite formal corporate emails in a punchy startup-founder tone."

    prompt = """Examples of rewrites:

Formal: "Per our previous discussion, I would like to schedule a follow-up meeting to align on next steps."
Punchy: "Quick sync to lock in next steps?"

Formal: "We regret to inform you that the proposed timeline is not feasible given current resource constraints."
Punchy: "Timeline doesn't work — we're stretched thin. Let's talk."

Now rewrite this:
Formal: "{email}"
Punchy:""".format(email=TEST_EMAIL)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.5,
        ),
    )
    return response.text.strip()


def main() -> None:
    console.print(Panel.fit(
        f"[bold]Original formal email:[/bold]\n[cyan]{TEST_EMAIL}[/cyan]",
        border_style="cyan",
    ))
    console.print()

    console.print("[yellow]Zero-shot (described tone)...[/yellow]")
    zero = zero_shot()
    console.print(Panel(zero, title="[red]ZERO-SHOT[/red]", border_style="red"))
    console.print()

    console.print("[yellow]Few-shot (showed tone with examples)...[/yellow]")
    few = few_shot()
    console.print(Panel(few, title="[green]FEW-SHOT[/green]", border_style="green"))
    console.print()

    console.print("[bold]What to look for:[/bold]")
    console.print("• Zero-shot: probably still a bit formal, longer than needed.")
    console.print("• Few-shot: should be 1-2 short punchy sentences, matching the example style.")


if __name__ == "__main__":
    main()