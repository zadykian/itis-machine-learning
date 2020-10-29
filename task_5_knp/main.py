from graph_node import GraphNode
from graph_edge import GraphEdge
from pandas import read_csv
from knp_algorithm import KnpAlgorithm
from matplotlib.pyplot import (scatter, plot, show)


def main():
	# Преобразуем данные из CSV-файла в список точек.
	points_data_set = list(map(
		lambda row: GraphNode(row[0], row[1]),
		read_csv("data_set.csv")[['abscissa', 'ordinate']].values))

	algorithm = KnpAlgorithm(6)
	graph = algorithm.perform_clustering(points_data_set)

	for graph_edge in graph.edges:
		draw_graph_edge(graph_edge)

	show()

# Отрисовать ребро графа.
def draw_graph_edge(graph_edge: GraphEdge):
	scatter(graph_edge.first_node.x, graph_edge.first_node.y, c='green', marker='^')
	scatter(graph_edge.second_node.x, graph_edge.second_node.y, c='green', marker='^')

	x_values = [graph_edge.first_node.x, graph_edge.second_node.x]
	y_values = [graph_edge.first_node.y, graph_edge.second_node.y]
	plot(x_values, y_values, c='green')


if __name__ == "__main__":
	main()