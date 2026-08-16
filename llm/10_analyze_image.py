"""
Create a toy image locally and ask a vision-capable model about it.

Requires: OPENAI_API_KEY
Run: uv run 10_analyze_image.py
"""

import base64
import io
import os
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

image = Image.new("RGB", (200, 120), "red")
buffer = io.BytesIO()
image.save(buffer, format="PNG")
data = base64.b64encode(buffer.getvalue()).decode()

load_dotenv()

client = OpenAI()
response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What is the dominant color? Answer with one word."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{data}"}},
        ],
    }],
)
print(response.choices[0].message.content)
