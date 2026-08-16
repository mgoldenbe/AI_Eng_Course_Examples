"""
A command with positional arguments and options.

Run:
    python 03_args_and_options.py hello input.txt
    python 03_args_and_options.py hello input.txt --count 3
    python 03_args_and_options.py hello input.txt --scale 1.5 --verbose
    python 03_args_and_options.py --help
"""

from pathlib import Path

import typer


def foo(
    text: str,
    input_path: Path,
    count: int = 1,
    scale: float = 1.0,
    output_path: Path = Path("output.txt"),
    verbose: bool = False,
):
    "The application description."
    print("Inside foo.")


typer.run(foo)
