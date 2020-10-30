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

        # Строим минимальное остовное дерево.
        # Пока граф не содержит все узлы из points,
        # ищем минимальное ребро, связывающее новый узел с графом.
        while any(map(
            lambda point: not graph.contains_node(point),
            points)):

            min_edge_to_add = self.get_edge_with_min_weight(
                points,
                # Если граф пуст, ищем минимальное ребро среди всех возможных,
                # иначе - ищем минимальное ребро, один узел которого находится в графе, а второй - ещё нет.
                lambda edge:
                    graph.is_empty
                    or graph.contains_node(edge.first_node) and not graph.contains_node(edge.second_node)
                    or not graph.contains_node(edge.first_node) and graph.contains_node(edge.second_node))

            graph.add_edge(min_edge_to_add)

        # Сортируем ребра по весу в порядке убывания
        # и отсекаем первые (required_clusters_number - 1) ребер.
        edges_without_longest = \
            sorted(graph.edges, key=lambda edge: edge.weight, reverse=True) \
            [self._required_clusters_number - 1:]

        return Graph(edges_without_longest)

    # Найти среди points две точки, наиболее близко расположенные друг к другу,
    # и сформировать соединяющее их ребро GraphEdge.
    @staticmethod
    def get_edge_with_min_weight(
        # Список всех точек (узлов графа) для кластеризации.
        points: List[GraphNode],
        # Предикат для поиска ребра.
        edge_predicate) -> GraphEdge:

        # Генерируем все возможные варианты ребер.
        all_edge_combinations = [GraphEdge(first_point, second_point)
            for first_point in points
            for second_point in points
            if first_point != second_point]

        min_edge = None

        # При помощи set() убираем дубликаты вида [a-b] [b-a], так как граф неориентированный.
        for current_edge in set(all_edge_combinations):
            if min_edge is None or edge_predicate(current_edge) and current_edge.weight < min_edge.weight:
                min_edge = current_edge

        return min_edge