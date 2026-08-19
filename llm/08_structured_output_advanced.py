"""
Return typed structured output using Pydantic.

Requires: OPENAI_API_KEY
Run: uv run 07_structured_output.py
"""

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field, create_model

MODEL = "gpt-5.6-luna"
INSTRUCTIONS = "Come up with random people profiles."

class Profile(BaseModel):
    name: str
    age: int
    profession: str

load_dotenv()

num_people = int(input("Number of profiles to generate: "))

Profiles = create_model(
    "Profiles",
    description=str,
    people=(
        list[Profile],
        Field(min_length=num_people, max_length=num_people),
    ),
)

client = OpenAI()
response = client.chat.completions.parse(
    model=MODEL,
    messages=[
        {"role": "developer", "content": INSTRUCTIONS},
    ],
    response_format=Profiles,
)
print(f"Description: {response.choices[0].message.parsed.description}")
for person in response.choices[0].message.parsed.people:
    print(f"Name: {person.name}, Age: {person.age}, Profession: {person.profession}")
