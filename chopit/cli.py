#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.



"""

import click
import chopit

__version__ = chopit.__version__

class Info(object):
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0



@click.command()
def hello(_: Info):
    """Say 'hello' to the nice people."""
    click.echo("chopit says 'hello'")


@click.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))

@click.group()
@click.version_option(version=__version__)
def cli():
    pass


if __name__ == '__main__':
    cli()