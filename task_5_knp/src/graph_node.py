from numpy import sqrt


# Узел графа - точка в двумерном пространстве.
class GraphNode:

	# Конструктор узла.
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

	# Сравнить узел с узлом other_point.
	def __eq__(self, other_node) -> bool:
		return self.x == other_node.x and self.y == other_node.y

	# Сравнить узел с узлом other_point.
	def __ne__(self, other_node) -> bool:
		return not (self == other_node)

	# Расчитать расстояние на плоскости между двумя узлами.
	def calculate_distance_to(self, other_node) -> float:
		return sqrt((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2)

	#  Строковое представление узла (для отладки).
	def __str__(self) -> str:
		return f'({self.x}, {self.y})'