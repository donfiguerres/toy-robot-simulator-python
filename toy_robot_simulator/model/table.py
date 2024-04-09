"""Model definitions for where a toy robot can move around"""


class Table:
    """Representation of an environment where a toy robot can move."""

    def __init__(self, width: int, length: int):
        """Create a new map with the given dimensions.

        Args:
            width: width of the map - x-axis (EAST to WEST)
            length: length of the map - y-axis (NORTH to SOUTH)
        """
        self.width = width
        self.length = length

    def is_valid_position(self, x: int, y: int):
        """Check if the given position is valid for the map.

        Args:
            x: The x coordinate
            y: The y coordinate

        Returns:
            True if the position is valid, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.length
