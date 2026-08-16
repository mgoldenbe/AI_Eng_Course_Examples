"""
An example of setting constraints for various types of arguments and options.

Run:
    python 05_constraints.py input.txt
    python 05_constraints.py input.txt --count 3
    python 05_constraints.py --help
"""

from pathlib import Path
from typing import Annotated

import typer


def foo(
    input_path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    count: Annotated[
        int,
        typer.Option(
            min=1,
            max=10,
        ),
    ] = 1,
):
    "The application description."
    print("Inside foo.")


typer.run(foo)
