"""Application entry point"""

from toy_robot_simulator.config import TABLE_WIDTH, TABLE_LENGTH
from toy_robot_simulator.domain.robot import Robot
from toy_robot_simulator.domain.table import Table
from toy_robot_simulator.controller import CommandInput, cli_controller
from toy_robot_simulator.view.output import Presentation


def main():
    """Application main function."""
    command_input = CommandInput()
    presentation = Presentation()
    table = Table(TABLE_WIDTH, TABLE_LENGTH)
    robot = Robot(table)

    cli_controller(
        command_input,
        presentation,
        robot,
    )
