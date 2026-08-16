"""
Stream generated text and show the most likely alternatives for each token.

Requires: OPENAI_API_KEY
Run: uv run 03_watch_token_generation.py
"""

import math
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
stream = client.chat.completions.create(
    model=os.getenv("OPENAI_LOGPROBS_MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": "Complete briefly: The capital of France is"}],
    stream=True,
    logprobs=True,
    top_logprobs=5,
)

for chunk in stream:
    for item in chunk.choices[0].logprobs.content or []:
        print(f"\nChosen: {item.token!r}")
        for alternative in item.top_logprobs:
            print(f"  {alternative.token!r:18} {math.exp(alternative.logprob):6.1%}")
