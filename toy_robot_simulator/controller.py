"""Handles application logic"""

from typing import List, Optional
from toy_robot_simulator.config import MAX_LENGTH, MAX_WIDTH
from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table
from toy_robot_simulator.parser import parse_line, ParsedCommand


class CommandInput:
    """Abstraction layer for user command input."""

    def __init__(self, commands: Optional[List[ParsedCommand]] = None) -> None:
        """Create a command input object.

        Args:
            commands: Optional list of ParsedCommand objects.
        """
        self._commands = commands

    def get_input(self) -> ParsedCommand:
        """Gets user input and returns a ParsedCommand"""
        if self._commands:
            command = self._commands.pop(0)
            return command
        return parse_line(input())


def main_controller(command_input: CommandInput) -> None:
    """Main application controller"""
    table = Table(MAX_LENGTH, MAX_WIDTH)
    robot = Robot(table)
    while True:
        try:
            command = command_input.get_input()

            if command.command == Command.PLACE:
                robot.place(command.args[0], command.args[1], command.args[2])
            elif command.command == Command.MOVE:
                robot.move()
            elif command.command == Command.LEFT:
                robot.left()
            elif command.command == Command.RIGHT:
                robot.right()

        # This application needs to be robust against bad user input so we just ignore
        # bad input then continue.
        except ParsingError:
            pass
