"""Tests for handling output."""

from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.view.output import Presentation


def test_presentation_prints_to_console(capsys):
    """Validate that present prints to stdout."""
    presentation = Presentation()

    presentation.render_position(Position(1, 2, Direction.NORTH))

    captured = capsys.readouterr()
    assert captured.out == "1,2,NORTH\n"
    assert captured.err == ""
