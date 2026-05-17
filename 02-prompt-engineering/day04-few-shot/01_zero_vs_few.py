"""Day 4 Experiment 1: Same task, zero-shot vs few-shot. Watch the difference."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# The task: convert a customer complaint into a structured "ticket"
# in a very specific format the model has never seen.
# Format: [PRIORITY] | [CATEGORY] | [ONE-LINE SUMMARY]

TEST_COMPLAINT = (
    "I've been a customer for 3 years and today my order arrived "
    "completely smashed. The packaging was torn, the product is unusable, "
    "and this is the second time this month. I want a refund AND a replacement."
)


def zero_shot() -> str:
    """No examples — just describe the task."""
    system = (
        "You are a customer support triage system. "
        "Convert customer complaints into structured tickets in this format: "
        "[PRIORITY] | [CATEGORY] | [ONE-LINE SUMMARY]\n"
        "PRIORITY is one of: LOW, MEDIUM, HIGH, CRITICAL\n"
        "CATEGORY is one of: SHIPPING, PRODUCT_QUALITY, BILLING, ACCOUNT, OTHER\n"
        "SUMMARY is one line, max 12 words."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=TEST_COMPLAINT,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.0,
        ),
    )
    return response.text.strip()


def few_shot() -> str:
    """Same task, but show 3 examples first."""
    system = (
        "You are a customer support triage system. "
        "Convert customer complaints into structured tickets."
    )
    # The user message now includes examples followed by the real task
    prompt = """Here are examples of complaints converted to tickets:

Complaint: "My credit card was charged twice for the same order!"
Ticket: HIGH | BILLING | Duplicate charge on customer order

Complaint: "Just checking when my package will arrive?"
Ticket: LOW | SHIPPING | Customer asking for delivery update

Complaint: "The app keeps crashing every time I try to log in. I can't access my account at all."
Ticket: HIGH | ACCOUNT | App crashes preventing customer login

Now convert this complaint:
Complaint: "{complaint}"
Ticket:""".format(complaint=TEST_COMPLAINT)

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
        f"[bold]Test complaint:[/bold]\n[cyan]{TEST_COMPLAINT}[/cyan]",
        border_style="cyan",
    ))
    console.print()

    console.print("[yellow]Running zero-shot (instructions only)...[/yellow]")
    zero = zero_shot()
    console.print(Panel(zero, title="[red]ZERO-SHOT result[/red]", border_style="red"))
    console.print()

    console.print("[yellow]Running few-shot (3 examples)...[/yellow]")
    few = few_shot()
    console.print(Panel(few, title="[green]FEW-SHOT result[/green]", border_style="green"))
    console.print()

    console.print("[bold]What to look for:[/bold]")
    console.print("• Did zero-shot follow the exact pipe-separated format?")
    console.print("• Did few-shot follow it perfectly?")
    console.print("• Which one is more consistent across runs? (Run it 3 times to test.)")


if __name__ == "__main__":
    main()