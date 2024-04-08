"""Application entry point"""

from toy_robot_simulator.controller import CommandInput, main_controller


def main():
    """Application main function."""
    main_controller(CommandInput())
