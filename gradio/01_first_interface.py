"""
A first Gradio application.
"""

import gradio as gr


def foo(text: str) -> str:
    return f"Received: {text}"


demo = gr.Interface(
    fn=foo,
    inputs=gr.Textbox(label="Text"),
    outputs=gr.Textbox(label="Result"),
    title="First Gradio Application",
    flagging_mode="never"
)


demo.launch()
