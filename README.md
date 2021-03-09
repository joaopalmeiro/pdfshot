# pdfshot

A Python CLI to export pages from PDF files as images.

## Quickstart

- Install [poppler](http://macappstore.org/poppler/) (macOS): `brew install poppler`.

**Usage**:

```console
$ pdfshot [OPTIONS] INPUT_PATH PDF_PAGE
```

**Arguments**:

* `INPUT_PATH`: The input PDF file.  [required]
* `PDF_PAGE`: The page number of the PDF file to export as an image.Page numbering starts at 1 (1-based indexing).  [required]

**Options**:

* `--version`
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

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
  - [Data validation](https://typer.tiangolo.com/tutorial/options/callback-and-context/).
  - [Numeric validation](https://typer.tiangolo.com/tutorial/parameter-types/number/).
  - For commands, think of `git` (`git push`, `git clone`, etc.).

## References

- [Building a Package](https://typer.tiangolo.com/tutorial/package/).
- [Version CLI Option, is_eager](https://typer.tiangolo.com/tutorial/options/version/).
