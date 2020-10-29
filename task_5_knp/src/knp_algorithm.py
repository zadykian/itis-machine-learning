from typing import List

from graph_node import GraphNode
from graph_edge import GraphEdge
from graph import Graph


# Алгоритм кластеризации КНП (поиск кратчайшего незамкнутого пути).
class KnpAlgorithm:

	# Конструктор алгоритма.
	# required_clusters_number - требуемое число кластеров.
	def __init__(self, required_clusters_number: int):
		self._required_clusters_number = required_clusters_number

	# Выполнить кластеризацию списка точек и сформировать результат в виде графа.
	# Граф - лес, состоящий их required_clusters_number компонентов.
	def perform_clustering(self, points: List[GraphNode]) -> Graph:
		graph = Graph()

		# Пока граф не содержит все узлы из points,
		# ищем минимальное ребро, связывающее новый узел с графом.
		while all(map(
				lambda point: graph.contains_node(point),
				points)):

			min_edge_to_add = self.get_edge_with_min_weight(
				points,
				# Ищем ребро, один узел которого находится в графе, а второй - ещё нет.
				lambda edge:
					graph.contains_node(edge.first_node) and not graph.contains_node(edge.second_node)
					or not graph.contains_node(edge.first_node and graph.contains_node(edge.second_node)))

			graph.add_edge(min_edge_to_add)

		return graph

	# Найти среди points две точки, наиболее близко расположенные друг к другу,
	# и сформировать соединяющее их ребро GraphEdge.
	@staticmethod
	def get_edge_with_min_weight(
			# Список всех точек (узлов графа) для кластеризации.
			points: List[GraphNode],
			# Предикат для поиска ребра.
			edge_predicate) -> GraphEdge:

		min_edge = GraphEdge(points[0], points[1])

		for outer_point in points:
			for inner_point in filter(lambda point: point != outer_point, points):
				current_edge = GraphEdge(outer_point, inner_point)
				if edge_predicate(current_edge) and current_edge.weight < min_edge.weight:
					min_edge = current_edge

		return min_edge
