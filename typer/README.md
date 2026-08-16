# Typer Templates

Twelve small, independently runnable examples of common Typer capabilities.
They share one `uv` project and one virtual environment.

## Setup

From this folder, run:

```bash
uv sync
```

Then run any example directly, for example:

```bash
uv run python 01_basic_command.py --help
```

Each Python module begins with a short description and example commands.

## Examples

1. `01_basic_command.py` — one simple command
2. `02_required_arguments.py` — required positional input
3. `03_options.py` — named options with defaults
4. `04_boolean_flags.py` — on/off switches
5. `05_input_types.py` — numbers and restricted choices
6. `06_files_and_folders.py` — validated paths and output files
7. `07_multiple_commands.py` — several operations in one application
8. `08_prompts_and_confirmation.py` — interactive questions
9. `09_help_and_errors.py` — descriptions and useful validation errors
10. `10_formatted_output.py` — tables and panels with Rich
11. `11_progress.py` — progress bars for longer work
12. `12_automation.py` — predictable output and exit behavior

The examples use a simple complaint-analysis theme. They do not call an LLM or require an API key.
