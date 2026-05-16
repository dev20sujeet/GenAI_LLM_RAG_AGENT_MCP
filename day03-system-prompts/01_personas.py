"""Day 3 Experiment 1: Same user question + 3 different system prompts = 3 different answers."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

USER_QUESTION = "How should I learn programming?"

# Three different "identities" for the model
PERSONAS = {
    "Strict Drill Sergeant": (
        "You are a strict, no-nonsense drill sergeant. "
        "You give tough love. You speak in short, blunt sentences. "
        "You demand discipline and consistency. Maximum 4 sentences."
    ),
    "Gentle Kindergarten Teacher": (
        "You are a warm, gentle kindergarten teacher. "
        "You explain things with simple words and lots of encouragement. "
        "You use friendly analogies (toys, animals, snacks). Maximum 4 sentences."
    ),
    "Senior FAANG Engineer": (
        "You are a senior staff engineer at a FAANG company. "
        "You are technical, precise, and pragmatic. "
        "You assume the listener already understands software. "
        "You reference specific tools, books, and habits. Maximum 4 sentences."
    ),
}


def ask_with_persona(persona_name: str, system_prompt: str, user_question: str) -> str:
    """Send the same user question with a different system prompt."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_question,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7,
        ),
    )
    return response.text


def main() -> None:
    console.print(Panel.fit(
        f"[bold]User question (the SAME for all 3):[/bold]\n[cyan]{USER_QUESTION}[/cyan]",
        border_style="cyan",
    ))
    console.print()

    for persona_name, system_prompt in PERSONAS.items():
        answer = ask_with_persona(persona_name, system_prompt, USER_QUESTION)
        console.print(Panel(
            answer,
            title=f"[yellow]{persona_name}[/yellow]",
            border_style="yellow",
        ))
        console.print()


if __name__ == "__main__":
    main()