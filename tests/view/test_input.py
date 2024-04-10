"""Tests for handling user input."""

from toy_robot_simulator.domain.command import Command
from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.view.input import CommandInput


def test_command_input(mocker):
    """Test reading from input()"""
    mocker.patch("builtins.input", return_value="PLACE 0,0,NORTH")
    command_input = CommandInput()

    place_command = command_input.get_next_command()
    assert place_command.command == Command.PLACE
    position = place_command.args["position"]
    assert position == Position(0, 0, Direction.NORTH)
