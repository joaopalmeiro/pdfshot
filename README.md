# pdfshot

A Python CLI to export pages from PDF files as images.

## Quickstart

- macOS:
  - Install [poppler](http://macappstore.org/poppler/): `brew install poppler`.
- WSL/Ubuntu:
  - Install [poppler](https://pdf2image.readthedocs.io/en/latest/installation.html#installing-poppler): `sudo apt-get install poppler-utils`.

**Usage**:

```console
$ pdfshot [OPTIONS] INPUT_PATH PDF_PAGE
```

**Arguments**:

* `INPUT_PATH`: The input PDF file.  [required]
* `PDF_PAGE`: The page number of the PDF file to export as an image. Page numbering starts at 1 (1-based indexing).  [required]

**Options**:

* `-b, --add-border`: Add border to the page image.  [default: False]
* `--version`: Show the version and exit.
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
  - `pdfshot test.pdf 1` or `pdfshot test.pdf 1 --add-border`.
- [Typer](https://github.com/tiangolo/typer):
  - CLI arguments (_required_ by default): CLI parameters (`./myproject`, for example) passed in some specific order to the CLI application (`ls`, for example).
  - CLI options (_optional_ by default): _CLI parameters_ (`--size`, for example) passed to the CLI application with a specific name.
  - [Data validation](https://typer.tiangolo.com/tutorial/options/callback-and-context/).
  - [Numeric validation](https://typer.tiangolo.com/tutorial/parameter-types/number/).
  - For commands, think of `git` (`git push`, `git clone`, etc.).
- [Poetry](https://python-poetry.org/):
  - [Outdated metadata after version bump for local package](https://github.com/python-poetry/poetry/issues/3289) (open) issue.
- On Windows, to keep the LF line ending ([source](https://stackoverflow.com/questions/9976986/force-lf-eol-in-git-repo-and-working-copy) and [source](https://www.aleksandrhovhannisyan.com/blog/crlf-vs-lf-normalizing-line-endings-in-git/)):
  - `git config core.eol lf`
  - `git config core.autocrlf input`
- Check the line ending format of a file in Ubuntu: `file README.md` vs. `file pyproject.toml` ([source](https://kuantingchen04.github.io/line-endings/))

## References

- [Building a Package](https://typer.tiangolo.com/tutorial/package/).
- [Version CLI Option, is_eager](https://typer.tiangolo.com/tutorial/options/version/).
