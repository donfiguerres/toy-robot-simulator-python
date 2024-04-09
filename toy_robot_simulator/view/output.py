"""Handles output to be presented to the user"""


class Presentation:
    """Abstraction layer for output to be presented to the user."""

    def present(self, output: str):
        """Present given string to the user."""
        print(output)
