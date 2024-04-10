"""Tests for the parser module"""

import pytest

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.domain.command import Command
from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.parser import parse_line


@pytest.mark.parametrize(
    ("line", "expected_command", "expected_args"),
    (
        (
            "PLACE 1,2,NORTH",
            Command.PLACE,
            {"position": Position(1, 2, Direction.NORTH)},
        ),
        (
            "PLACE 1, 2, NORTH",
            Command.PLACE,
            {"position": Position(1, 2, Direction.NORTH)},
        ),
        (
            "PLACE 1, 2, NORTH",
            Command.PLACE,
            {"position": Position(1, 2, Direction.NORTH)},
        ),
        (
            "     PLACE 1, 2, NORTH    ",
            Command.PLACE,
            {"position": Position(1, 2, Direction.NORTH)},
        ),
        (
            "place 1, 2, north",
            Command.PLACE,
            {"position": Position(1, 2, Direction.NORTH)},
        ),
        ("MOVE", Command.MOVE, None),
        ("move", Command.MOVE, None),
        ("LEFT", Command.LEFT, None),
        ("left", Command.LEFT, None),
        ("RIGHT", Command.RIGHT, None),
        ("right", Command.RIGHT, None),
        ("REPORT", Command.REPORT, None),
        ("     REPORT   ", Command.REPORT, None),
        ("     report   ", Command.REPORT, None),
    ),
)
def test_parse_line(line, expected_command, expected_args):
    """Test the parse_line function"""
    parsed_command = parse_line(line)
    assert parsed_command.command == expected_command
    if expected_args is None:
        assert parsed_command.args is None
    else:
        parsed_position = parsed_command.args["position"]
        expected_position = expected_args["position"]
        assert expected_position == parsed_position


@pytest.mark.parametrize(
    ("command_line"),
    (
        "INVALID",
        "    INVALID   ",
        "PLACE 1+2,NORTH",
        "PLACE ",
        "MOVE 1,2,NORTH",
        "LEFT 1,2,NORTH",
        "REPORT LEFT",
    ),
)
def test_parse_line_invalid(command_line):
    """Test the parse_line function with an invalid command"""
    with pytest.raises(ParsingError):
        parse_line(command_line)
