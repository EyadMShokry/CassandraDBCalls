from . import __version__ as VERSION

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
