"""A minimal progress bar for a long-running Gradio task."""

import random
import time

import gradio as gr


def process_indefinite(progress=gr.Progress()):
    for completed in range(1, 21):
        time.sleep(0.2)
        progress((completed, None), desc="Processing...")

        # Simulate discovering that no more work remains as the task runs.
        if completed >= 10 and random.random() < 0.15:
            break

    return f"Done after {completed} items"

with gr.Blocks(title="Long-Running Work") as demo:
    gr.Markdown("# Progress for a Long-Running Task")
    with gr.Row():
        run_indefinite_button = gr.Button("Start indefinite amount of work")
    output = gr.Textbox(label="Result")

    run_indefinite_button.click(fn=lambda: "", outputs=output, queue=False).then(
        fn=process_indefinite,
        outputs=output,
    )

demo.launch()
