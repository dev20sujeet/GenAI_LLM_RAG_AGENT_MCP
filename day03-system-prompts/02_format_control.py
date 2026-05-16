"""Day 3 Experiment 2: Use system prompts to lock down output format."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

USER_QUESTION = "Tell me about the planet Mars."

# Same question, four different output format constraints
FORMATS = {
    "Free prose (no constraint)": "You are a helpful assistant.",
    "Strict bullet list (5 bullets, max 8 words each)": (
        "You are a fact summarizer. Respond with EXACTLY 5 bullet points. "
        "Each bullet MUST be 8 words or fewer. No introduction. No conclusion. "
        "Just the 5 bullets, starting each with '- '."
    ),
    "Haiku only": (
        "You are a haiku poet. Respond with EXACTLY one haiku — three lines, "
        "5/7/5 syllables. No title. No explanation. Just the haiku."
    ),
    "JSON object only": (
        "You are a structured data API. Respond with ONLY a valid JSON object "
        "with keys: name, type, distance_from_sun_km, key_facts (array of 3 short strings). "
        "No markdown fences. No prose. Just the JSON."
    ),
}


def main() -> None:
    console.print(Panel.fit(
        f"[bold]User question (the SAME for all 4):[/bold]\n[cyan]{USER_QUESTION}[/cyan]",
        border_style="cyan",
    ))
    console.print()

    for format_name, system_prompt in FORMATS.items():
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=USER_QUESTION,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.3,  # lower temp = more obedient to format
            ),
        )
        console.print(Panel(
            response.text,
            title=f"[yellow]{format_name}[/yellow]",
            border_style="yellow",
        ))
        console.print()


if __name__ == "__main__":
    main()