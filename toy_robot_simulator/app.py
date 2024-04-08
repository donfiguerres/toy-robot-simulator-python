"""Application entry point"""

from toy_robot_simulator.controller import main_controller


def main():
    """Application main function.

    This acts as the applications controller component which bridges the models with
    user input and output
    """
    print("Initializing toy robot simulator")
    main_controller()
