## Notes

- [pdf2image](https://github.com/Belval/pdf2image):
  - To **only convert** PDF files to images.
- Commands:
  - `poetry init` + `poetry install`.
  - `poetry add "typer[all]"`.
  - `which pdfshot`.
  - `pdfshot test.pdf 1`.
- [Typer](https://github.com/tiangolo/typer):
  - CLI arguments (_required_ by default): CLI parameters (`./myproject`, for example) passed in some specific order to the CLI application (`ls`, for example).
  - CLI options (_optional_ by default): _CLI parameters_ (`--size`, for example) passed to the CLI application with a specific name.
  - [Data validation](https://typer.tiangolo.com/tutorial/options/callback-and-context/).
  - [Numeric validation](https://typer.tiangolo.com/tutorial/parameter-types/number/).
  - For commands, think of `git` (`git push`, `git clone`, etc.).
- [Poetry](https://python-poetry.org/):
  - [Outdated metadata after version bump for local package](https://github.com/python-poetry/poetry/issues/3289) (open) issue.

## References

- [Building a Package](https://typer.tiangolo.com/tutorial/package/).
- [Version CLI Option, is_eager](https://typer.tiangolo.com/tutorial/options/version/).
