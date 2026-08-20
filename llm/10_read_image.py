"""
Read a local image and ask a vision-capable model about it.

Requires: OPENAI_API_KEY
Run: uv run 10_read_image.py
"""

import base64
from dotenv import load_dotenv
from openai import OpenAI

IMAGE_PATH = "error_code.png"
MODEL = "gpt-5.6-luna"
INSTRUCTIONS = "Determine the fault code displayed on the screen in the image."

load_dotenv()

with open(IMAGE_PATH, "rb") as image_file:
    data = base64.b64encode(image_file.read()).decode("utf-8")

client = OpenAI()
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "developer",
            "content": INSTRUCTIONS,
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{data}",
                    },
                },
            ],
        }
    ],
)
print(response.choices[0].message.content)
