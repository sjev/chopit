#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**chopit** - simple static website builder

"""

from pathlib import Path
import click
import chopit

__version__ = chopit.__version__

@click.command()
@click.version_option(version=__version__)
@click.option('--src', default='content', help='source folder for content files')
@click.option('--dest', default='site', help='destination folder ')
def cli(src,dest):
    """ markdown and jinja2 site builder"""

    src_path = Path(src).absolute()
    click.echo(f'Source path: {src_path}')

    dest_path = Path(dest).absolute()

    try:
        assert src_path.exists(), 'Source path not found'

        if not dest_path.exists():
            dest_path.mkdir()

    except Exception as e:
        click.echo(f'Error: {e}')
