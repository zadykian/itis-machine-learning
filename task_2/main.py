import pandas
import numpy
import matplotlib.pyplot as pyplot


# Точка в двумерном пространстве.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Расчитать расстояние между двумя точками на плоскости.
def calculate_distance(first_point: Point, second_point: Point):
    return numpy.sqrt(
        (first_point.x - second_point.x) ** 2
        + (first_point.y - second_point.y) ** 2)


class KMeansAlgorithm:

    def __init__(self, k=3, tolerance=0.0001, max_iterations=500):
        self.k = k
        self.tolerance = tolerance
        self.max_iterations = max_iterations

    def perform_clustering(self, points):

        self.centroids = {}
        # Берём в качестве первоначальных цетроидов первые k точек из массива данных.
        for i in range(self.k):
            self.centroids[i] = points[i]

        for i in range(self.max_iterations):
            self.clusters = {}
            for i in range(self.k):
                self.clusters[i] = []

            # Вычисляем расстояния от точки до всех центроидов, находим ближайший
            for point in points:

                distances_to_centroids = list(map(
                    lambda x: calculate_distance(point, x),
                    self.centroids.values()))

                classification = distances_to_centroids.index(min(distances_to_centroids))
                self.clusters[classification].append(point)

            previous = dict(self.centroids)

            # Вычисляем новый центроид кластера.
            for classification in self.clusters:
                self.centroids[classification] = numpy.average(self.clusters[classification], axis=0)

            # Проверяем, не достигнута ли требуемый шаг изменения позиции центроидов
            for centroid in self.centroids:

                original_centroid = previous[centroid]
                current_centroid = self.centroids[centroid]

                if numpy.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tolerance:
                    break


def main():
    # Преобразуем данные из CSV-файла в коллекцию точек.
    points_data_set = map(
        lambda row: Point(row[0], row[1]),
        pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values)

    algorithm = KMeansAlgorithm(3)
    algorithm.perform_clustering(list(points_data_set))

    colors = 10 * ["r", "g", "c", "b", "k"]

    # Отрисовываем центроиды
    for centroid in algorithm.centroids:
        pyplot.scatter(algorithm.centroids[centroid].x, algorithm.centroids[centroid].y, marker="x")

    # Отрисовываем кластеры
    for classification in algorithm.clusters:
        for point in algorithm.clusters[classification]:
            pyplot.scatter(point.x, point.y, color=colors[classification])

    pyplot.show()


if __name__ == "__main__":
    main()
