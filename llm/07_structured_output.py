"""
Return typed structured output using Pydantic.

Requires: OPENAI_API_KEY
Run: uv run 07_structured_output.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

load_dotenv()

client = OpenAI()
response = client.chat.completions.parse(
    model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
    messages=[
        {"role": "developer", "content": "Extract the person."},
        {"role": "user", "content": "Maya is 27 years old."},
    ],
    response_format=Person,
)
print(response.choices[0].message.parsed)
