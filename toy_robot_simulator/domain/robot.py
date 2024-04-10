"""Representation of a Toy Robot"""

from typing import Optional
from toy_robot_simulator.domain.position import (
    calculate_new_position_after_move,
    Position,
    rotate_left,
    rotate_right,
)
from toy_robot_simulator.domain.table import Table


class Robot:
    """Representation of a Toy Robot.

    The toy robot keeps track of its current position and whether it is placed
    on the table.  It can be placed on the table, moved, rotated and report its
    current position.
    """

    def __init__(self, table: Table):
        """Instantiate a toy robot.

        Args:
            table: The table where the robot will be placed on.
        """
        self.position: Optional[Position] = None
        self.map = table

    def place(self, position: Position) -> None:
        """Place the robot on the table"""
        if self.map.is_valid_position(position.x, position.y):
            self.position = position

    def move(self) -> None:
        """Move the robot one unit forward in its current direction."""
        if self.position:
            new_position = calculate_new_position_after_move(self.position)
            if self.map.is_valid_position(new_position.x, new_position.y):
                self.position = new_position

    def left(self) -> None:
        """Rotate the robot 90 degrees to the left."""
        if self.position:
            self.position = rotate_left(self.position)

    def right(self) -> None:
        """Rotate the robot 90 degrees to the right."""
        if self.position:
            self.position = rotate_right(self.position)

    def report(self) -> Optional[Position]:
        """Return the current position of the robot.

        If the robot has not been placed yet then the position is None.
        """
        return self.position
