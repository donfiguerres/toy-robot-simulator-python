"""Tests for the directions."""

import pytest

from toy_robot_simulator.domain.position import (
    calculate_new_position_after_move,
    Direction,
    Position,
    rotate_left,
    rotate_right,
)


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
    position = Position(1, 1, direction)
    new_position = rotate_left(position)
    assert new_position.x == 1
    assert new_position.y == 1
    assert new_position.direction == expected


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
    position = Position(1, 1, direction)
    new_position = rotate_right(position)
    assert new_position.x == 1
    assert new_position.y == 1
    assert new_position.direction == expected


@pytest.mark.parametrize(
    ("old_position", "expected_position"),
    (
        (Position(0, 0, Direction.NORTH), Position(0, 1, Direction.NORTH)),
        (Position(1, 0, Direction.NORTH), Position(1, 1, Direction.NORTH)),
        (Position(0, 1, Direction.SOUTH), Position(0, 0, Direction.SOUTH)),
        (Position(1, 0, Direction.EAST), Position(2, 0, Direction.EAST)),
        (Position(0, 1, Direction.WEST), Position(-1, 1, Direction.WEST)),
        (Position(0, 0, Direction.WEST), Position(-1, 0, Direction.WEST)),
        (Position(0, 0, Direction.SOUTH), Position(0, -1, Direction.SOUTH)),
    ),
)
def test_calculate_new_position_after_move(old_position, expected_position):
    """Test calculation of new position after a move."""
    new_position = calculate_new_position_after_move(old_position)
    assert new_position == expected_position
