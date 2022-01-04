import pytest

from game.game_objects import UObject, Vector, MovableObject, RotableObject, Move, Rotate, ErrorHandler
from logger import logger


def test_vector():
    v1 = Vector([1, 1, 1])
    assert v1
    assert str(v1) == "(1, 1, 1)"
    v2 = Vector([1, 1, 1])
    v_sum = v1 + v2
    assert isinstance(v_sum, Vector)
    assert v_sum.body == (2, 2, 2)
    assert len(v_sum) == 3
    assert v_sum == Vector([2, 2, 2])


@pytest.fixture
def movable_tank():
    tank = UObject()
    return MovableObject(tank, Vector([12, 5]))


def test_move_tank(movable_tank):
    assert movable_tank.velocity.body == (0, 0)
    movable_tank.velocity = Vector([-7, 3])
    assert movable_tank.velocity.body == (-7, 3)
    Move(movable_tank).execute()
    assert movable_tank.position.body == (5, 8)


@pytest.fixture
def rotable_tank():
    tank = UObject()
    return RotableObject(tank)


def test_rotate_tank(rotable_tank):
    assert rotable_tank.direction == 0
    assert rotable_tank.angular_velocity == 0
    rotable_tank.angular_velocity = 5
    assert rotable_tank.angular_velocity == 5
    Rotate(rotable_tank).execute()
    assert rotable_tank.direction == 1


def test_move_unmovable(rotable_tank):
    """Check if attempt to move unmovable object in handler raises an error in run time"""
    with pytest.raises(AttributeError):
        Move(rotable_tank).execute()


def test_error_handler(rotable_tank, caplog):
    """Check if attempt to move unmovable object in handler does NOT raise an error in run time"""
    ErrorHandler().handel(Move(rotable_tank))
    assert 'Default error handler called. Error' in caplog.text


def test_error_handler_with_error_mapping(rotable_tank, caplog):
    def _custom_handler(e):
        logger.error(f'Custom error handler called. Error{e}:')

    handler = ErrorHandler()
    handler.error_mapping.update({AttributeError: _custom_handler})
    handler.handel(Move(rotable_tank))
    assert 'Custom error handler called. Error' in caplog.text
