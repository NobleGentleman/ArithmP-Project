import click

from .parser import Parser


@click.command()
@click.option(
    "-c", "--command", "expression", required=True, help="Expression to evaluate."
)
def main(expression: str):
    parser = Parser()
    result = parser.parse(expression)

    click.echo(result)


if __name__ == "__main__":
    main()
