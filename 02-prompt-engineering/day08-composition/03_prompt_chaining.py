"""
03_prompt_chaining.py  🟩  Break one job into three steps; each step's output feeds the next.

The job: read an angry support email, decide what to do, write a reply.
As a chain, you can INSPECT the result of each step and see exactly where any problem starts.
Related: Zhou et al. 2022, "Least-to-Most Prompting" (https://arxiv.org/abs/2205.10625).

==Code run instructions==

uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\03_prompt_chaining.py

─────────────────────────────────────────────────────────────────────────── 🟩 Step 1 — extract the facts ────────────────────────────────────────────────────────────────────────────
{'product': 'Anker power bank', 'issue': 'The power bank will not hold a charge past 20%.', 'sentiment': 'angry', 'urgency': 'high'}
─────────────────────────────────────────────────────────────────────────── 🟩 Step 2 — decide the action ────────────────────────────────────────────────────────────────────────────
{
    'action': 'replacement',
    'rationale': "The power bank is defective and unable to hold a charge, necessitating a replacement to resolve the customer's issue promptly due to the high urgency."
}
──────────────────────────────────────────────────────────────────────────── 🟩 Step 3 — write the reply ─────────────────────────────────────────────────────────────────────────────
Subject: Regarding your Anker Power Bank - Replacement Process
Dear Customer, we sincerely apologize for the trouble you're experiencing with your Anker power bank not holding a charge past 20%. We understand how frustrating this must be, 
especially with the high urgency of your situation. We've reviewed your case and have decided to send you a replacement unit immediately. You can expect further details regarding the
shipment of your new power bank within 24-48 hours. Thank you for your patience.

"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from typing import Literal
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# A small helper so we don't repeat the same config three times.
def call(prompt: str, schema, temperature: float = 0.0):
    """Make one structured call. `schema` is the shape the answer must match."""
    resp = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",   # reply as JSON...
            response_schema=schema,                  # ...in this shape
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            temperature=temperature,                 # 0 for facts/logic; higher when writing prose
        ),
    )
    return resp.parsed                               # a typed object the next step can use

# Step 1's output shape: the plain facts pulled from the email.
class Complaint(BaseModel):
    product: str = Field(description="What product the customer is unhappy about")
    issue: str = Field(description="The core problem, one sentence")
    sentiment: Literal["calm", "frustrated", "angry"] = Field(description="The customer's mood")
    urgency: Literal["low", "medium", "high"] = Field(description="How time-sensitive it is")

# Step 2's output shape: the decision, based on Step 1's facts.
class Resolution(BaseModel):
    action: Literal["refund", "replacement", "troubleshoot", "escalate"] = Field(
        description="The single best action to take"
    )
    rationale: str = Field(description="Why this action fits, one sentence")

# Step 3's output shape: the actual reply to send.
class Reply(BaseModel):
    subject: str = Field(description="Email subject line")
    body: str = Field(description="Polite, concise reply under 120 words")

def step1_extract(email_text: str) -> Complaint:
    """🟩 Step 1: messy email -> plain facts (you can read this and check it)."""
    return call(f"Extract the key facts from this support email:\n\n{email_text}", Complaint)

def step2_decide(complaint: Complaint) -> Resolution:
    """🟩 Step 2: facts -> a decision. Note the input is STEP 1's output object."""
    # model_dump_json() turns the Step 1 object back into text the AI can read.
    return call(
        "Given these complaint facts, choose the single best action.\n"
        f"Facts: {complaint.model_dump_json()}",
        Resolution,
    )

def step3_write(complaint: Complaint, resolution: Resolution) -> Reply:
    """🟩 Step 3: facts + decision -> the reply. Slightly higher temp for natural wording."""
    return call(
        "Write a customer support reply.\n"
        f"Facts: {complaint.model_dump_json()}\n"
        f"Decision: {resolution.model_dump_json()}\n"
        "Be warm, acknowledge the problem, and clearly state what you'll do.",
        Reply,
        temperature=0.6,
    )

if __name__ == "__main__":
    EMAIL = (
        "Subject: This is ridiculous!! The Anker power bank I bought THREE WEEKS ago already "
        "won't hold a charge past 20%. I have a flight tomorrow and need this working. "
        "Either fix it or give me my money back."
    )

    console.rule("[bold]🟩 Step 1 — extract the facts[/bold]")
    complaint = step1_extract(EMAIL)                # run step 1
    console.print(complaint.model_dump())            # 👀 you can INSPECT step 1's output here

    console.rule("[bold]🟩 Step 2 — decide the action[/bold]")
    resolution = step2_decide(complaint)            # step 1's output goes INTO step 2
    console.print(resolution.model_dump())           # 👀 inspect step 2's output

    console.rule("[bold]🟩 Step 3 — write the reply[/bold]")
    reply = step3_write(complaint, resolution)      # both feed into step 3
    console.print(f"[bold]Subject:[/bold] {reply.subject}")
    console.print(reply.body)