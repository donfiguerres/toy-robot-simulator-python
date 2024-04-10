"""Tests for the map"""

import pytest

from toy_robot_simulator.domain.table import Table


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
def test_is_valid_position(x, y, expected):
    """Test valid positions in a table"""
    table = Table(5, 5)
    assert table.is_valid_position(x, y) == expected
