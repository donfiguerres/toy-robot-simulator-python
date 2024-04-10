"""Tests for the toy robot"""

from toy_robot_simulator.domain.position import Direction, Position
from toy_robot_simulator.domain.robot import Robot
from toy_robot_simulator.domain.table import Table


def test_robot_init():
    """Test the robot initialization"""
    table = Table(5, 5)
    robot = Robot(table)
    assert robot.is_placed is False


def test_robot_move():
    """Test movement of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.move()
    report = robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 1
    assert robot.position.direction == Direction.NORTH
    assert report == "0,1,NORTH"


def test_robot_rotate_left():
    """Test rotate left rotate motion of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.left()
    report = robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 0
    assert robot.position.direction == Direction.WEST
    assert report == "0,0,WEST"


def test_robot_rotate_right():
    """Test rotate right rotate motion of robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(0, 0, Direction.NORTH))
    robot.right()
    report = robot.report()

    assert robot.position.x == 0
    assert robot.position.y == 0
    assert robot.position.direction == Direction.EAST
    assert report == "0,0,EAST"


def test_robot_combination():
    """Test combination of motion and rotation of the robot"""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(1, 2, Direction.EAST))
    robot.move()
    robot.move()
    robot.left()
    robot.move()
    report = robot.report()

    assert robot.position.x == 3
    assert robot.position.y == 3
    assert robot.position.direction == Direction.NORTH
    assert report == "3,3,NORTH"


def test_ignore_instructions_before_place():
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
    report = robot.report()

    assert robot.position.x == 3
    assert robot.position.y == 3
    assert robot.position.direction == Direction.NORTH
    assert report == "3,3,NORTH"


def test_ignore_invalid_placement():
    """Validate that invalid placement is ignored."""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(5, 5, Direction.EAST))

    assert robot.is_placed is False


def test_ignore_invalid_move():
    """Validate that invalid move is ignored."""
    table = Table(5, 5)
    robot = Robot(table)

    robot.place(Position(4, 4, Direction.EAST))
    robot.move()

    assert robot.is_placed is True
    assert robot.position.x == 4
    assert robot.position.y == 4
    assert robot.position.direction == Direction.EAST


def test_no_report_if_not_placed():
    """Validate that the report command is ignored if the robot is not placed."""
    table = Table(5, 5)
    robot = Robot(table)

    report = robot.report()

    assert robot.is_placed is False
    assert report == ""
