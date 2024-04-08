"""Handles application logic"""

from toy_robot_simulator.model.command import Command
from toy_robot_simulator.model.position import Direction
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.parser import parse_line, ParsedCommand


class CommandInput:
    """Abstraction layer for user command input."""

    def get_input(self) -> ParsedCommand:
        """Gets user input and returns a ParsedCommand"""
        return parse_line(input())


def main_controller() -> None:
    """Main application controller"""
    command_input = CommandInput()
    robot = Robot()
    while True:
        command = command_input.get_input()

        if command.command == Command.PLACE:
            robot.place(command.args[0], command.args[1], command.args[2])

        if command.command == "exit":
            break
        if command.command == "place":
            print("Place command")
        if command.command == "move":
            print("Move command")
        if command.command == "left":
            print("Left command")
        if command.command == "right":
            print("Right command")
        if command.command == "report":
            print("Report command")
