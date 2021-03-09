from pathlib import Path
from typing import Optional

import typer
from pdf2image import convert_from_path
from yaspin import yaspin

from . import __description__, __name__, __version__
from .constants import FILE_PATH, INPUT_PATH_HELP, PDF_PAGE_HELP

# Explicit application.
app = typer.Typer()


def export_single_pdf_page_as_image(input_path: Path, page_number: int) -> None:
    with yaspin(text="Processing") as sp:
        images = convert_from_path(
            input_path,
            fmt="png",
            dpi=300,
            first_page=page_number,
            last_page=page_number,
        )

        sp.write("✅ Processing")
        sp.text = "Exporting"

        output_name = f"{input_path.stem}_page{page_number}.png"
        images[0].save(output_name)

        sp.ok("✅")


def version_callback(value: bool):
    if value:
        typer.echo(f"{__name__}: {__version__}")
        raise typer.Exit()


@app.command(help=__description__)
def main(
    input_path: Path = typer.Argument(..., help=INPUT_PATH_HELP, **FILE_PATH),
    pdf_page: int = typer.Argument(..., help=PDF_PAGE_HELP),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True
    ),
):
    export_single_pdf_page_as_image(input_path, pdf_page)

    typer.secho("\n✨ Done!", bold=True)


# Since this is a Python package, there is no need to add the block below.
# if __name__ == "__main__":
#     typer.run(main)
#     app()
