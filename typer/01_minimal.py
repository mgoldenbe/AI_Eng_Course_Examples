"""
The smallest Typer application.

Run:
    python 01_minimal.py
    python 01_minimal.py --help
"""

import typer


def foo():
    print("Inside foo.")


typer.run(foo)
