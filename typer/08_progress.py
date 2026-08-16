"""
Demonstrates a progress bar for a long computation.

Run:
    python 08_progress.py --count 40
"""

import time

import typer


def main(count: int):
    tasks = range(count)

    with typer.progressbar(
        tasks,
        label="Processing...",
    ) as progress:
        for task in progress:
            time.sleep(0.1)  # In real code, process the task instead of sleeping

    print(f"Done")


typer.run(main)
