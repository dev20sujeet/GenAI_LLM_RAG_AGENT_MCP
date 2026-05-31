"""
01_basic_structured.py

Goal
----
Extract a typed Person object from a paragraph. Show that:
  - resp.parsed returns a Pydantic instance directly
  - Pydantic does the type-checking for you
  - Field descriptions guide the model

Key teaching points
-------------------
- response_mime_type="application/json" + response_schema=ModelClass is the
  two-line incantation for Gemini structured output.
- The Field(description=...) text is part of the schema and is visible to
  the model. Write it like a prompt, not like internal documentation.
- We still set thinking_budget=0 to keep the teaching loop fast and cheap.
  In production with reasoning models, leave it on for hard extraction tasks.
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from rich.console import Console

load_dotenv()
console = Console()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash-lite"

class Person(BaseModel):
    name: str = Field(description="The person's full name as it appears in the text")
    age: int = Field(description="Age in years; integer only")
    occupation: str = Field(description="Their job title or role")
    company: str | None = Field(
        default=None,
        description="Employer name if mentioned, otherwise null",
    )


TEXT = (
    "Sujeet Kumar is a 41-year-old senior software engineer at Anthropic, "
    "currently focused on AI agent infrastructure."
)

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Person,
    thinking_config=types.ThinkingConfig(thinking_budget=0),
    temperature=0.0,
)

resp = client.models.generate_content(
    model=MODEL,
    contents=f"Extract the person's information from this text:\n\n{TEXT}",
    config=config,
)

# Two ways to look at the output:
print("Raw JSON returned by the model:")
print(resp.text)
print()

# resp.parsed is already a validated Pydantic Person object.
person: Person = resp.parsed
print(f"Typed object: {person!r}")
print(f"  .name      = {person.name}")
print(f"  .age       = {person.age}     (type: {type(person.age).__name__})")
print(f"  .company   = {person.company}")

# Bonus: see what the model actually received as the schema.
# This is what you should mentally treat as part of your prompt.
import json
print("\nJSON schema that the model conditioned on:")
print(json.dumps(Person.model_json_schema(), indent=2))