"""
Return typed structured output using Pydantic.

Requires: OPENAI_API_KEY
Run: uv run 07_structured_output.py
"""

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

MODEL = "gpt-5.6-luna"
class Person(BaseModel):
    name: str
    age: int

load_dotenv()

client = OpenAI()
response = client.chat.completions.parse(
    model=MODEL,
    messages=[
        {"role": "developer", "content": "Extract the person's name and age."},
        {"role": "user", "content": "Maya is 27 years old."},
    ],
    response_format=Person,
)
print(f"Name: {response.choices[0].message.parsed.name}")
print(f"Age: {response.choices[0].message.parsed.age}")
