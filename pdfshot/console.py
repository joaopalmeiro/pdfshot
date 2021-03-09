from pathlib import Path

import typer
from pdf2image import convert_from_path

from . import __description__, __version__

# images = convert_from_path("test.pdf", fmt="png", dpi=300)

# Explicit application.
app = typer.Typer()


# More info: https://typer.tiangolo.com/tutorial/parameter-types/path/.
@app.command(help=__description__)
def main(
    input_path: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        help="The input PDF file.",
    )
):
    if input_path.is_file():
        typer.echo(f"Hello {input_path}")


# Since this is a Python package, there is no need to add the block below.
# if __name__ == "__main__":
#     typer.run(main)
#     app()
