"""
A tiny evaluation harness for an LLM classifier.

Requires: OPENAI_API_KEY
Run: uv run 08_evaluation_harness.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

class Result(BaseModel):
    sentiment: str

load_dotenv()

client = OpenAI()
tests = [
    ("I loved it.", "positive"),
    ("It was awful.", "negative"),
    ("Nothing special.", "neutral"),
]

for text, expected in tests:
    response = client.chat.completions.parse(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        messages=[
            {"role": "developer", "content": "Classify sentiment as positive, negative, or neutral."},
            {"role": "user", "content": text},
        ],
        response_format=Result,
    )
    actual = response.choices[0].message.parsed.sentiment
    print("PASS" if actual == expected else "FAIL", f"{text!r}: expected={expected}, actual={actual}")
