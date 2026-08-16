# Gradio Examples

Self-contained examples for **Part 4. Building Web Interfaces with Gradio**.

## Setup

```bash
uv sync
```

## Run an example

Examples 1–7 start their own Gradio server:

```bash
uv run python 01_first_interface.py
```

Stop the server with `Ctrl+C`.

Example 8 mounts Gradio inside FastAPI:

```bash
uv run uvicorn 08_fastapi:app --reload
```

Then open:

- <http://127.0.0.1:8000/health>
- <http://127.0.0.1:8000/app>

## Advanced authentication example

Example 7 uses these demonstration accounts:

- `founder` / `founder-pass`
- `tester` / `tester-pass`

It checks whether `OPENAI_API_KEY` exists in the server environment but never displays its value. For example, in PowerShell:

```powershell
$env:OPENAI_API_KEY = "your-key"
uv run python 07_authentication.py
```

The hard-coded passwords are for demonstration only, not for a deployed application.
