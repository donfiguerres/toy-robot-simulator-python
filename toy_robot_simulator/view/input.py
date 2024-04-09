"""Handles user input"""

from typing import List, Optional

from toy_robot_simulator.parser import parse_line, ParsedCommand


class CommandInput:
    """Abstraction layer for user command input."""

    def __init__(self, commands: Optional[List[ParsedCommand]] = None) -> None:
        """Create a command input object.

        Args:
            commands: Optional list of ParsedCommand objects.
        """
        self._commands = commands
        self._get_from_stdin = not commands

    def get_next_command(self) -> Optional[ParsedCommand]:
        """Gets user input and returns a ParsedCommand.

        None return signifies end of input.

        Returns:
            ParsedCommand object or None
        """
        if self._get_from_stdin:
            return parse_line(input())

        if self._commands:
            command = self._commands.pop(0)
            return command

        return None
