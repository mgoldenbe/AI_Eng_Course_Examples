"""
Maintain conversation history explicitly with Chat Completions.
"""

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "gpt-5.6-luna"
INSTRUCTIONS = """
Reply briefly.
"""

load_dotenv()

client = OpenAI()
messages = [{"role": "developer", "content": INSTRUCTIONS}]

while True:
    text = input("You: ")
    if text.lower() == "quit":
        break
    messages.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Assistant:", reply)
