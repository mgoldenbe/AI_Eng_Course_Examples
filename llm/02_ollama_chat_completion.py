"""
The same Chat Completions interface with a local Ollama model.
"""

from dotenv import load_dotenv
from openai import OpenAI

MODEL = "qwen3:4b"

load_dotenv()

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",
)
response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "In one sentence, what is an LLM?"}],
)
print(response.choices[0].message.content)
