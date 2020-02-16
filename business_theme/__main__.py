import os
import subprocess
import click


setup_directory = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../'))


@click.group()
def cli():
    pass


@cli.command()
def create():
    print(setup_directory)
    subprocess.call(['cookiecutter', setup_directory])


if __name__ == '__main__':
    cli()
