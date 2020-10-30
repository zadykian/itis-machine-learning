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

    # Выполняем кластеризацию.
    algorithm = KnpAlgorithm(3)
    graph = algorithm.perform_clustering(points_data_set)

    # Отрисовываем полученный лес.
    for graph_node in points_data_set: draw_graph_node(graph_node)
    for graph_edge in graph.edges: draw_graph_edge(graph_edge)
    show()


# Отрисовать узел графа.
def draw_graph_node(graph_node: GraphNode):
    scatter(graph_node.x, graph_node.y, c='green', marker='^')


# Отрисовать ребро графа.
def draw_graph_edge(graph_edge: GraphEdge):
    x_values = [graph_edge.first_node.x, graph_edge.second_node.x]
    y_values = [graph_edge.first_node.y, graph_edge.second_node.y]
    plot(x_values, y_values, c='green')


if __name__ == "__main__":
    main()