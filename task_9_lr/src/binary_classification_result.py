from typing import Iterable
from classified_point import ClassifiedPoint
from plane import Plane


# Результат бинарной классификации.
class BinaryClassificationResult:

    # Конструктор результата.
    # classified_points - последовательность точек, разбитых на два класса;
    # dividing_plane - плоскость, разделяющая набор точек на классы.
    def __init__(self,
                 classified_points: Iterable[ClassifiedPoint],
                 dividing_plane: Plane):

        self._classified_points = list(classified_points)
        self._dividing_plane = dividing_plane

    # Точки, разбитые на два класса.
    @property
    def classified_points(self) -> Iterable[ClassifiedPoint]:
        return self._classified_points

    # Плоскость, разделяющая набор точек на два класса.
    @property
    def dividing_plane(self) -> Plane:
        return self._dividing_plane
