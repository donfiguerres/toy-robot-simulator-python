import pytest

from toy_robot_simulator.controller import CommandInput, main_controller
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction, Position
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table
from toy_robot_simulator.parser import ParsedCommand


def test_command_input(mocker):
    mocker.patch("builtins.input", return_value="PLACE 0,0,NORTH")
    command_input = CommandInput()

    place_command = command_input.get_next_command()
    assert place_command.command == Command.PLACE
    position = place_command.args["position"]
    assert position.x == 0
    assert position.y == 0
    assert position.direction == Direction.NORTH


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
    command_input = CommandInput(commands)

    main_controller(command_input, robot)

    position = robot.position
    assert position.x == expected_position.x
    assert position.y == expected_position.y
    assert position.direction == expected_position.direction
    captured = capsys.readouterr()
    assert captured.out == expected_output
