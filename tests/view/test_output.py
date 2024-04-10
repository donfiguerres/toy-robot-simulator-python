"""Tests for handling output."""

from toy_robot_simulator.view.output import Presentation


def test_presentation_prints_to_console(capsys):
    """Validate that present prints to stdout."""
    presentation = Presentation()

    presentation.present("Hello World")

    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
    assert captured.err == ""
