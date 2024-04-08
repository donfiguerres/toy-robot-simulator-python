"""Domain model representation of positions and movements"""

from enum import Enum
from typing import Tuple


class Direction(Enum):
    """Possible directions a robot can face"""

    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


def rotate_left(current_direction: Direction) -> Direction:
    """Return the direction to the left of the given current direction.

    Args:
        current_direction: The current direction

    Returns:
        The direction to the left of the current direction
    """
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    return Direction(directions[(current_index - 1) % 4])


def rotate_right(current_direction: Direction) -> Direction:
    """Return the direction to the right of the given current direction.

     Args:
        current_direction: The current direction

    Returns:
        The direction to the right of the current direction
    """
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    return Direction(directions[(current_index + 1) % 4])


def calculate_new_position(x: int, y: int, direction: Direction) -> Tuple[int, int]:
    """Calculate the next position the robot if it moves."""
    x = x
    y = y

    if direction == Direction.NORTH:
        y += 1
    elif direction == Direction.SOUTH:
        y -= 1
    elif direction == Direction.EAST:
        x += 1
    elif direction == Direction.WEST:
        x -= 1

    return x, y
