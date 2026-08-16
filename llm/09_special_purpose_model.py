"""
Use a special-purpose sentiment-classification model from Hugging Face.

Requires: HF_TOKEN
Run: uv run 09_special_purpose_model.py
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(token=os.environ["HF_TOKEN"])
results = client.text_classification(
    "I absolutely loved this course.",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
)
for result in results:
    print(result.label, f"{result.score:.1%}")
