"""
A Blocks application with layout, events, and user feedback.

Run:
    uv run python 03_blocks_and_events.py
"""

import gradio as gr


def transform(text: str, uppercase: bool) -> tuple[str, int]:
    text = text.strip()

    if not text:
        raise gr.Error("Enter some text.")

    if len(text) < 5:
        gr.Warning("The text is very short.")

    gr.Info("The text was processed.")
    result = text.upper() if uppercase else text.lower()
    return result, len(result)


def describe_mode(uppercase: bool) -> str:
    return "Uppercase mode" if uppercase else "Lowercase mode"


with gr.Blocks(title="Blocks and Events") as demo:
    gr.Markdown("# Blocks and Events")

    with gr.Row():
        with gr.Column():
            text = gr.Textbox(
                label="Text",
                placeholder="Enter some text",
                lines=4,
            )

            with gr.Accordion("Options", open=True):
                uppercase = gr.Checkbox(label="Use uppercase", value=True)
                mode = gr.Markdown("Uppercase mode")

        with gr.Column():
            result = gr.Textbox(label="Result", lines=4)
            length = gr.Number(label="Number of characters", precision=0)

    with gr.Row():
        run_button = gr.Button("Process", variant="primary")
        gr.ClearButton([text, result, length])

    run_button.click(
        fn=transform,
        inputs=[text, uppercase],
        outputs=[result, length],
    )
    text.submit(
        fn=transform,
        inputs=[text, uppercase],
        outputs=[result, length],
    )
    uppercase.change(
        fn=describe_mode,
        inputs=uppercase,
        outputs=mode,
    )


demo.launch()
