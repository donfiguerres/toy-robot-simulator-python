# Toy Robot Simulator

![actions workflow](https://github.com/donfiguerres/toy-robot-simulator-python/actions/workflows/test.yml/badge.svg)

This is a simulation of a robot toy moving on a square table top with a size of 5 units
x 5 units. It reads the instructions from the standard input and will perform the
necessary actions based on the input.

For example:

```bash
PLACE X,Y,F
MOVE
LEFT
RIGHT
REPORT
```

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST
or WEST. The origin (0,0) can be considered to be the SOUTH WEST most corner.

MOVE will move the toy robot one unit forward in the direction it is currently facing.

LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without
changing the position of the robot.

REPORT will announce the X,Y and F of the robot to the standard output.

## Constraints

1. It is required that the first command to the robot is a PLACE command, after that,
any sequence of commands may be issued, in any order, including another PLACE command.
The application should discard all commands in the sequence until a valid PLACE command
has been executed.

2. The toy robot must not fall off the table during movement. This also includes the
initial placement of the toy robot. Any move that would cause the robot to fall must be
ignored.

## Design Considerations

### Design Philosophy

Domain Driven Design (DDD) is used to model the problem domain. It is ensured that the
implemented models closely resemble the entities mentioned in the requirements. See
the Domain Entities section for more details about the domain entities.

### Domain Entities

- Robot: The robot toy itself. It performs the received commands.
- Table: The environment where the robot is placed and performs the commands.
- Position: The current position of the robot in the Table.
- Commands: The commands given by the user.

### Architecture

The Model-View-Controller (MVC) Framework is the architecture followed in this project.
This is a tried and tested architecture that provides better maintainability of a
software project due to separation of concerns.

- The model component, not to be confused with ORM models, refers to the domain entities
being modeled in the application - already discussed in the previous section.
- The view component, refers to how the application is presented to the user. There
isn't much here as stdin (or file) and stdout are the only user interface as per
requirements.
- The controller component contains the the interconnection between the model and view
components.

### Project Structure

The project structure mirrors the components in the MVC framework. However, it was
decided to use `domain` for the directory containing domain models instead of `model`
so that the terminology is closer to the Domain Driven Design philosophy and also to
avoid being associated with ORM models.

## Development Considerations

### Behavior Driven Development (BDD)

The listed expected behavior of the application from the requirements are taken and
converted into test cases. These test cases are used as acceptance criteria.

> **_NOTE:_** Although, BDD is mentioned here, a BDD testing framework is not used in
the project. Pytest is the only test framework used for simplicity.

### Unit Testing

Pytest is chosen testing framework for its ease of use.

### Continuous Integration

GitHub Actions is Continuous Integration (CI) tooling chosen as it is freely available
on GitHub. Using a CI tooling in this project will ensure that all the code pushed into
the repository is properly tested and all breakages are promptly reported and visible in
the project's README page.

## Prerequisites

### Python

This project requires Python 3.11.

> **_TIP:_** You can use `pyenv` to install several Python versions in your working
environment. See [pyenv](https://github.com/pyenv/pyenv) to learn more.

### Poetry

You can install poetry using the official installer by running the following command.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

You may also follow the instructions in
[https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation).

## Setting Up the Application

Once you have cloned the project into your working environment, go to the project
directory and run the following commands.

```bash
poetry install
```

## Running the Command Line Application

After setting up your virtual environment, the executable should be available in your
`PATH`. You can run the application through the poetry virtual environment.

Run it with the `poetry` command.

```bash
poetry run toy-robot-simulator
```

Or by entering the `poetry` `shell` first then calling the executable

```bash
poetry shell
toy-robot-simulator
```

The application will wait for commands via the standard input. Type your command
in the terminal then press enter.

### Examples

#### Example 1

```bash
PLACE 0,0,NORTH
MOVE
REPORT
```

stdout:

```bash
0,1,NORTH
```

#### Example 2

```bash
PLACE 0,0,NORTH
LEFT
REPORT
```

stdout:

```bash
0,0,WEST
```

#### Example 3

```bash
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

stdout:

```bash
3,3,NORTH
```

## Development Guide

### Running the Test

You can run the tests by running the `pytest` command. See examples below. Be
sure to run these in your virtual environment shell.

Running the tests without coverage report.

```bash
pytest tests
```

Running the tests with coverage report to stdout.

```bash
pytest --cov=toy_robot_simulator tests
```

Running the tests with HTML format coverage report.

```bash
pytest --cov=toy_robot_simulator --cov-report html tests
```

### Docstring

The docstring format followed is the Google styleguide format.
See [Google Styleguide](https://google.github.io/styleguide/pyguide.html) to learn more.

Note that function summaries need to be in imperative mood as recommended in
[PEP 257](https://peps.python.org/pep-0257/).
