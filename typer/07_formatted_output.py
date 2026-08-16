"""
Demonstrates a table and a highlighted panel using Rich.

Run:
    uv run python 07_formatted_output.py
"""

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def main() -> None:
    console.print(
        "[bold yellow]⚠ Warning:[/] Six more urgent complaints require [red]immediate[/] attention."
    )

    table = Table(title="Complaint Summary")
    table.add_column("Topic")
    table.add_column("Count", justify="right")
    table.add_column("Urgent", justify="right")
    table.add_row("Delivery", "12", "3")
    table.add_row("Billing", "8", "1")
    table.add_row("Product", "5", "2")

    console.print(table)
    console.print(
        Panel(
            "Process the next urgent complaint.",
            title="Next Action",
            border_style="green",
        )
    )


typer.run(main)
