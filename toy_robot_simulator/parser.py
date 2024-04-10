"""Input parser

The parser is designed to be robust to user input and will ignore unknown commands.
"""

from typing import Any, Dict, Optional


from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.domain.command import Command
from toy_robot_simulator.domain.position import Direction, Position


class ParsedCommand:
    """Representation of a parsed command.

    A line of command has the following format:

    `COMMAND [ARG1, ARG2, ...]`

    If the command does not have any arguments, the value `args` this field is
    None. If the command has arguments, the value of this field is a dictionary
    where the keys are the argument names and the values are the argument
    values.

    For example, consider the following `PLACE` command.

    `PLACE 0,0,NORTH`

    The corresponding `ParsedCommand` object will have the following fields:
    - command: `Command.PLACE`
    - args: `{'position': Position(0, 0, Direction.NORTH)}`

    On the other hand, consider the following `MOVE` command.

    `MOVE`

    The corresponding `ParsedCommand` object will have the following fields:
    - command: `Command.MOVE`
    - args: None
    """

    def __init__(self, command: Command, args: Optional[Dict[str, Any]] = None):
        """Instantiate a parsed command.

        Args:
            command: The parsed command.
            args: The arguments of the command.
        """
        self.command = command
        self.args = args


def parse_line(command_line: str) -> ParsedCommand:
    """Parse a line of input

    Args:
        command_line: The command line to parse.

    Returns:
        A parsed command.
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

        # This section is for commands that do not have any arguments.
        if len(unparsed_args) > 0:
            raise ParsingError("Invalid command arguments")

        return ParsedCommand(enum_command)

    except ValueError as error:
        raise ParsingError("Invalid command") from error
