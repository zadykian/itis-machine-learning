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

    # Рассчитать расстояние между двумя точками на плоскости.
    def calculate_distance_to(self, second_point):
        return numpy.sqrt((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2)


# Получить центроид массива точек
def get_centroid(points):
    x_sum = sum(map(lambda p: p.x, points))
    y_sum = sum(map(lambda p: p.y, points))
    return Point(x_sum / len(points), y_sum / len(points))


# Получить оптимальное число кластеров
def get_optimal_clusters_number(points):
    current_distance_square_sum = 0

    for current_clusters_number in range(1, len(points)):
        previous_distance_square_sum = current_distance_square_sum
        current_distance_square_sum = 0

        algorithm = KMeansAlgorithm(current_clusters_number)
        algorithm.perform_clustering(points)

        for cluster_index in range(0, len(algorithm.clusters)):
            for point_in_cluster in algorithm.clusters[cluster_index]:
                current_distance_square_sum \
                    += point_in_cluster.calculate_distance_to(algorithm.centroids[cluster_index]) ** 2

        if previous_distance_square_sum - current_distance_square_sum < 5.0 and previous_distance_square_sum != 0:
            return current_clusters_number

    return len(points)


class KMeansAlgorithm:

    def __init__(self, k=3, max_iterations=1000):
        self.clusters = {}
        self.centroids = {}
        self.k = k
        self.max_iterations = max_iterations

    def perform_clustering(self, points):

        # Берём в качестве первоначальных центроидов первые k точек из массива данных.
        for i in range(self.k):
            self.centroids[i] = points[i]

        for i in range(self.max_iterations):
            for j in range(self.k):
                self.clusters[j] = []

            # Вычисляем расстояния от точки до всех центроидов, находим ближайший
            for point in points:

                distances_to_centroids = list(map(
                    lambda x: point.calculate_distance_to(x),
                    self.centroids.values()))

                classification = distances_to_centroids.index(min(distances_to_centroids))
                self.clusters[classification].append(point)

            previous_centroids = dict(self.centroids)

            # Находим новые центроиды кластеров
            for classification in self.clusters:
                self.centroids[classification] = get_centroid(self.clusters[classification])

            tolerance_is_reached = True

            # Проверяем, не достигнуто равновесие
            for centroid in self.centroids:

                previous_centroid = previous_centroids[centroid]
                current_centroid = self.centroids[centroid]
                if current_centroid != previous_centroid:
                    tolerance_is_reached = False

            if tolerance_is_reached:
                break


def main():
    # Преобразуем данные из CSV-файла в коллекцию точек.
    points_data_set = list(map(
        lambda row: Point(row[0], row[1]),
        pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values))

    optimal_clusters_number = get_optimal_clusters_number(points_data_set)
    algorithm = KMeansAlgorithm(optimal_clusters_number)
    algorithm.perform_clustering(points_data_set)

    colors = ["r", "g", "b", "c", "k"]

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
