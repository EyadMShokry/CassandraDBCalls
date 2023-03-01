import pytest
from cli.__main__ import cli
from cli import cli_command

from .test_base_cli import TestCLI


@pytest.mark.cli
@pytest.mark.baselines
@pytest.mark.usefixtures("cli_runner", "calls_get_args")
class TestCassandraCLI(TestCLI):

    def test_calls_group_exists(self):
        assert cli.commands.get("calls") is not None

    def test_calls_get_command_exists(self):
        assert "get" in cli_command.calls.commands

    def test_calls_get_command_works(self, cli_runner, calls_get_args):
        result = cli_runner.invoke(cli_command.calls.commands.get("get"), args=calls_get_args)
        assert result.exit_code == 0

    def test_calls_get_command_without_phone_number(self, cli_runner, calls_get_args_without_phone_number):
        result = cli_runner.invoke(cli_command.calls.commands.get("get"), args=calls_get_args_without_phone_number)
        assert result.exit_code == 0

    def test_calls_get_command_without_required_duration(self, cli_runner, calls_get_args_without_duration):
        result = cli_runner.invoke(cli_command.calls.commands.get("get"), args=calls_get_args_without_duration)
        assert result.exit_code == 2
        assert "Error: Missing option '--duration'." in result.output

