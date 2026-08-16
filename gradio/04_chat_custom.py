"""A custom chat interface."""

import gradio as gr
from lorem_text import lorem

history: list[dict] = []


def respond(message: str, history: list[dict]) -> str:
    return (
        f"History length: {len(history)}\n"
        f"You said: {message}\n"
        f"I reply: {lorem.words(7)}"
    )

def submit_message(message: str) -> tuple[str, list[dict]]:
    reply = respond(message, history)
    history.extend([
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ])
    return "", history


def last_turn() -> str:
    return history[-2]["content"]


def undo() -> tuple[str, list[dict]]:
    message = last_turn()
    del history[-2:]
    return message, history


def retry() -> tuple[str, list[dict]]:
    message, _ = undo()
    visible_history = history + [{"role": "user", "content": message}]
    return message, visible_history

def clear_history() -> list[dict]:
    history.clear()
    return history

with gr.Blocks(title="Custom Chat", fill_height=True) as demo:
    gr.Markdown("# Custom Chat")
    chatbot = gr.Chatbot(label="My Chatbot", scale=1)

    with gr.Group():
        message = gr.Textbox(
            label="",
            show_label=False,
            placeholder="Type a message...",
            scale=7,
            autofocus=True,
            submit_btn=True)

    message.submit(submit_message, message, [message, chatbot])
    chatbot.undo(undo, outputs=[message, chatbot])
    chatbot.clear(clear_history, outputs=chatbot)
    chatbot.retry(retry, outputs=[message, chatbot]).then(
        submit_message, message, [message, chatbot]
    )


demo.launch()
