from point import Point


# Ребро неориентированного графа, соединяющее две точки на плоскости.
class GraphEdge:

	def __init__(self, first_node: Point, second_node: Point):
		self._first_node = first_node
		self._second_node = second_node

	# Первый узел графа, принадлежащий ребру.
	@property
	def first_node(self) -> Point:
		return self._first_node

	# Второй узел графа, принадлежащий ребру.
	@property
	def second_node(self) -> Point:
		return self._second_node

	# Вес ребра - расстояние между точками.
	@property
	def weight(self) -> float:
		return self.first_node.calculate_distance_to(self.second_node)

	# Строковое представление ребра (для отладки).
	def __str__(self) -> str:
		return f'{self.first_node} - {self.second_node}'