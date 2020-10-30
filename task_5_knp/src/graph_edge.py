from graph_node import GraphNode


# Ребро неориентированного графа, соединяющее две точки на плоскости.
class GraphEdge:

    def __init__(self, first_node: GraphNode, second_node: GraphNode):
        self._first_node = first_node
        self._second_node = second_node

    # Первый узел графа, принадлежащий ребру.
    @property
    def first_node(self) -> GraphNode:
        return self._first_node

    # Второй узел графа, принадлежащий ребру.
    @property
    def second_node(self) -> GraphNode:
        return self._second_node

    # Вес ребра - расстояние между узлами (точками на плоскости).
    @property
    def weight(self) -> float:
        return self.first_node.calculate_distance_to(self.second_node)

    # Определить, равны ли два ребра.
    def __eq__(self, other_edge) -> bool:
        return \
            self.first_node == other_edge.first_node and self.second_node == other_edge.second_node \
            or self.second_node == other_edge.first_node and self.first_node == other_edge.second_node

    # Получить хеш-код ребра.
    def __hash__(self) -> int:
        return hash(self.first_node) ^ hash(self.second_node)

    # Строковое представление ребра (для отладки).
    def __str__(self) -> str:
        return f'{self.first_node} - {self.second_node} : {self.weight}'