"""Handles application logic"""

from logging import getLogger
from typing import List, Optional

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.parser import parse_line, ParsedCommand


LOG = getLogger()


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


def main_controller(command_input: CommandInput, robot: Robot) -> None:
    """Main application controller"""
    while True:
        try:
            command = command_input.get_next_command()
            if command is None:
                break

            if command.command == Command.PLACE:
                if not command.args or ("position" not in command.args):
                    raise ParsingError("Invalid command arguments")
                position = command.args["position"]
                robot.place(position)
            elif command.command == Command.MOVE:
                robot.move()
            elif command.command == Command.LEFT:
                robot.left()
            elif command.command == Command.RIGHT:
                robot.right()
            elif command.command == Command.REPORT:
                robot.report()

        # This application needs to be robust against bad user input so we just
        # continue parsing the next command after a bad input
        except ParsingError as error:
            LOG.error(error)
        except KeyboardInterrupt:
            print("Exiting...")
            break
