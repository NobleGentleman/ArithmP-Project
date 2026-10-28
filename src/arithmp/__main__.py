import click

from .parser import Parser


@click.command()
@click.option("-c", "--command", "expression", help="Expression to evaluate.")
def main(expression: str | None):
    parser = Parser()

    if expression is not None:
        click.echo(parser.parse(expression))
        return

    while True:
        line = input(">>> ")
        if line == "exit":
            break
        try:
            click.echo(parser.parse(line))
        except Exception as error:
            click.echo(f"Error: {error}")


if __name__ == "__main__":
    main()
