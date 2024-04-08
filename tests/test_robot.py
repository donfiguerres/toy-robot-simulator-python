"""Tests for the toy robot"""

from toy_robot_simulator.model.position import Direction
from toy_robot_simulator.model.robot import Robot
from toy_robot_simulator.model.table import Table


def test_robot_init():
    """Test the robot initialization"""
    table = Table(5, 5)
    robot = Robot(table)
    assert robot.is_placed is False


def test_robot_move():
    """Test movement of robot"""
    table = Table(5, 5)
    robot = Robot(table)
    robot.place(0, 0, Direction.NORTH)
    robot.move()
    assert robot.x == 0
    assert robot.y == 1
    assert robot.direction == Direction.NORTH


def test_robot_rotate():
    """Test rotate motion of robot"""
    table = Table(5, 5)
    robot = Robot(table)
    robot.place(0, 0, Direction.NORTH)
    robot.left()
    assert robot.x == 0
    assert robot.y == 0
    assert robot.direction == Direction.WEST


def test_robot_combination():
    """Test combination of motion and rotation of the robot"""
    table = Table(5, 5)
    robot = Robot(table)
    robot.place(1, 2, Direction.EAST)
    robot.move()
    robot.move()
    robot.left()
    robot.move()
    assert robot.x == 3
    assert robot.y == 3
    assert robot.direction == Direction.NORTH
