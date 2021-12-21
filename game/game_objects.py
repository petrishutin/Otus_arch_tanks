import abc
from math import sqrt
from typing import List

MAX_DIRECTIONS: int = 4


class Vector:
    def __init__(self, body: List[int]):
        self.body: tuple = tuple(body)

    def __add__(self, other):
        new_body = list(
            (map(lambda x: sum(x), zip(self.body, other.body)))
        )
        return Vector(new_body)

    def __repr__(self):
        return f'{self.body}'

    def __len__(self):
        return int(
            sqrt(
                sum(
                    map(lambda x: x ** 2, self.body)
                )
            )
        )

    def __eq__(self, other):
        return all(
            list(
                map(lambda x: x[0] == x[1], zip(self.body, other.body))
            )
        )

    def __bool__(self):
        return True


class UObject:
    pass


class MovableObject:

    def __init__(self, obj: object, position: Vector):
        self.obj = obj
        self.position = position
        self.velocity = Vector([0, 0])


class RotableObject:
    def __init__(self, obj: object, direction: int = 0):
        self.obj = obj
        self.direction: int = direction
        self.angular_velocity = 0
        self.max_directions = MAX_DIRECTIONS


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError


class Move(Command):
    def __init__(self, obj: MovableObject):
        self.obj = obj

    def execute(self):
        self.obj.position += self.obj.velocity


class Rotate(Command):
    def __init__(self, obj: RotableObject):
        self.obj = obj

    def execute(self):
        self.obj.direction = (self.obj.direction + self.obj.angular_velocity) % self.obj.max_directions
