from . import __version__ as VERSION
from typing import Union
from pathlib import Path

import yaml


def add_intro_text(help_text: str) -> str:
    """Return version and disclaimer text + help text.

    Args:
        help_text (str):  help text

    Returns:
        str: Intro + help_text.
    """
    return f"""Cassandra DB Client v{VERSION}

    {help_text}
    """


def load_yaml(file_path: Union[Path, str]) -> dict:
    """Loads a YAML file as a dictionary.

    Args:
        file_path: Path to logging configuration YAML file.

    Returns: Loaded configuration as a dictionary.
    """
    with open(file_path, "r") as f:
        config = yaml.safe_load(f.read())
    return config
