.PHONY: docs readme clean

CMD:=poetry run
DOCS:=docs/

docs:
	$(CMD) typer pdfshot.console utils docs --output $(DOCS)cli.md --name pdfshot
	tail +5 $(DOCS)cli.md > $(DOCS)cli.md.new && mv $(DOCS)cli.md.new $(DOCS)cli.md

readme: docs
	rm -f README.md
	for file in $(DOCS)header.md $(DOCS)cli.md $(DOCS)footer.md ; do \
		cat $$file >> README.md ; \
		echo >> README.md ; \
	done
	# More info: https://stackoverflow.com/a/40066559
	cat README.md | tail -r | tail -n +2 | tail -r > README.md.new && mv README.md.new README.md

clean:
	find . -name "*.png" -type f -delete
