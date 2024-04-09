"""Application entry point"""

from toy_robot_simulator.config import TABLE_WIDTH, TABLE_LENGTH
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table
from toy_robot_simulator.controller import CommandInput, main_controller


def main():
    """Application main function."""
    command_input = CommandInput()
    table = Table(TABLE_WIDTH, TABLE_LENGTH)
    robot = Robot(table)

    main_controller(command_input, robot)
