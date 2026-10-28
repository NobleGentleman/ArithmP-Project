import click

from .parser import Parser


@click.command()
def main():
    parser = Parser()

    while True:
        line = input(">>> ")
        if line == "exit":
            break
        click.echo(parser.parse(line))


if __name__ == "__main__":
    main()
