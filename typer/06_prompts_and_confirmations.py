"""
Demonstrates using prompts and yes/no confirmations.

Run:
    python 06_prompts_and_confirmation.py
"""

import typer


def main():
    name_for_greeting = typer.prompt("User name")
    use_title = typer.confirm("Should I call you Mr.?")

    if use_title:
        name_for_greeting = f"Mr. {name_for_greeting}"

    print(f"Hi, {name_for_greeting}!")


typer.run(main)
