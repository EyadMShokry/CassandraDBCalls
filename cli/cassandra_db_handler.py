import math
from typing import Optional, List

from cassandra.cluster import Cluster


class CassandraDBHandler:

    def __init__(self, host, port, keyspace):
        self._current_session = None
        self._host = host
        self._port = port
        self._keyspace = keyspace

        self.open_cassandra_connection()

    def open_cassandra_connection(self):
        """Opens connection with Cassandra Database with the giver host and port and creates a session to be used
        for queries execution."""
        cluster = Cluster([self._host], port=self._port)

        current_session = cluster.connect()

        current_session.set_keyspace(self._keyspace)

        self._current_session = current_session

    def calculate_succesfull_calls(self, calls_rows: List) -> int:
        """Returns percentage of the successful calls found in the given calls_rows argument.

        Args:
            calls_rows (List): The calls rows which are found and retrieved from Cassandra database.

        Returns:
            int: Percentage of the successful calls.
        """

        if not calls_rows:
            return 0
        successfully_completed_calls_count = sum([row.call_successfully_completed for row in calls_rows])

        percentage = math.ceil(successfully_completed_calls_count / len(calls_rows) * 100)
        return percentage

    def get_successful_calls(self, duration: str, user_phone_number: Optional[str] = None) -> str:
        """Retrieves calls records from Cassandra database and calculates the successful ones.

        Args:
            duration (str): The duration of calls those should be retrieved from the database.
            user_phone_number: The caller phone number of calls those should be retrieved from the database.

        Returns:
            str: Percentage of the successful calls.
        """

        query = f"SELECT call_successfully_completed FROM userdata WHERE duration = '{duration}'"

        if user_phone_number is not None:
            query += f" AND user_phone_number = '{user_phone_number}'"

        query += ' ALLOW FILTERING;'

        calls_rows = self._current_session.execute(query=query)
        successful_calls_percentage = self.calculate_succesfull_calls(calls_rows=list(calls_rows))

        return f"{successful_calls_percentage}%"
