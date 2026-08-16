"""
A basic text-only chat interface.
"""

import gradio as gr
from lorem_text import lorem


def respond(message: str, history: list[dict]) -> str:
    result = (
        f"History length: {len(history)}\n"
        f"You said: {message}\n"
        f"I reply: {lorem.words(7)}"
    )
    return result


demo = gr.ChatInterface(fn=respond, title="Basic Chat")


demo.launch()
