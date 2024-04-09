"""Handles application logic"""

from typing import List, Optional

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.position import Position
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

    def get_input(self) -> Optional[ParsedCommand]:
        """Gets user input and returns a ParsedCommand"""
        if self._get_from_stdin:
            return parse_line(input())

        if self._commands:
            command = self._commands.pop(0)
            return command
        # None return to signifies end of input
        return None


def main_controller(command_input: CommandInput, robot: Robot) -> None:
    """Main application controller"""
    while True:
        try:
            command = command_input.get_input()
            if command is None:
                break

            if command.command == Command.PLACE:
                position = Position(command.args[0], command.args[1], command.args[2])
                robot.place(position)
            elif command.command == Command.MOVE:
                robot.move()
            elif command.command == Command.LEFT:
                robot.left()
            elif command.command == Command.RIGHT:
                robot.right()
            elif command.command == Command.REPORT:
                robot.report()

        # This application needs to be robust against bad user input so we just ignore
        # bad input then continue.
        except ParsingError:
            pass
