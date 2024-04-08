
import pytest

from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction
from toy_robot_simulator.parser import ParsedCommand

@pytest.mark.parametrize(
    ("commands", "expected_position"),
    (
        (
            (
                ParsedCommand(Command.PLACE, args=(0, 0, Direction.NORTH)),
                ParsedCommand(Command.MOVE),
            ),
            (0, 1, Direction.NORTH),
        ),
    )
)
def test_robot_movements(commands, expected_position):
    """Test the robot movements"""
    table = Table(5, 5)
    robot = Robot(table)
    for command in commands:
        robot.(command)
    assert robot.position == expected_position
