"""Module for main entry point for CLI."""
import click
from . import __app_name__, __version__
from cli.cli_command import calls
from cli.utils import add_intro_text


@click.group(
    help=add_intro_text(
        """Main entry point for Cassandra DB Client CLI.
    Add '--help' to see more information about each command, option or argument."""
    )
)
@click.version_option(version=__version__, prog_name=__app_name__)
def cli():
    """Main group for CLI."""


cli.add_command(calls)


if __name__ == "__main__":
    cli()
