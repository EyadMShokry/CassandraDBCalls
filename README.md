# Cassandra DB CLI Package

This package introduces a CLI program which have only one command so far to get calls records from Cassandra DB based on class durations and callers phone numbers.

## Prerequisites

- [Click~=8.1.3](https://click.palletsprojects.com/en/8.1.x/) is used to write the CLI Program.
- [cassandra-driver~=3.25.0](https://pypi.org/project/cassandra-driver/) is used to deal with Cassandra DB.
- [PyYAML>=6.0](https://pypi.org/project/PyYAML/) is used to parse configuration yaml files.

## Installation

1. Clone or download this repository.
2. Write your Cassandra DB server host, port, and keyspace variables in the `configurations/cassandra_db_connection.yaml`. They will be used to connect and retrieve data records by `CassandraDBHandler` class in `cassandra_db_handler.py` file. 
3. Install the CLI package using pip: `pip install .` (alternatively, you may install the package in editable mode using `pip install -e .`)

## Usage

At any time, you can view usage instructions by entering `cassandra_cli --help`. You will be able to find all the available command groups and helper texts.

### Get Calls

To get calls based on a specific duration and phone number:

```commandline
cassandra_cli calls get --duration '00:00:04' --phone-number '(739) 476-8397'
```

#### Options
- --duration (text): Duration of the desired calls (required).
- --phone-number (text): User Phone Number of the desired calls.
- --help: Shows a help message and exits.