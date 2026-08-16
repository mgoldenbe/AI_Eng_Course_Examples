"""A custom chat with multimodal input and streamed replies."""

import time
from collections.abc import Iterator
from typing import Any

import gradio as gr
from lorem_text import lorem

history: list[dict] = []


def respond(message: dict, history: list[dict], word_count: int) -> Iterator[str]:
    reply = (
        f"History length: {len(history)}\n"
        f"You said: {message['text']}\n"
        f"I reply: {lorem.words(word_count)}"
    )
    for character in reply:
        time.sleep(0.05)
        yield character


def history_content(message: dict) -> list:
    content = [{"path": path} for path in message["files"]]
    content.append(message["text"])
    return content


def submit_message(message: dict, word_count: int) -> Iterator[tuple[Any, list[dict]]]:
    previous_history = history.copy()

    history.extend([
        {"role": "user", "content": history_content(message)},
        {"role": "assistant", "content": ""},
    ])

    # Clear the submitted message immediately and only once
    yield {"text": "", "files": []}, history

    for character in respond(message, previous_history, word_count):
        history[-1]["content"] += character
        yield gr.skip(), history


def last_turn() -> list:
    return history[-2]["content"]


def input_message(content: list) -> dict:
    return {
        "text": content[-1],
        "files": [file["path"] for file in content[:-1]],
    }


def undo() -> tuple[dict, list[dict]]:
    message = input_message(last_turn())
    del history[-2:]
    return message, history


def retry() -> tuple[dict, list[dict]]:
    message, _ = undo()
    visible_history = history + [{"role": "user", "content": history_content(message)}]
    return message, visible_history


def clear_history() -> list[dict]:
    history.clear()
    return history


with gr.Blocks(title="Advanced Chat", fill_height=True) as demo:
    gr.Markdown("# Advanced Chat")
    chatbot = gr.Chatbot(label="My Chatbot", scale=1)

    with gr.Group():
        message = gr.MultimodalTextbox(
            label="",
            show_label=False,
            placeholder="Type a message or add a file...",
            scale=7,
            autofocus=True,
            submit_btn=True,
        )
        word_count = gr.Slider(1, 20, value=7, step=1, label="Reply words")

    message.submit(submit_message, [message, word_count], [message, chatbot])
    chatbot.undo(undo, outputs=[message, chatbot])
    chatbot.clear(clear_history, outputs=chatbot)
    chatbot.retry(retry, outputs=[message, chatbot]).then(
        submit_message, [message, word_count], [message, chatbot]
    )


demo.launch()
