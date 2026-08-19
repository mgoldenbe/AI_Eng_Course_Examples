"""
Use a special-purpose sentiment-classification model from Hugging Face.
"""

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

MODEL = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
load_dotenv()

client = InferenceClient()
results = client.text_classification(
    "I absolutely loved this course.",
    model=MODEL,
)
for result in results:
    print(result.label, f"{result.score:.1%}")
