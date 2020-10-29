from typing import List

from graph_edge import GraphEdge
from graph_node import GraphNode


# Неориентированный граф.
class Graph:

	def __init__(self):
		self._edges = []

	# Список рёбер, входящих в состав графа.
	@property
	def edges(self) -> List[GraphEdge]:
		return self._edges

	# Добавить в граф ребро graph_edge.
	def add_edge(self, graph_edge: GraphEdge):
		self._edges.append(graph_edge)

	# Определить, содержит ли граф узел graph_node.
	def contains_node(self, graph_node: GraphNode) -> bool:
		return any(map(
			lambda edge: edge.first_node == graph_node or edge.second_node == graph_node,
			self.edges))
