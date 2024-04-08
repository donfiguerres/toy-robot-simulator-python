"""Model definitions for where a toy robot can move around"""


class Table:
    """Representation of an environment where a toy robot can move."""

    def __init__(self, width: int, height: int):
        """Create a new map with the given dimensions.

        Args:
            width: The width of the map (EAST to WEST)
            height: The height of the map (NORTH to SOUTH)
        """
        self.width = width
        self.height = height

    def is_valid_position(self, x: int, y: int):
        """Check if the given position is valid for the map.

        Args:
            x: The x coordinate
            y: The y coordinate

        Returns:
            True if the position is valid, False otherwise
        """
        return 0 <= x < self.width and 0 <= y < self.height
