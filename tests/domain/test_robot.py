"""Tests for the toy robot"""

from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.domain.robot import Robot
from toy_robot_simulator.domain.table import Table


def test_robot_init():
    """Test the robot initialization"""
    table = Table(5, 5)
    robot = Robot(table)
    assert robot.is_placed is False


def test_robot_move(capsys):
    """Test movement of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.move()
    robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 1
    assert robot.position.direction == Direction.NORTH
    captured = capsys.readouterr()
    assert captured.out == "0,1,NORTH\n"


def test_robot_rotate_left(capsys):
    """Test rotate left rotate motion of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.left()
    robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 0
    assert robot.position.direction == Direction.WEST
    captured = capsys.readouterr()
    assert captured.out == "0,0,WEST\n"


def test_robot_rotate_right(capsys):
    """Test rotate right rotate motion of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.right()
    robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 0
    assert robot.position.direction == Direction.EAST
    captured = capsys.readouterr()
    assert captured.out == "0,0,EAST\n"


def test_robot_combination(capsys):
    """Test combination of motion and rotation of the robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(1, 2, Direction.EAST))
    robot.move()
    robot.move()
    robot.left()
    robot.move()
    robot.report()

    assert robot.position.x == 3
    assert robot.position.y == 3
    assert robot.position.direction == Direction.NORTH
    captured = capsys.readouterr()
    assert captured.out == "3,3,NORTH\n"


def test_ignore_instructions_before_place(capsys):
    """Validate that commands given before the place command are ignored"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.move()
    robot.move()
    robot.right()
    robot.place(Position(1, 2, Direction.EAST))
    robot.move()
    robot.move()
    robot.left()
    robot.move()
    robot.report()

    assert robot.position.x == 3
    assert robot.position.y == 3
    assert robot.position.direction == Direction.NORTH
    captured = capsys.readouterr()
    assert captured.out == "3,3,NORTH\n"


def test_ignore_invalid_placement():
    """Validate that invalid placement is ignored."""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(6, 6, Direction.EAST))
    assert robot.is_placed is False
