from pathlib import Path

import typer as typer

app = typer.Typer()


@app.command()
def modify(
    path: Path = typer.Option(...),
    speed: float = typer.Option(...),
    volume: float = typer.Option(...),
) -> None:
    pass


@app.command()
def stt(
    path: Path = typer.Option(...),
) -> None:
    pass


if __name__ == '__main__':
    app()
