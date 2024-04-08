"""Representation of a Toy Robot"""

from toy_robot_simulator.model.position import (
    calculate_new_position,
    Direction,
    rotate_left,
    rotate_right,
)
from toy_robot_simulator.model.map import Map


class Robot:
    """Class representing a Toy Robot"""

    def __init__(self, map: Map):
        self.is_placed = False
        self.x = 0
        self.y = 0
        self.direction = Direction.NORTH
        self.map = map

    def place(self, x: int, y: int, direction: Direction) -> None:
        """Place the robot on the table"""
        self.x = x
        self.y = y
        self.direction = direction

    def move(self) -> None:
        """Move the robot one unit forward in its current direction."""
        if self.is_placed:
            x, y = calculate_new_position(self.x, self.y, self.direction)
            if self.map.is_valid_position(x, y):
                self.x = x
                self.y = y

    def left(self) -> None:
        """Rotate the robot 90 degrees to the left."""
        if self.is_placed:
            self.direction = rotate_left(self.direction)

    def right(self) -> None:
        """Rotate the robot 90 degrees to the right."""
        if self.is_placed:
            self.direction = rotate_right(self.direction)
