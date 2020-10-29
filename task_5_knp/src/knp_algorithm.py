from typing import List

from graph_node import GraphNode
from graph_edge import GraphEdge

# Алгоритм кластеризации КНП (поиск кратчайшего незамкнутого пути).
class KnpAlgorithm:

	# Конструктор алгоритма.
	# required_clusters_number - требуемое число кластеров.
	def __init__(self, required_clusters_number: int):
		self._required_clusters_number = required_clusters_number

	def perform_clustering(self, points: List[GraphNode]):
		return 0

	# Найти среди points две точки, наиболее близко расположенные друг к другу и сформировать ребро GraphEdge
	@staticmethod
	def get_edge_with_min_weight(points: List[GraphNode]) -> GraphEdge:
		min_edge = GraphEdge(points[0], points[1])

		for outer_point in points:
			for inner_point in filter(lambda point: point != outer_point, points):
				current_edge = GraphEdge(outer_point, inner_point)
				if current_edge.weight < min_edge.weight:
					min_edge = current_edge

		return min_edge
