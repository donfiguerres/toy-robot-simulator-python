"""Handles application logic"""

from logging import getLogger

from toy_robot_simulator.exception import ParsingError
from toy_robot_simulator.domain.command import Command
from toy_robot_simulator.domain.robot import Robot
from toy_robot_simulator.view.input import CommandInput
from toy_robot_simulator.view.output import Presentation


LOG = getLogger()


def cli_controller(
    command_input: CommandInput, presentation: Presentation, robot: Robot
) -> None:
    """CLI application controller

    Args:
        command_input: Command input instance
        presentation: Presentation instance
        robot: Robot instance
    """
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
                if position := robot.report():
                    presentation.render_position(position)

        # This application needs to be robust against bad user input so we just
        # continue parsing the next command after a bad input
        except ParsingError as error:
            LOG.error(error)
        except KeyboardInterrupt:
            print("Exiting...")
            break
