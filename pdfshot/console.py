import typer
from pdf2image import convert_from_path

# images = convert_from_path("test.pdf", fmt="png", dpi=300)


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")


# Since this is a Python package, there is no need to add the block below.
# if __name__ == "__main__":
#     typer.run(main)
