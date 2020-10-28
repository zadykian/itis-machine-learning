import pandas
import numpy
import matplotlib.pyplot as pyplot
from enum import Enum
from typing import Optional


# Цвет точки. Определяет её принадлежность к одной из трёх групп.
from typing import List


class PointColor(Enum):
    # Зелёные точки являются корневыми - имеют не менее, чем min_neighbors_count, соседей.
    Green = 1
    # Жёлтые точки имеют хотя бы одну зелёную точку на расстоянии, не превышающем max_neighbor_distance.
    Yellow = 2
    # Красные точки не имеют ни одного зелёного соседа.
    Red = 3
    # Цвет точки ещё не определён.
    Unknown = -1


# Точка в двумерном пространстве.
class Point(object):

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y
        self._color = PointColor.Unknown
        self._is_visited = False
        self._cluster_index = None

    # Абсцисса точки.
    @property
    def x(self) -> float:
        return self._x

    @property
    # Ордината точки.
    def y(self) -> float:
        return self._y

    # Получить цвет точки.
    @property
    def color(self) -> PointColor:
        return self._color

    # Установить цвет точки.
    @color.setter
    def color(self, color: PointColor):
        self._color = color
        self._is_visited = True

    # Была ли точка уже посещена.
    @property
    def is_visited(self):
        return self._is_visited

    # Получить индекс кластера, которому принадлежит точка.
    @property
    def cluster_index(self) -> Optional[int]:
        return self._cluster_index

    # Установить индекс кластера, которому принадлежит точка.
    @cluster_index.setter
    def cluster_index(self, cluster_index: int):
        self._cluster_index = cluster_index

    # Расчитать расстояние между двумя точками на плоскости.
    def calculate_distance_to(self, second_point):
        return numpy.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)


# алгоритм кластеризации dbscan - density-based spatial clustering of applications with noise
class DbScanAlgorithm:

    # max_neighbor_distance - максимальное расстояние между точками в одном кластере
    # min_neighbors_count - минимально необходимое число соседей для корневой точки
    def __init__(self,
                 max_neighbor_distance: float,
                 min_neighbors_count: float):
        self._max_neighbor_distance = max_neighbor_distance
        self._min_neighbors_count = min_neighbors_count

    # Выполнить кластеризацию.
    # points_data_set - список точек Point.
    def perform_clustering(self, points_data_set: List[Point]):
        current_cluster_index = 0

        for current_point in points_data_set:
            if current_point.is_visited:
                continue

            # Получаем соседей.
            neighbors = self.get_neighbors_of(current_point, points_data_set)

            if len(neighbors) < self._min_neighbors_count:
                current_point.color = PointColor.Red
                continue

            current_point.cluster_index = current_cluster_index
            current_cluster_index += 1

            for neighbor in neighbors:
                if neighbor.is_visited:
                    continue
                neighbor.cluster_index = current_point.cluster_index

                neighbors_of_neighbor = self.get_neighbors_of(neighbor, points_data_set)
                if len(neighbors_of_neighbor) >= self._min_neighbors_count:
                    neighbor.color = PointColor.Green
                    neighbors += neighbors_of_neighbor
                else:
                    neighbor.color = PointColor.Yellow

        for yellow_point in filter(lambda point: point.color == PointColor.Yellow, points_data_set):
            nearest_green_point = self.get_nearest_green_point(yellow_point, points_data_set)
            yellow_point.cluster_index = nearest_green_point.cluster_index

    # Найти соседей точки origin_point среди точек points_list
    # на основании значения _max_neighbor_distance
    def get_neighbors_of(self, origin_point: Point, points_list: List[Point]):
        return list(filter(
                lambda point: origin_point.calculate_distance_to(point) <= self._max_neighbor_distance,
                points_list))

    # Найти среди points_list ближайшую к origin_point зелёную точку.
    @staticmethod
    def get_nearest_green_point(origin_point: Point, points_list: List[Point]) -> Point:
        min_distance = min(map(
            lambda point: origin_point.calculate_distance_to(point),
            points_list))

        return next(filter(
            lambda point: origin_point.calculate_distance_to(point) == min_distance,
            points_list))


def main():
    # Преобразуем данные из CSV-файла в коллекцию точек.
    points_data_set = list(map(
        lambda row: Point(row[0], row[1]),
        pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values))

    algorithm = DbScanAlgorithm(0.075, 3)
    algorithm.perform_clustering(points_data_set)

    # маркеры для определения принадлежности точки кластеру.
    cluster_markers = ['D', '<', '>', 's', 'P', 'X', '^', 'v']

    for point in points_data_set:
        point_marker = 'o' if point.cluster_index is None else cluster_markers[point.cluster_index]
        pyplot.scatter(point.x, point.y,
                       c=point.color.name.lower(),
                       marker=point_marker)

    pyplot.show()


if __name__ == "__main__":
    main()
