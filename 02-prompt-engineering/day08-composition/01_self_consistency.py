"""
01_self_consistency.py  🟦  Ask the SAME hard question many times, take the majority answer.

The idea: one run is a coin-flip on a tricky problem. Seven runs + a vote is stable,
because correct reasoning agrees with itself while mistakes scatter.
Reference: Wang et al. 2022 (https://arxiv.org/abs/2203.11171).


==Run the code==
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\01_self_consistency.py


"""

import os                                    # lets us read environment variables (the API key)
from collections import Counter              # counts how many times each answer appeared (the vote)
from dotenv import load_dotenv               # loads variables from your .env file into the program
from rich.console import Console             # gives us colorful terminal printing
from pydantic import BaseModel, Field        # lets us define the exact shape of the AI's answer
from google import genai                     # the Gemini SDK
from google.genai import types               # config objects for the SDK

load_dotenv()                                # read .env so GOOGLE_API_KEY becomes available
console = Console()                          # make one printer we reuse everywhere
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))   # connect to Gemini using your key
MODEL = "gemini-2.5-flash-lite"              # the cheap, fast model we default to

# Define the shape of ONE answer. Because we ask for this shape, Gemini returns a clean
# object we can read directly (resp.parsed) instead of digging an answer out of free text.
class Solution(BaseModel):
    reasoning: str = Field(description="Step-by-step reasoning")             # the AI's working-out
    answer: int = Field(description="The final day number, integer only")   # the value we vote on

# The puzzle. The trap answer is 12; the correct answer is 10.
PROBLEM = (
    "A snail is at the bottom of a 12-meter well. Each day it climbs up 3 meters, "
    "but each night it slides back down 2 meters. On which day does it first reach "
    "the top of the well?"
)

def sample_once() -> Solution | None:
    """Run the question ONE time and return the AI's answer object."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=PROBLEM + "\n\nThink step by step, then give the final day number.",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # ask Gemini to reply as JSON, not prose
            response_schema=Solution,                # the JSON must match our Solution shape
            thinking_config=types.ThinkingConfig(
                thinking_budget=0,                   # turn off the model's hidden reasoning so we
            ),                                       #   are testing our OWN prompt, not its built-in mode
            temperature=0.7,                         # ⚠️ ABOVE 0 so each run reasons a bit differently 
                                                     #[!WARNING] 🟦 Temperature must be above 0 for self-consistency, or all your runs are identical and the vote is meaningless.
        ),                                           #   (at 0 you'd get 7 identical answers = no vote)
    )
    return resp.parsed                               # a ready-to-use Solution object

def self_consistency(n: int = 7) -> None:
    """Run the question n times, then take the majority answer."""
    answers: list[int] = []                          # we'll collect each run's answer here
    for i in range(1, n + 1):                        # do n separate runs
        sol = sample_once()                          # one run
        if sol is None:                              # if a run came back unreadable, skip it
            console.print(f"[red]sample {i}: unreadable, skipped[/red]")
            continue
        answers.append(sol.answer)                   # record this run's vote
        console.print(f"sample {i}: answer = [cyan]{sol.answer}[/cyan]")

    if not answers:                                  # nothing usable came back at all
        console.print("[red]No valid samples.[/red]")
        return

    tally = Counter(answers)                         # e.g. Counter({10: 5, 12: 2})
    winner, votes = tally.most_common(1)[0]          # the answer with the most votes
    confidence = votes / len(answers)                # how many runs agreed, as a fraction

    console.rule("[bold]Result[/bold]")
    console.print(f"All votes:       [yellow]{dict(tally)}[/yellow]")
    console.print(f"Majority answer: [bold green]{winner}[/bold green] "
                  f"({votes}/{len(answers)} runs agreed = {confidence:.0%} confidence)")

if __name__ == "__main__":
    self_consistency(n=7)