"""Tests for the parser module"""

import pytest

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.direction import Direction
from toy_robot_simulator.parser import parse_line, ParsedCommand


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        (
            "PLACE 1,2,NORTH",
            ParsedCommand(Command.PLACE, [1, 2, Direction.NORTH]),
        ),
        (
            "PLACE 1, 2, NORTH",
            ParsedCommand(Command.PLACE, [1, 2, Direction.NORTH]),
        ),
        (
            "PLACE 1, 2, NORTH",
            ParsedCommand(Command.PLACE, [1, 2, Direction.NORTH]),
        ),
        (
            "     PLACE 1, 2, NORTH    ",
            ParsedCommand(Command.PLACE, [1, 2, Direction.NORTH]),
        ),
        (
            "place 1, 2, north",
            ParsedCommand(Command.PLACE, [1, 2, Direction.NORTH]),
        ),
        ("MOVE", ParsedCommand(Command.MOVE)),
        ("move", ParsedCommand(Command.MOVE)),
        ("LEFT", ParsedCommand(Command.LEFT)),
        ("left", ParsedCommand(Command.LEFT)),
        ("RIGHT", ParsedCommand(Command.RIGHT)),
        ("right", ParsedCommand(Command.RIGHT)),
        ("REPORT", ParsedCommand(Command.REPORT)),
        ("     REPORT   ", ParsedCommand(Command.REPORT)),
        ("     report   ", ParsedCommand(Command.REPORT)),
    ),
)
def test_parse_line(line, expected):
    """Test the parse_line function"""
    parsed_command = parse_line(line)
    assert parsed_command.command == expected.command
    assert parsed_command.args == expected.args


@pytest.mark.parametrize(
    ("input"),
    (
        "INVALID",
        "    INVALID   ",
        "PLACE 1+2,NORTH",
        "MOVE 1,2,NORTH",
        "LEFT 1,2,NORTH",
        "REPORT LEFT",
    ),
)
def test_parse_line_invalid(input):
    """Test the parse_line function with an invalid command"""
    with pytest.raises(ParsingError):
        parse_line(input)
