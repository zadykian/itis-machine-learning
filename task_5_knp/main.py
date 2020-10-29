from graph_edge import GraphEdge
from graph_node import GraphNode
from pandas import read_csv
from knp_algorithm import KnpAlgorithm



def main():
	# Преобразуем данные из CSV-файла в список точек.
	points_data_set = list(map(
		lambda row: GraphNode(row[0], row[1]),
		read_csv("data_set.csv")[['abscissa', 'ordinate']].values))

	algorithm = KnpAlgorithm(6)
	algorithm.perform_clustering(points_data_set)


if __name__ == "__main__":
	main()