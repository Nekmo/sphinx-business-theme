import os
import subprocess
import click

from business_theme.google_drive_upload import GoogleDrive

setup_directory = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../'))


@click.group()
def cli():
    pass


@cli.command()
@click.argument('local_file')
@click.argument('remote_file')
@click.argument('folder')
def upload(local_file, remote_file, folder):
    GoogleDrive().upload(local_file, remote_file, folder)


@cli.command()
def create():
    print(setup_directory)
    subprocess.call(['cookiecutter', setup_directory])


if __name__ == '__main__':
    cli()
