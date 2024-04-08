"""Application entry point"""

from toy_robot_simulator.config import MAX_LENGTH, MAX_WIDTH
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table
from toy_robot_simulator.controller import CommandInput, main_controller


def main():
    """Application main function."""
    command_input = CommandInput()
    table = Table(MAX_LENGTH, MAX_WIDTH)
    robot = Robot(table)

    main_controller(command_input, robot)
