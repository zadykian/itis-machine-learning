import pandas
import numpy
import matplotlib.pyplot as pyplot
from enum import Enum


# Цвет точки. Определяет её принадлежность к одной из трёх групп.
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
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = PointColor.Unknown
        self.is_visited = False

    # Расчитать расстояние между двумя точками на плоскости.
    def calculate_distance_to(self, second_point):
        return numpy.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)

    # Определить, была ли точка уже посещена.
    def is_visited(self):
        return self.is_visited

    # Установить цвет точки.
    def set_color(self, color):
        self.color = color
        self.is_visited = True


# алгоритм кластеризации dbscan - density-based spatial clustering of applications with noise
class DbScanAlgorithm:

    # max_neighbor_distance - максимальное расстояние между точками в одном кластере
    # min_neighbors_count - минимально необходимое число соседей для корневой точки
    def __init__(self, max_neighbor_distance, min_neighbors_count):
        self.max_neighbor_distance = max_neighbor_distance
        self.min_neighbors_count = min_neighbors_count

    # points_data_set - список точек Point для кластеризации
    def perform_clustering(self, points_data_set):
        clusters = {}

        for point in points_data_set:
            if point.is_visited():
                continue



def main():
    # Преобразуем данные из CSV-файла в коллекцию точек.
    points_data_set = list(map(
        lambda row: Point(row[0], row[1]),
        pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values))

    algorithm = DbScanAlgorithm(0.1, 3)
    clusters = algorithm.perform_clustering(points_data_set)


if __name__ == "__main__":
    main()
