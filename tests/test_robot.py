"""Tests for the toy robot"""

from toy_robot_simulator.model.position import Direction, Position
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table


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


def test_robot_rotate(capsys):
    """Test rotate motion of robot"""
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
