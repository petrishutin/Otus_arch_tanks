from __future__ import annotations

import abc
from logger import logger
from math import sqrt
from typing import List, Dict, Callable, Type

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

    def __init__(self, obj: object, position: Vector, velocity: Vector = None):
        self.obj = obj
        self.position = position
        self.velocity = velocity or Vector([0, 0])


class RotableObject:
    def __init__(self, obj: object, direction: int = 0):
        self.obj = obj
        self.direction: int = direction
        self.angular_velocity = 0
        self.max_directions = MAX_DIRECTIONS


class ErrorHandler:

    def __init__(self, error_mapping: Dict[Type, Callable] = None):
        self.error_mapping = error_mapping or {}

    # @property
    # def error_mapping(self) -> Dict[str, Callable]:
    #     return self.error_mapping
    #
    # @error_mapping.setter
    # def error_mapping(self, error_mapping: Dict[str, Callable]):
    #     self.error_mapping = error_mapping

    @staticmethod
    def _default_handler(e: Exception):
        logger.error(f'Default error handler called. Error{e}:')

    def handel(self, command: Command):
        try:
            command.execute()
        except Exception as e:
            handler = self.error_mapping.get(e.__class__, self._default_handler)
            handler(e)


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
