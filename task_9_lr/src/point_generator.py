from typing import Iterable
from random import (seed, random)
from point import Point

# Генератор точек.
class PointGenerator:

    # Сгенерировать points_count случайных точек в трехмерном пространстве.
    # Диапазон по всем осям - [0..1].
    @staticmethod
    def generate_random_points(points_count: int) -> Iterable[Point]:
        seed()
        def random_value(): return round(random(), 3)

        return \
            [
                Point(random_value(), random_value(), random_value())
                for _ in range(0, points_count)
            ]
