"""
Generate an image and save it as generated.png.

Requires: OPENAI_API_KEY
Run: uv run 11_generate_image.py
"""

import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
response = client.images.generate(
    model="gpt-image-2",
    prompt="A simple blue robot icon on a white background.",
    size="1024x1024",
    quality="low",
)
with open("generated.png", "wb") as file:
    file.write(base64.b64decode(response.data[0].b64_json))
print("Saved generated.png")
