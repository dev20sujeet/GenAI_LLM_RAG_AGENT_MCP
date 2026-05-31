"""Day 5 Experiment 1: CoT vs no-CoT on math word problems.
Model only sees questions. Ground-truth answers are in 01b_grade.py
to prevent test-set contamination."""
import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.console import Console

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

QUESTIONS = [
    "A bakery sold 47 loaves on Monday, 23 fewer loaves on Tuesday, and twice as many as Tuesday on Wednesday. How many loaves total over the three days?",
    "A train leaves at 2:00 PM going 45 mph. Another leaves at 2:30 PM from the same station going 60 mph in the same direction. At what time (HH:MM PM) does the second train catch up?",
    "Sarah is 4 times older than Tom. In 6 years, she'll be only twice as old. How old is Tom now?",
    "A store offers 20% off, then an additional 10% off the discounted price. What single discount is equivalent? (Answer as a percentage.)",
    "If 3 workers can complete a job in 12 days, how many days will 5 workers take, assuming all work at the same rate?",
]


def ask_no_cot(question: str) -> str:
    system = (
        "Answer the math question. Respond with ONLY the final numeric answer. "
        "No explanation. Just the number (or HH:MM for time questions)."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.0,
            thinking_config=types.ThinkingConfig(thinking_budget=0),
        ),
    )
    return response.text.strip()


def ask_cot(question: str) -> str:
    system = (
        "Solve the math problem step by step. Show your reasoning. "
        "On the very last line, write 'FINAL ANSWER: <number>' "
        "(or 'FINAL ANSWER: HH:MM' for time questions)."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=0.0,
            #Gemini 2.5 Flash secretly thinks before answering. To see the real effect of CoT prompting, 
            #we disable that with thinking_config=ThinkingConfig(thinking_budget=0). Real production code usually leaves it on."""
            thinking_config=types.ThinkingConfig(thinking_budget=0),             
        ),
    )
    return response.text.strip()


def extract_final_answer(text: str) -> str:
    match = re.search(r"FINAL ANSWER:\s*([^\s\n]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip(".")
    return text.strip().split("\n")[-1].strip(". ")


def main() -> None:
    console.print("[bold cyan]Math problems — CoT vs no-CoT[/bold cyan]")
    console.print("[dim]Gemini 2.5 Flash, T=0, thinking_budget=0[/dim]\n")

    results = []
    for i, q in enumerate(QUESTIONS, 1):
        console.print(f"[yellow]Problem {i}...[/yellow]")
        no_cot = ask_no_cot(q)
        cot_full = ask_cot(q)
        cot_answer = extract_final_answer(cot_full)
        results.append({
            "question_index": i,
            "question": q,
            "no_cot_response": no_cot,
            "cot_full_response": cot_full,
            "cot_extracted_answer": cot_answer,
        })

    out_path = Path(__file__).parent / "responses.json"
    out_path.write_text(json.dumps(results, indent=2))
    console.print(f"\n[bold green]✓ Saved {len(results)} responses to {out_path.name}[/bold green]")
    console.print("[bold]Next:[/bold] run 01b_grade.py to see the scores")


if __name__ == "__main__":
    main()