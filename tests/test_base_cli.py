import os

import pytest
from click.testing import CliRunner


class TestCLI:
    @classmethod
    def setup_class(cls):
        # Setup code that runs once before all tests in this class
        pass

    @classmethod
    def teardown_class(cls):
        # Teardown code that runs once after all tests in this class
        pass

    def setup_method(self):
        # Setup code that runs before each test method
        pass

    def teardown_method(self):
        # Teardown code that runs after each test method
        pass

    @pytest.fixture
    def calls_get_args(self):
        return [
            "--duration",
            "00:00:04",
            "--phone-number",
            "(739) 476-8397"
        ]

    @pytest.fixture
    def calls_get_args_without_duration(self):
        return [
            "--phone-number",
            "(739) 476-8397"
        ]

    @pytest.fixture
    def calls_get_args_without_phone_number(self):
        return [
            "--duration",
            "00:00:04"
        ]

    @pytest.fixture
    def cli_runner(self):
        return CliRunner()
