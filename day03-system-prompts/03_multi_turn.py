"""Day 3 Experiment 3: Multi-turn conversation — proving the model has no memory unless you give it some."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM = "You are a helpful tutor. Keep answers under 3 sentences."


def chat_once(history: list[types.Content], user_msg: str) -> tuple[str, list[types.Content]]:
    """Send full history + new user message; return reply + updated history."""
    # Add user message to history
    history.append(types.Content(role="user", parts=[types.Part(text=user_msg)]))

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            temperature=0.5,
        ),
    )

    # Add the model's reply to history (so next turn remembers it)
    history.append(types.Content(role="model", parts=[types.Part(text=response.text)]))
    return response.text, history


def main() -> None:
    history: list[types.Content] = []

    # Turn 1
    console.print("[cyan]User:[/cyan] My name is Kumar and I love .NET.")
    reply, history = chat_once(history, "My name is Kumar and I love .NET.")
    console.print(f"[green]Bot:[/green] {reply}\n")

    # Turn 2 — model SHOULD remember Kumar and .NET because we're sending history
    console.print("[cyan]User:[/cyan] What's my name and what do I love?")
    reply, history = chat_once(history, "What's my name and what do I love?")
    console.print(f"[green]Bot:[/green] {reply}\n")

    # Turn 3 — proof it's all in the history
    console.print(f"[dim]History now contains {len(history)} messages "
                  f"(2 user + 2 model = 4 entries).[/dim]\n")

    # Now do the SAME turn 2 question, but with EMPTY history → model has no idea
    console.print("[cyan]User (with EMPTY history):[/cyan] What's my name and what do I love?")
    reply_no_memory, _ = chat_once([], "What's my name and what do I love?")
    console.print(f"[red]Bot (no memory):[/red] {reply_no_memory}\n")

    console.print("[bold yellow]Key takeaway:[/bold yellow] "
                  "The model has zero built-in memory. Memory = you sending history.")


if __name__ == "__main__":
    main()