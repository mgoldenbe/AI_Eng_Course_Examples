"""
n, temperature and seed
"""

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "gpt-4o-mini"  # gpt-5.6-luna does not support some parameters

load_dotenv()

client = OpenAI()
for temperature in [0.0, 1.0, 2.0]:
    print(f"\nTemperature: {temperature}")
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "In five words, what is the weather like in July in Paris?"
            }
        ],
        n = 5,
        temperature = temperature,
        seed = 42
    )
    for choice in response.choices:
        print('\t' + choice.message.content)
