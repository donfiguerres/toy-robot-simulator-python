"""Tests for the map"""

import pytest

from toy_robot_simulator.model.map import Map


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, True),
        (1, 2, True),
        (2, 3, True),
        (4, 4, True),
        (5, 5, False),
        (-1, 4, False),
        (4, -1, False),
    ),
)
def test_map(x, y, expected):
    map = Map(5, 5)
    assert map.is_valid_position(x, y) == expected
