"""
Compare temperature and random seed.

Requires: OPENAI_API_KEY
Run: uv run 04_temperature_and_seed.py
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
model = os.getenv("OPENAI_SAMPLING_MODEL", "gpt-4o-mini")
prompt = "Invent a short name for a robot that sorts packages."

for temperature, seed in [(0, 1), (1, 1), (1, 2)]:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
        seed=seed,
    )
    print(f"temperature={temperature}, seed={seed}: {response.choices[0].message.content}")
