from pathlib import Path
from typing import Optional

import typer
from pdf2image import convert_from_path
from PIL import ImageOps
from yaspin import yaspin

from . import __description__, __name__, __version__
from .constants import (
    BORDER_HELP,
    FILE_PATH,
    INPUT_PATH_HELP,
    PDF_PAGE_HELP,
    VERSION_HELP,
)

# Explicit application.
app = typer.Typer()


def export_single_pdf_page_as_image(
    input_path: Path, page_number: int, add_border: bool
) -> None:
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

        if add_border:
            # More info:
            # - https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.expand
            bimg = ImageOps.expand(images[0], border=10, fill="#000000")
            bimg.save(output_name)
        else:
            images[0].save(output_name)

        sp.ok("✅")


def version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__name__}: {__version__}")
        raise typer.Exit()


@app.command(help=__description__)
def main(
    input_path: Path = typer.Argument(..., help=INPUT_PATH_HELP, **FILE_PATH),
    pdf_page: int = typer.Argument(..., help=PDF_PAGE_HELP),
    border: bool = typer.Option(False, "--add-border", "-b", help=BORDER_HELP),
    version: Optional[bool] = typer.Option(
        None, "--version", callback=version_callback, is_eager=True, help=VERSION_HELP
    ),
) -> None:
    export_single_pdf_page_as_image(input_path, pdf_page, border)

    # CLI application directory.
    # typer.echo(typer.get_app_dir(__name__))

    typer.secho("\n✨ Done!", bold=True)


# Since this is a Python package, there is no need to add the block below.
# if __name__ == "__main__":
#     typer.run(main)
#     app()
