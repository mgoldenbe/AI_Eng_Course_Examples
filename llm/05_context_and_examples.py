"""
Instructions, supplied context, and few-shot examples.

Requires: OPENAI_API_KEY
Run: uv run 05_context_and_examples.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
messages = [
    {
        "role": "developer",
        "content": "Classify the user's message as BILLING or DELIVERY. Use this company rule: refunds are BILLING.",
    },
    {"role": "user", "content": "My parcel arrived three days late."},
    {"role": "assistant", "content": "DELIVERY"},
    {"role": "user", "content": "I was charged twice."},
    {"role": "assistant", "content": "BILLING"},
    {"role": "user", "content": "I want a refund because the box was damaged."},
]
response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
    messages=messages,
)
print(response.choices[0].message.content)
