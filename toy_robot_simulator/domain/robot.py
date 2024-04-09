"""Representation of a Toy Robot"""

from toy_robot_simulator.domain.position import (
    calculate_new_position_after_move,
    Direction,
    Position,
    rotate_left,
    rotate_right,
)
from toy_robot_simulator.domain.table import Table


class Robot:
    """Class representing a Toy Robot"""

    def __init__(self, table: Table):
        self.is_placed = False
        self.position = Position(0, 0, Direction.NORTH)
        self.map = table

    def place(self, position: Position) -> None:
        """Place the robot on the table"""
        if self.map.is_valid_position(position.x, position.y):
            self.position = position
            self.is_placed = True

    def move(self) -> None:
        """Move the robot one unit forward in its current direction."""
        if self.is_placed:
            new_position = calculate_new_position_after_move(self.position)
            if self.map.is_valid_position(new_position.x, new_position.y):
                self.position = new_position

    def left(self) -> None:
        """Rotate the robot 90 degrees to the left."""
        if self.is_placed:
            self.position = rotate_left(self.position)

    def right(self) -> None:
        """Rotate the robot 90 degrees to the right."""
        if self.is_placed:
            self.position = rotate_right(self.position)

    def report(self) -> str:
        """Return the current position of the robot as string."""
        if self.is_placed:
            return (
                f"{self.position.x},{self.position.y},{self.position.direction.value}"
            )
        return ""
