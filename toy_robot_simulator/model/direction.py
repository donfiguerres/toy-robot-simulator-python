"""Representation of directions"""

from enum import Enum


class Direction(Enum):
    """Possible directions a robot can face"""

    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


def left(current_direction: Direction) -> Direction:
    """Return the direction to the left of the given current direction.

    Args:
        current_direction: The current direction

    Returns:
        The direction to the left of the current direction
    """
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    return Direction(directions[(current_index - 1) % 4])


def right(current_direction: Direction) -> Direction:
    """Return the direction to the right of the given current direction.

     Args:
        current_direction: The current direction

    Returns:
        The direction to the right of the current direction
    """
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    return Direction(directions[(current_index + 1) % 4])
