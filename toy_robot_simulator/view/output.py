"""Handles output to be presented to the user"""

from toy_robot_simulator.domain.position import Position


class Presentation:
    """Abstraction layer for output to be presented to the user."""

    def render_position(self, position: Position):
        """Present given position to the user.

        Args:
            position: The position to be presented to the user.
        """
        position_str = f"{position.x},{position.y},{position.direction.value}"
        print(position_str)
