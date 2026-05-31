"""
02_ab_test.py  ⚖️  Run TWO prompt versions on the SAME eval set and see which wins.

This reuses the harness idea from Lab 1, but now we test two versions:
  v1 = vague   ("categorize this")
  v2 = clear   (lists the categories and what each means)
Whichever scores higher is the better prompt — proven, not guessed.

uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\02_ab_test.py

"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

HERE = Path(__file__).parent
EVAL_DIR = HERE / "eval_set"
with open(EVAL_DIR / "questions.json", encoding="utf-8") as f:
    questions = json.load(f)
with open(EVAL_DIR / "answer_key.json", encoding="utf-8") as f:
    answer_key = {x["id"]: x["category"] for x in json.load(f)}

# 🏷️ VERSIONING: we keep both prompt versions in a dictionary, labeled v1 and v2.
# Old versions aren't lost — we can compare them and roll back any time.
PROMPTS = {
    "v1": "Categorize this message.\n\nMessage: {message}",   # vague on purpose
    "v2": (                                                    # clear and specific
        "Categorize this support message into exactly one of: billing, technical, general.\n"
        "Definitions: billing = payments, charges, refunds, subscriptions; "
        "technical = bugs, crashes, errors, login problems; "
        "general = anything else.\n"
        "Reply with only the one category word, lowercase.\n\n"
        "Message: {message}"
    ),
}

def classify(prompt_template: str, message: str) -> str:
    """Run one message through a given prompt version; return the cleaned guess."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt_template.format(message=message),
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text.strip().lower()

def evaluate(prompt_template: str) -> float:
    """THE HARNESS: run a prompt version on the whole eval set, return its accuracy."""
    correct = 0
    for q in questions:
        predicted = classify(prompt_template, q["message"])
        if predicted == answer_key[q["id"]]:    # compare to ground truth
            correct += 1
    return correct / len(questions)             # the accuracy number

# Run the harness once per version and remember each score.
scores = {}
for version, template in PROMPTS.items():
    scores[version] = evaluate(template)
    console.print(f"{version}: [cyan]{scores[version]:.0%}[/cyan]")

# Declare the winner: whichever version has the higher score.
winner = max(scores, key=scores.get)            # the key (version) with the biggest value
console.print(f"\n🏆 Winner: [bold green]{winner}[/bold green] "
              f"({scores[winner]:.0%} vs {min(scores.values()):.0%}) — proven, not guessed.")