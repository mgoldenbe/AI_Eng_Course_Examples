"""
An application with several commands.

Run:
    python 02_multiple_commands.py foo
    python 02_multiple_commands.py goo
    python 02_multiple_commands.py --help
"""

import typer

app = typer.Typer(help="This is the application description.")


@app.command()
def foo():
    """
    This is the foo command description.
    """
    print("Inside foo.")


@app.command()
def goo():
    """
    This is the goo command description.
    """
    print("Inside goo.")


app()
