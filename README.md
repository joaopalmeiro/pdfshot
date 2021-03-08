# pdfshot

A Python CLI to export pages from PDF files as images.

## Quickstart

- Install [poppler](http://macappstore.org/poppler/) (macOS): `brew install poppler`.

## Notes

- [pdf2image](https://github.com/Belval/pdf2image):
  - To **only convert** PDF files to images.
- Commands:
  - `poetry init` + `poetry install`.
  - `poetry add "typer[all]"`.
  - `which pdfshot`.
- [Typer](https://github.com/tiangolo/typer):
  - CLI arguments (_required_ by default): CLI parameters (`./myproject`, for example) passed in some specific order to the CLI application (`ls`, for example).
  - CLI options (_optional_ by default): _CLI parameters_ (`--size`, for example) passed to the CLI application with a specific name.

## References

- [Building a Package](https://typer.tiangolo.com/tutorial/package/).
