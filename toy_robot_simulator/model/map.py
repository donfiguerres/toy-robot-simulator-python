"""Model definitions for where a toy robot can move around"""


class Map:
    """Representation of an environment where a toy robot can move."""

    def __init__(self, width: int, height: int):
        """Create a new map with the given dimensions."""
        self.width = width
        self.height = height
