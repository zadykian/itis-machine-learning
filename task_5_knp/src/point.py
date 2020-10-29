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
	def __eq__(self, other_point):
		return self.x == other_point.x and self.y == other_point.y

	# Сравнить точку с точкой other_point.
	def __ne__(self, other_point):
		return not (self == other_point)

	# Расчитать расстояние между двумя точками на плоскости.
	def calculate_distance_to(self, other_point) -> float:
		return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

	#  Строковое представление точки (для отладки).
	def __str__(self):
		return f'({self.x}, {self.y})'