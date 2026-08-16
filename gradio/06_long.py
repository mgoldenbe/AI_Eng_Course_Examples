"""A minimal progress bar for a long-running Gradio task."""

import random
import time

import gradio as gr


def process(count: int, progress=gr.Progress()):
    for completed in range(count):
      progress((completed + 1, count), desc="Processing")
      time.sleep(0.2)

    return "Done"


with gr.Blocks(title="Long-Running Work") as demo:
    gr.Markdown("# Progress for a Long-Running Task")
    count = gr.Slider(1, 20, value=5, step=1, label="Number of items")
    with gr.Row():
        run_button = gr.Button("Process the chosen number of items", variant="primary")
    output = gr.Textbox(label="Result")

    # Explanation of the chain:
    # First clear the output. This should happen immediately, without waiting in the queue of requests to the Gradio backend.
    run_button.click(fn=lambda: "", outputs=output, queue=False).then(
        fn=process,
        inputs=count,
        outputs=output,
    )


demo.launch()
