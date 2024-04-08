"""Tests for the directions."""

import pytest

from toy_robot_simulator.model.direction import Direction, left, right


@pytest.mark.parametrize(
    ("direction", "expected"),
    (
        (Direction.NORTH, Direction.WEST),
        (Direction.WEST, Direction.SOUTH),
        (Direction.SOUTH, Direction.EAST),
        (Direction.EAST, Direction.NORTH),
    ),
)
def test_left(direction, expected):
    """Test the left direction."""
    assert left(direction) == expected


@pytest.mark.parametrize(
    ("direction", "expected"),
    (
        (Direction.NORTH, Direction.EAST),
        (Direction.EAST, Direction.SOUTH),
        (Direction.SOUTH, Direction.WEST),
        (Direction.WEST, Direction.NORTH),
    ),
)
def test_right(direction, expected):
    """Test the right direction."""
    assert right(direction) == expected
