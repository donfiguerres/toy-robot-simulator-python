"""Representation of directions"""

from enum import Enum


class Direction(Enum):
    """Possible directions a robot can face"""

    NORTH = "NORTH"
    EAST = "EAST"
    SOUTH = "SOUTH"
    WEST = "WEST"
