from numpy import sqrt


# Точка в двумерном пространстве.
class Point:

    # Конструктор точки.
    # x - абсцисса
    # y - ордината
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    # Абсцисса точки.
    @property
    def x(self) -> float:
        return self._x

    # Ордината точки.
    @property
    def y(self) -> float:
        return self._y

    # Сравнить точку с точкой other_point.
    def __eq__(self, other_point) -> bool:
        return self.x == other_point.x and self.y == other_point.y

    # Расчитать расстояние на плоскости между двумя точками.
    def calculate_distance_to(self, other_point) -> float:
        return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    #  Строковое представление узла (для отладки).
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'