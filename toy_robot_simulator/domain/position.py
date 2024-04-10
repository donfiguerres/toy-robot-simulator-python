"""Domain model representation of positions and movements"""

from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    """Possible directions a robot can face"""

    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"


@dataclass(frozen=True)
class Position:
    """Domain model representation of a robot's position"""

    x: int
    y: int
    direction: Direction


def rotate_left(position: Position) -> Position:
    """Return the direction to the left of the given current direction.

    Args:
        position: current position

    Returns:
        new position after rotating to the left
    """
    current_direction = position.direction
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    new_direction = Direction(directions[(current_index - 1) % 4])
    return Position(position.x, position.y, new_direction)


def rotate_right(position: Position) -> Position:
    """Return the direction to the right of the given current direction.

     Args:
        position: current position

    Returns:
        new position after rotating to the right
    """
    current_direction = position.direction
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]
    current_index = directions.index(current_direction.value)
    new_direction = Direction(directions[(current_index + 1) % 4])
    return Position(position.x, position.y, new_direction)


def calculate_new_position_after_move(position: Position) -> Position:
    """Calculate the next position the robot if it moves."""
    x = position.x
    y = position.y

    if position.direction == Direction.NORTH:
        y += 1
    elif position.direction == Direction.SOUTH:
        y -= 1
    elif position.direction == Direction.EAST:
        x += 1
    elif position.direction == Direction.WEST:
        x -= 1

    return Position(x, y, position.direction)
