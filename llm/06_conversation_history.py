"""
Maintain conversation history explicitly with Chat Completions.

Requires: OPENAI_API_KEY
Run: uv run 06_conversation_history.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
messages = [{"role": "developer", "content": "Reply briefly."}]

while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        messages=messages,
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Assistant:", reply)
