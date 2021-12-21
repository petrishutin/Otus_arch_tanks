from math import sqrt
from typing import List


class Vector:
    def __init__(self, body: List[int]):
        self.body: tuple = tuple(body)

    def __add__(self, other):
        new_body = list(
            (map(lambda x: sum(x), zip(self.body, other.body)))
        )
        return Vector(new_body)

    def __repr__(self):
        return f'Vector: {self.body}'

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
