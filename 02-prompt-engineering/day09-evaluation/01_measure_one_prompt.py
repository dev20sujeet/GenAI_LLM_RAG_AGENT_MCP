"""
01_measure_one_prompt.py  📏  Measure how good ONE prompt is, with a real number.

The plan:
  1) load the test questions (inputs only),
  2) ask the AI to categorize each one,
  3) load the answer key (from a SEPARATE file) and count how many it got right,
  4) print the accuracy.

Why separate files? So the correct answers never touch the prompt. If the AI saw the
answer, it would just copy it and "pass" by cheating. That cheating is called
test-set contamination, and it makes your score meaningless.

COde run 
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\01_measure_one_prompt.py
q1 │ billing   │ billing        │ ✅     │
│ q2 │ technical │ technical      │ ✅     │
│ q3 │ general   │ general        │ ✅     │
│ q4 │ billing   │ billing        │ ✅     │
│ q5 │ technical │ technical      │ ✅     │
└────┴───────────┴────────────────┴────────┘

Score: 5/5 = 100%
"""

import os                                    # to read environment variables (the API key)
import json                                  # to read our .json data files
from pathlib import Path                     # a clean way to build file paths
from dotenv import load_dotenv               # loads variables from .env
from rich.console import Console             # colorful printing
from rich.table import Table                 # pretty results table
from google import genai                     # Gemini SDK
from google.genai import types               # config objects

load_dotenv()                                # make GOOGLE_API_KEY available
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# Path(__file__) is THIS script's location. .parent is the folder it lives in.
# We build paths from here so the script works no matter which folder you run it from.
HERE = Path(__file__).parent
EVAL_DIR = HERE / "eval_set"                 # the sub-folder with our data

# Open the QUESTIONS file (inputs only) and turn the JSON text into a Python list.
with open(EVAL_DIR / "questions.json", encoding="utf-8") as f:
    questions = json.load(f)                 # e.g. [{"id":"q1","message":"..."}, ...]

# Open the ANSWER KEY file (the correct categories) — a DIFFERENT file.
with open(EVAL_DIR / "answer_key.json", encoding="utf-8") as f:
    answer_list = json.load(f)               # e.g. [{"id":"q1","category":"billing"}, ...]

# Turn the answer list into a fast lookup dictionary: id -> correct category.
# (So we can ask "what's the right answer for q3?" instantly.)
answer_key = {item["id"]: item["category"] for item in answer_list}

# The prompt we are testing. {message} is a placeholder we fill in for each question.
PROMPT = (
    "Categorize this support message into exactly one of: billing, technical, general.\n"
    "Reply with only the one category word, in lowercase.\n\n"
    "Message: {message}"
)

def classify(message: str) -> str:
    """Send ONE message to the AI and return its category guess (cleaned up)."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=PROMPT.format(message=message),   # fill the {message} placeholder
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),  # no hidden reasoning
            temperature=0.0,                        # steady, repeatable answers
        ),
    )
    # .strip() removes spaces/newlines; .lower() makes "Billing" match "billing".
    return resp.text.strip().lower()

# Build a results table to show each question's outcome.
table = Table(title="Prompt evaluation")
table.add_column("id")
table.add_column("AI said")
table.add_column("correct answer")
table.add_column("right?")

correct = 0                                  # running count of how many we got right
for q in questions:                          # go through every test question
    predicted = classify(q["message"])       # the AI's guess
    expected = answer_key[q["id"]]           # the ground-truth answer for this id
    is_right = (predicted == expected)       # True if they match exactly
    correct += is_right                      # True counts as 1, False as 0
    mark = "✅" if is_right else "❌"
    table.add_row(q["id"], predicted, expected, mark)

console.print(table)

# Accuracy = how many right, divided by the total. This is our METRIC.
accuracy = correct / len(questions)
console.print(f"\nScore: [bold green]{correct}/{len(questions)} = {accuracy:.0%}[/bold green]")