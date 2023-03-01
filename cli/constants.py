"""Constants for Cassandra DB Client CLI."""
from pathlib import Path

# Root directory for CLI package.
CLI_ROOT_DIR = Path(__file__).parent

# Configuration file in configuration directory under package root directory.
LOGGING_CONFIGURATION_FILE_PATH = str(
    Path(CLI_ROOT_DIR, "configurations/cassandra_db_connection.yaml")
)
