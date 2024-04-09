"""Tests for the parser module"""

import pytest

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction, Position
from toy_robot_simulator.parser import parse_line, ParsedCommand


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
        ("MOVE", Command.MOVE),
        ("move", Command.MOVE),
        ("LEFT", Command.LEFT),
        ("left", Command.LEFT),
        ("RIGHT", Command.RIGHT),
        ("right", Command.RIGHT),
        ("REPORT", Command.REPORT),
        ("     REPORT   ", Command.REPORT),
        ("     report   ", Command.REPORT),
    ),
)
def test_parse_line(line, expected_command, expected_args):
    """Test the parse_line function"""
    parsed_command = parse_line(line)
    assert parsed_command.command == expected_command
    assert parsed_command.args == expected_args


@pytest.mark.parametrize(
    ("command_line"),
    (
        "INVALID",
        "    INVALID   ",
        "PLACE 1+2,NORTH",
        "MOVE 1,2,NORTH",
        "LEFT 1,2,NORTH",
        "REPORT LEFT",
    ),
)
def test_parse_line_invalid(command_line):
    """Test the parse_line function with an invalid command"""
    with pytest.raises(ParsingError):
        parse_line(command_line)
