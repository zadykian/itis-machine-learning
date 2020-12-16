# Точка в трехмерном пространстве.
class Point:

    # Конструктор точки.
    # x - абсцисса;
    # y - ордината;
    # z - аппликата.
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    # Абсцисса точки.
    @property
    def x(self) -> float:
        return self._x

    # Ордината точки.
    @property
    def y(self) -> float:
        return self._y

    # Аппликата точки.
    @property
    def z(self) -> float:
        return self._z

    #  Строковое представление точки (для отладки).
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'