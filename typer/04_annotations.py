"""
Using annotations.

Run:
    python 04_annotations.py hello --count 3 -v
    python 04_annotations.py hello -c 3
    python 04_annotations.py --help
"""

from typing import Annotated

import typer


def foo(
    text: Annotated[
        str,
        typer.Argument(help="The text to process."),
    ],
    count: Annotated[
        int,
        typer.Option("--count", "-c", help="Number of repetitions."),
    ] = 1,
    verbose: Annotated[
        bool,
        typer.Option("--verbose", "-v", help="Display additional information."),
    ] = False,
):
    print("Inside foo.")


typer.run(foo)
