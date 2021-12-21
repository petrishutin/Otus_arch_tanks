from game_objects import Vector


def test_vector():
    v1 = Vector([1, 1, 1])
    assert str(v1) == "Vector: (1, 1, 1)"
    v2 = Vector([1, 1, 1])
    v_sum = v1 + v2
    assert isinstance(v_sum, Vector)
    assert v_sum.body == (2, 2, 2)
    assert len(v_sum) == 3
    assert v_sum == Vector([2, 2, 2])
