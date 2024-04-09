"""Command representations"""

from enum import Enum


class Command(Enum):
    """Commands from the user"""

    PLACE = "PLACE"
    MOVE = "MOVE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    REPORT = "REPORT"
