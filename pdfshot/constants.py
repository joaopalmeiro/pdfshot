INPUT_PATH_HELP = "The input PDF file."
PDF_PAGE_HELP = (
    "The page number of the PDF file to export as an image."
    "Page numbering starts at 1 (1-based indexing)."
)
VERSION_HELP = "Show the version and exit."

# More info: https://typer.tiangolo.com/tutorial/parameter-types/path/.
FILE_PATH = dict(
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)
