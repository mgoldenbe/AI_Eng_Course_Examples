"""
Mount a Gradio application inside a FastAPI backend.

Run:
    uv run uvicorn 08_fastapi:app --reload

Open:
    http://127.0.0.1:8000/health
    http://127.0.0.1:8000/app
"""

from fastapi import FastAPI

import gradio as gr


app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def echo(text: str) -> str:
    return text


demo = gr.Interface(
    fn=echo,
    inputs=gr.Textbox(label="Text"),
    outputs=gr.Textbox(label="Result"),
)

app = gr.mount_gradio_app(app, demo, path="/app")
