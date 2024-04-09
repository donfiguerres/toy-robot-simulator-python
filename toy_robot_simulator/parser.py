"""Input parser

The parser is designed to be robust to user input and will ignore unknown commands.
"""

from logging import getLogger
from typing import Any, Dict, List, Optional


from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction, Position

LOG = getLogger()


class ParsedCommand:
    """Parsed command"""

    def __init__(self, command: Command, args: Optional[Dict[str, Any]] = None):
        self.command = command
        self.args = args


def parse_line(command_line: str) -> ParsedCommand:
    """Parse a line of input

    Args:
        command_line: The command line to parse

    Returns:
        A parsed command
    """
    try:
        command, *unparsed_args = command_line.split(maxsplit=1)
        command = command.upper()
        enum_command = Command(command)

        if enum_command == Command.PLACE:
            if len(unparsed_args) != 1:
                raise ParsingError("Invalid command arguments")

            args = list(map(str.strip, unparsed_args[0].split(",")))
            if len(args) != 3:
                raise ParsingError("Invalid command arguments")

            x = int(args[0])
            y = int(args[1])
            direction = Direction(args[2].upper())
            position = Position(x, y, direction)
            return ParsedCommand(enum_command, {"position": position})

        if len(unparsed_args) > 0:
            raise ParsingError("Invalid command arguments")

        return ParsedCommand(enum_command)

    except ValueError as error:
        LOG.error("Invalid command: %s", command_line)
        raise ParsingError("Invalid command") from error
