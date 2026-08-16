"""
The same Chat Completions interface with a local Ollama model.

Before running: ollama pull qwen3:4b
Run: uv run 02_ollama_chat_completion.py
"""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama",  # Required by the client; ignored by local Ollama.
)
response = client.chat.completions.create(
    model="qwen3:4b",
    messages=[{"role": "user", "content": "In one sentence, what is an LLM?"}],
)
print(response.choices[0].message.content)
