"""
02_react_loop.py  🟪  The AI thinks and asks for tools; YOUR CODE runs the tools.

Remember the split: the AI is the brain (it reasons and NAMES a tool); your code is the
hands (it runs the tool and hands the result back). This loop repeats until the AI finishes.
Reference: Yao et al. 2022 (https://arxiv.org/abs/2210.03629).



==Run the code==
uv run python E:\GIT_Repo\GenAI_LLM_RAG_AGENT_MCP\02-prompt-engineering\day08-composition\02_react_loop.py

───────────────────────────────────────────────────────────────────────────────────── ReAct loop ─────────────────────────────────────────────────────────────────────────────────────
Step 1
  🧠 Thought: The user is asking for the time it takes for light to travel from the Sun to the Earth. I know the distance between the Earth and the Sun and the speed of light. I can 
calculate the time by dividing the distance by the speed.
  🎯 Action: lookup(earth_sun_distance_m)
  👁️ Observation: 149600000000
Step 2
  🧠 Thought: I have the distance between the Earth and the Sun. Now I need the speed of light to calculate the time. I will use the lookup action to get the speed of light.
  🎯 Action: lookup(speed_of_light_m_per_s)
  👁️ Observation: 299792458
Step 3
  🧠 Thought: I have both the Earth-Sun distance and the speed of light. I can now calculate the time it takes for light to travel from the Sun to the Earth by dividing the distance 
by the speed. The question asks to round to the nearest second, so I will perform the calculation and then round the result.
  🎯 Action: calculate(149600000000 / 299792458)
  👁️ Observation: 499.01188641643546
Step 4
  🧠 Thought: I have calculated the time it takes for light to travel from the Sun to the Earth. The result is approximately 499.01 seconds. The question asks to round to the nearest
second. Therefore, the final answer is 499 seconds.
  🎯 Action: finish(499)
  ✅ Answer: 499
──────────────────────────────────────────────────────────────────────────────────────── Done ────────────────────────────────────────────────────────────────────────────────────────
Final answer: 499   (expected ~499 seconds)

"""

import os
from dotenv import load_dotenv
from rich.console import Console
from pydantic import BaseModel, Field
from typing import Literal                       # lets us restrict a field to a fixed set of words
from google import genai
from google.genai import types

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

# ⚙️ THE TOOLS — these belong to YOUR CODE. The AI can only ask for them by name.
# A tiny fact book the AI can look things up in. (A real agent would use a database or web search.)
KNOWLEDGE = {
    "speed_of_light_m_per_s": 299_792_458,        # speed of light, meters per second
    "earth_sun_distance_m": 149_600_000_000,      # Sun–Earth distance, meters
    "earth_moon_distance_m": 384_400_000,         # Earth–Moon distance, meters
}

def run_tool(action: str, action_input: str) -> str:
    """Your code runs the tool the AI asked for, and returns the result as text."""
    if action == "lookup":                                  # the AI asked to look a fact up
        key = action_input.strip()
        # If the key exists, return its value; if not, tell the AI clearly so it can fix its next guess.
        return str(KNOWLEDGE.get(key, f"KEY NOT FOUND. Valid keys: {list(KNOWLEDGE)}"))
    if action == "calculate":                               # the AI asked to do exact math
        try:
            # 🚨 Bare eval is DANGEROUS on untrusted text. We block builtins here for the lab only;
            #    in real code use a safe math parser (e.g. the simpleeval library), never bare eval.
            return str(eval(action_input, {"__builtins__": {}}, {}))
        except Exception as e:
            return f"CALC ERROR: {e}"                       # tell the AI the math failed, so it retries
    return f"UNKNOWN ACTION: {action}"

# 🧠 THE AI'S TURN — one structured step. Forcing this shape (Day 6) makes the loop reliable to read.
class ReActStep(BaseModel):
    thought: str = Field(description="Your reasoning about the next move")
    action: Literal["lookup", "calculate", "finish"] = Field(  # the AI must pick one of these three
        description="lookup a fact, calculate an expression, or finish with the answer"
    )
    action_input: str = Field(
        description="For lookup: a key. For calculate: a math expression. For finish: the final answer."
    )

# The instructions we give the AI: the rules of the loop and the tools available to it.
SYSTEM = f"""You answer questions using a Reason+Act loop.
Each step, output a Thought, an Action, and an action_input.
Actions you may use:
  - lookup(key): read a fact. Valid keys: {list(KNOWLEDGE)}
  - calculate(expression): do exact math, e.g. "149600000000 / 299792458"
  - finish(answer): stop and give the final answer
Use only the valid keys. When you have enough, use finish."""

def react(question: str, max_steps: int = 8) -> str:
    """Run the loop: ask the AI for a step, run the tool, feed back the result, repeat."""
    transcript = f"Question: {question}\n"          # the running history the AI sees each turn

    for step in range(1, max_steps + 1):            # 🛡️ max_steps stops a confused AI looping forever
                                                    # 🟪 Always set a max-steps limit on a ReAct loop. A confused AI can otherwise loop forever, burning money. (We go deeper on this on Day 30.)
        # Ask the AI for its NEXT step, given everything so far.
        resp = client.models.generate_content(
            model=MODEL,
            contents=SYSTEM + "\n\n" + transcript + "\nWhat is the next step?",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ReActStep,
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                temperature=0.0,                    # steady, repeatable reasoning steps
            ),
        )
        s: ReActStep = resp.parsed                  # the AI's {thought, action, action_input}

        console.print(f"[bold]Step {step}[/bold]")
        console.print(f"  🧠 [magenta]Thought:[/magenta] {s.thought}")
        console.print(f"  🎯 [blue]Action:[/blue] {s.action}({s.action_input})")

        if s.action == "finish":                    # the AI decided it has enough → done
            console.print(f"  ✅ [green]Answer:[/green] {s.action_input}")
            return s.action_input

        # Your code runs the requested tool and reports the result back.
        observation = run_tool(s.action, s.action_input)
        console.print(f"  👁️ [yellow]Observation:[/yellow] {observation}")

        # Add this turn to the history so the AI's next thought can use the new fact.
        transcript += (f"\nThought: {s.thought}"
                       f"\nAction: {s.action}({s.action_input})"
                       f"\nObservation: {observation}\n")

    return "Stopped: hit the max step limit without finishing."   # the safety guard fired

if __name__ == "__main__":
    QUESTION = "How many seconds does light take to travel from the Sun to the Earth? Round to the nearest second."
    console.rule("[bold]ReAct loop[/bold]")
    answer = react(QUESTION)
    console.rule("[bold]Done[/bold]")
    console.print(f"Final answer: [bold green]{answer}[/bold green]   (expected ~499 seconds)")