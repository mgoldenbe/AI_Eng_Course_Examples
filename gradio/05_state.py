"""A custom chat interface."""

import gradio as gr
from lorem_text import lorem


def respond(message: str, history: list[dict]) -> str:
    return (
        f"History length: {len(history)}\n"
        f"You said: {message}\n"
        f"I reply: {lorem.words(7)}"
    )


def submit_message(message: str, history: list[dict]) -> tuple[str, list[dict], list[dict]]:
    reply = respond(message, history)
    history.extend([
        {"role": "user", "content": message},
        {"role": "assistant", "content": reply},
    ])
    return "", history, history


def last_turn(history: list[dict]) -> str:
    return history[-2]["content"]


def undo(history: list[dict]) -> tuple[str, list[dict], list[dict]]:
    message = last_turn(history)
    del history[-2:]
    return message, history, history


def retry(history: list[dict]) -> tuple[str, list[dict], list[dict]]:
    message = last_turn(history)
    del history[-2:]
    visible_history = history + [{"role": "user", "content": message}]
    return message, visible_history, history


def clear_history(history: list[dict]) -> tuple[list[dict], list[dict]]:
    history.clear()
    return history, history


with gr.Blocks(title="Custom Chat", fill_height=True) as demo:
    gr.Markdown("# Custom Chat")
    history = gr.State([])
    chatbot = gr.Chatbot(label="My Chatbot", scale=1)

    with gr.Group():
        message = gr.Textbox(
            label="",
            show_label=False,
            placeholder="Type a message...",
            scale=7,
            autofocus=True,
            submit_btn=True)

    message.submit(submit_message, [message, history], [message, chatbot, history])
    chatbot.undo(undo, history, [message, chatbot, history])
    chatbot.clear(clear_history, history, [chatbot, history])
    chatbot.retry(retry, history, [message, chatbot, history]).then(
        submit_message, [message, history], [message, chatbot, history]
    )


demo.launch()
