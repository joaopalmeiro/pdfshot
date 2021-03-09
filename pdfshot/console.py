from pathlib import Path
from typing import Optional

import typer
from pdf2image import convert_from_path

from . import __description__, __name__, __version__
from .constants import FILE_PATH, INPUT_PATH_HELP, PDF_PAGE_HELP

# images = convert_from_path("test.pdf", fmt="png", dpi=300)

# Explicit application.
app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__name__}: {__version__}")
        raise typer.Exit()


@app.command(help=__description__)
def main(
    input_path: Path = typer.Argument(..., help=INPUT_PATH_HELP, **FILE_PATH),
    pdf_page: int = typer.Argument(..., help=PDF_PAGE_HELP,),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    ),
):
    typer.echo(f"Hello {input_path}")


# Since this is a Python package, there is no need to add the block below.
# if __name__ == "__main__":
#     typer.run(main)
#     app()
