"""Tests for the parser module"""

import pytest

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
        ("MOVE", ParsedCommand(Command.MOVE)),
        ("LEFT", ParsedCommand(Command.LEFT)),
        ("RIGHT", ParsedCommand(Command.RIGHT)),
        ("REPORT", ParsedCommand(Command.REPORT)),
        ("     REPORT   ", ParsedCommand(Command.REPORT)),
    ),
)
def test_parse_line(line, expected):
    """Test the parse_line function"""
    parsed_command = parse_line(line)
    assert parsed_command.command == expected.command
    assert parsed_command.args == expected.args
