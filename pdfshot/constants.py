from typing import Dict

INPUT_PATH_HELP: str = "The input PDF file."
PDF_PAGE_HELP: str = (
    "The page number of the PDF file to export as an image. "
    "Page numbering starts at 1 (1-based indexing)."
)
VERSION_HELP: str = "Show the version and exit."
BORDER_HELP: str = "Add border to the page image."

# More info: https://typer.tiangolo.com/tutorial/parameter-types/path/.
FILE_PATH: Dict[str, bool] = dict(
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)
