"""
Monitoring costs.
"""

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "gpt-5.6-luna"

load_dotenv()

client = OpenAI()
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "In one sentence, what is an LLM?"}],
)
print(response.choices[0].message.content)
print(f"Input tokens: {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
print(f"Cached tokens: {response.usage.prompt_tokens_details.cached_tokens}")