import pandas
import numpy
import matplotlib.pyplot as pyplot


# Точка в двумерном пространстве.
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)

    # Расчитать расстояние между двумя точками на плоскости.
    def calculate_distance_to(self, second_point):
        return numpy.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)


class DbScanAlgorithm:

    # max_neighbor_distance - максимальное расстояние между точками в одном кластере
    # min_neighbors_count - минимально необходимое число соседей для корневой точки
    def __init__(self, max_neighbor_distance, min_neighbors_count):
        self.max_neighbor_distance = max_neighbor_distance
        self.min_neighbors_count = min_neighbors_count

    # data_set - список точек Point для кластеризации
    def perform_clustering(self, data_set):
        return 0


def main():
    # Преобразуем данные из CSV-файла в коллекцию точек.
    points_data_set = list(map(
        lambda row: Point(row[0], row[1]),
        pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values))


if __name__ == "__main__":
    main()
