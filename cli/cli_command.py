import click
from cli.cassandra_db_handler import CassandraDBHandler


class CallsGetCommand:
    """Calls get command class.

    Attributes:
        _duration: Duration of the calls to be retrieved.
        _phone_number: Caller phone number of the calls to be retrieved (optional).
    """

    def __init__(
        self,
        duration: str,
        phone_number: str,
    ):
        self._duration = duration
        self._phone_number = phone_number

    def run(self):
        """Executes the command."""

        # TODO: read these values from configurations yaml file
        cassandra_handler = CassandraDBHandler(host='127.0.0.1', port=9042, keyspace='calldrop')
        calls_percentage = cassandra_handler.get_successful_calls(duration=self._duration, user_phone_number=self._phone_number)
        click.echo(calls_percentage)


@click.group()
def calls():
    """Used to interact with the calls command group."""


@calls.command(name="get", help="Defines get command for calls group.")
@click.option("--duration", type=click.STRING, required=True, help="Duration of the desired calls")
@click.option("--phone-number", type=click.STRING, required=False, help="User Phone Number of the desired calls")
def _get(
    duration: str,
    phone_number: str,
):
    CallsGetCommand(
        duration=duration,
        phone_number=phone_number,
    ).run()
