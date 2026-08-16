"""
An interface with several input and output components.

Run:
    uv run python 02_components.py
"""

from pathlib import Path
from typing import Any

import gradio as gr


def inspect_values(
    text: str,
    count: int,
    enabled: bool,
    category: str,
    input_file: str | None,
) -> tuple[str, int, dict[str, Any], str | None]:
    file_name = Path(input_file).name if input_file else None

    return (
        text,
        count,
        {
            "enabled": enabled,
            "category": category,
            "file_name": file_name,
        },
        input_file,
    )


demo = gr.Interface(
    fn=inspect_values,
    inputs=[
        gr.Textbox(label="Text", placeholder="Enter some text"),
        gr.Slider(1, 10, value=3, step=1, label="Count"),
        gr.Checkbox(label="Enabled"),
        gr.Dropdown(["A", "B", "C"], value="A", label="Category"),
        gr.File(type="filepath", label="Optional file"),
    ],
    outputs=[
        gr.Textbox(label="Text received"),
        gr.Number(label="Count received", precision=0),
        gr.JSON(label="Other values"),
        gr.File(label="Download the uploaded file"),
    ],
    examples=[
        ["Hello", 3, True, "A", None],
        ["Another example", 7, False, "C", None],
    ],
    flagging_mode="never",
    title="Components",
)


demo.launch()
