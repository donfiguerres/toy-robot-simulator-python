"""Tests for the controller"""

import pytest

from toy_robot_simulator.controller import cli_controller
from toy_robot_simulator.domain.command import Command
from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.domain.robot import Robot
from toy_robot_simulator.domain.table import Table
from toy_robot_simulator.parser import ParsedCommand
from toy_robot_simulator.view.input import CommandInput
from toy_robot_simulator.view.output import Presentation


@pytest.mark.parametrize(
    ("commands", "expected_position", "expected_output"),
    (
        (
            [
                ParsedCommand(
                    Command.PLACE, args={"position": Position(0, 0, Direction.NORTH)}
                ),
                ParsedCommand(Command.MOVE),
                ParsedCommand(Command.REPORT),
            ],
            Position(0, 1, Direction.NORTH),
            "0,1,NORTH\n",
        ),
        (
            [
                ParsedCommand(
                    Command.PLACE, args={"position": Position(0, 0, Direction.NORTH)}
                ),
                ParsedCommand(Command.LEFT),
                ParsedCommand(Command.REPORT),
            ],
            Position(0, 0, Direction.WEST),
            "0,0,WEST\n",
        ),
        (
            [
                ParsedCommand(
                    Command.PLACE, args={"position": Position(0, 0, Direction.NORTH)}
                ),
                ParsedCommand(Command.RIGHT),
                ParsedCommand(Command.REPORT),
            ],
            Position(0, 0, Direction.EAST),
            "0,0,EAST\n",
        ),
        (
            [
                ParsedCommand(
                    Command.PLACE, args={"position": Position(1, 2, Direction.EAST)}
                ),
                ParsedCommand(Command.MOVE),
                ParsedCommand(Command.MOVE),
                ParsedCommand(Command.LEFT),
                ParsedCommand(Command.MOVE),
                ParsedCommand(Command.REPORT),
            ],
            Position(3, 3, Direction.NORTH),
            "3,3,NORTH\n",
        ),
        (
            [
                # Invalid command should be ignored
                ParsedCommand(Command.PLACE),
                ParsedCommand(
                    Command.PLACE, args={"position": Position(0, 0, Direction.NORTH)}
                ),
                ParsedCommand(Command.MOVE),
                ParsedCommand(Command.REPORT),
            ],
            Position(0, 1, Direction.NORTH),
            "0,1,NORTH\n",
        ),
    ),
)
def test_main_controller(capsys, commands, expected_position, expected_output):
    """Test the main controller.

    Validates that all commands are properly passed from input handler to robot model.
    """
    table = Table(5, 5)
    robot = Robot(table)
    presentation = Presentation()
    command_input = CommandInput(commands)

    cli_controller(command_input, presentation, robot)

    assert robot.report() == expected_position
    captured = capsys.readouterr()
    assert captured.out == expected_output
