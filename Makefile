.PHONY: docs

CMD:=poetry run

docs:
	$(CMD) typer pdfshot.console utils docs --output API.md --name pdfshot
