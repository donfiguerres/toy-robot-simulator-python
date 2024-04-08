import pytest

from toy_robot_simulator.controller import CommandInput, main_controller
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction, Position
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table
from toy_robot_simulator.parser import ParsedCommand


@pytest.mark.parametrize(
    ("commands", "expected_position"),
    (
        (
            [
                ParsedCommand(Command.PLACE, args=(0, 0, Direction.NORTH)),
                ParsedCommand(Command.MOVE),
            ],
            Position(0, 1, Direction.NORTH),
        ),
    ),
)
def test_robot_movements(commands, expected_position):
    """Test the robot movements"""
    table = Table(5, 5)
    robot = Robot(table)
    command_input = CommandInput(commands)
    main_controller(command_input, robot)

    position = robot.position
    assert position.x == expected_position.x
    assert position.y == expected_position.y
    assert position.direction == expected_position.direction
