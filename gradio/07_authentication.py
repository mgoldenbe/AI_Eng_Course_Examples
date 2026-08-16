"""
Authentication, authorization, secrets, and security limits.

Run:
    uv run python 07_authentication.py

Demonstration users:
    founder / founder-pass
    tester / tester-pass
"""

import os
from pathlib import Path

import gradio as gr


USERS = {
    "founder": "founder-pass",
    "tester": "tester-pass",
}
ROLES = {
    "founder": "admin",
    "tester": "user",
}
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROJECT_DIR = Path(__file__).resolve().parent


def authenticate(username: str, password: str) -> bool:
    return USERS.get(username) == password


def show_user(request: gr.Request) -> dict[str, object]:
    username = request.username or "unknown"
    return {
        "username": username,
        "role": ROLES.get(username, "unknown"),
        "openai_key_configured_on_server": OPENAI_API_KEY is not None,
    }


def admin_action(text: str, request: gr.Request) -> str:
    username = request.username

    if ROLES.get(username) != "admin":
        raise gr.Error("This operation is restricted to administrators.")

    return f"Administrator {username} submitted: {text}"


with gr.Blocks(title="Authentication and Authorization") as demo:
    gr.Markdown("# Authentication and Authorization")

    user_info = gr.JSON(label="Current user")
    demo.load(fn=show_user, outputs=user_info)

    text = gr.Textbox(label="Administrator input")
    run_button = gr.Button("Run administrator operation")
    output = gr.Textbox(label="Result")

    run_button.click(
        fn=admin_action,
        inputs=text,
        outputs=output,
        api_visibility="private",
    )


# The passwords above are only for a runnable demonstration.
# A real application should use a database or identity provider.
demo.launch(
    auth=authenticate,
    max_file_size="5mb",
    blocked_paths=[
        str(PROJECT_DIR / ".env"),
        str(PROJECT_DIR / ".git"),
    ],
)
