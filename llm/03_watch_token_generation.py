"""
Stream generated text and show the most likely alternatives for each token.

This requires a model that supports log probabilities.  The GPT-5.6 Codex
models stream text but do not expose them, so this example uses gpt-4o-mini.
"""

import math
from dotenv import load_dotenv
from openai import OpenAI

MODEL = "gpt-4o-mini"  # gpt-5.6-luna does not support `logprobs`

load_dotenv()

client = OpenAI()
stream = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "In five words, what is the weather like in July in Paris?"
        }
    ],
    stream=True,
    logprobs=True,
    top_logprobs=5,
)

for chunk in stream:
    choice = chunk.choices[0]
    if not choice.logprobs:
        continue
    for item in choice.logprobs.content:
        print(f"\nChosen: {item.token!r}")
        for alternative in item.top_logprobs:
            print(f"  {alternative.token!r:18}" 
                  f"{math.exp(alternative.logprob):5.2%}")
