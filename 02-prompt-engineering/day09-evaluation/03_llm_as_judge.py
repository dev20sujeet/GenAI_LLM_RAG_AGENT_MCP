"""
03_llm_as_judge.py  🧑‍⚖️  Score outputs that have NO single right answer.

Exact-match works for categories. But how do you score a SUMMARY? There's no one
"correct" summary to match. The trick: ask a SECOND AI (the "judge") to rate the
summary against the original on a 1-5 scale, with a reason. (Big topic on Day 46.)
Reference: Zheng et al. 2023, "Judging LLM-as-a-Judge" (https://arxiv.org/abs/2306.05685).

//Code run

uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day09-evaluation\03_llm_as_judge.py

"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# A paragraph we want summarized, and a summary the "worker" AI produced.
ORIGINAL = (
    "Our new app update improves battery life by 20%, adds a dark mode, and fixes the "
    "crash that happened when opening Settings. It is rolling out to all users this week."
)

def make_summary(text: str) -> str:
    """The 'worker' AI: produce a one-sentence summary."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=f"Summarize this in one sentence:\n\n{text}",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.text.strip()

# The shape of the JUDGE's verdict. Forcing a number + reason makes it usable as a metric.
class Verdict(BaseModel):
    score: int = Field(description="Quality from 1 (poor) to 5 (excellent)")
    reason: str = Field(description="One-sentence reason for the score")

def judge(original: str, summary: str) -> Verdict:
    """The 'judge' AI: rate the summary against the original, 1-5, with a reason."""
    prompt = (
        "You are grading a summary. Score 1 (poor) to 5 (excellent) based on whether the "
        "summary is accurate and captures the key points of the original.\n\n"
        f"ORIGINAL:\n{original}\n\n"
        f"SUMMARY:\n{summary}"
    )
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # the judge replies as JSON...
            response_schema=Verdict,                 # ...matching our Verdict shape
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=0.0,
        ),
    )
    return resp.parsed

# 1) worker produces a summary  2) judge scores it.
summary = make_summary(ORIGINAL)
verdict = judge(ORIGINAL, summary)

console.print(f"[bold]Summary:[/bold] {summary}")
console.print(f"[bold]Judge score:[/bold] [green]{verdict.score}/5[/green] — {verdict.reason}")
console.print("[dim]Now you can A/B-test summary prompts by comparing their average judge scores.[/dim]")