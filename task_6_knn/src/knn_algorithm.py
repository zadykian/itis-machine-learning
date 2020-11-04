from typing import (Iterable, Tuple)
from itertools import groupby
from statistics import mean

from point import Point
from classified_point import ClassifiedPoint

# Алгоритм классификации kNN - k nearest neighbors.
class KnnAlgorithm:

    # Конструктор алгоритма.
    # nearest_neighbors_count - число ближайших точек для определения
    # принадлежности новой точки к одному из кластеров.
    def __init__(self, nearest_neighbors_count: int):
        self._nearest_neighbors_count = nearest_neighbors_count

    # Отнести точку point_to_classify к одному из кластеров
    # на основании набора данных training_dataset.
    def classify_point(self,
        training_dataset: Iterable[ClassifiedPoint],
        point_to_classify: Point) \
        -> ClassifiedPoint:

        # Ищем ближайших соседей.
        nearest_neighbors = self.get_nearest_neighbors_with_distances(training_dataset, point_to_classify)

        # Группируем ближайших соседей по кластерам, к которым они принадлежат.
        grouped_by_clusters = [
            (
                # Индекс кластера.
                cluster_index,
                # Число ближайших соседей, входящих в кластер.
                len(list(distance_tuples)),
                # Среднее расстояние от точки point_to_classify до соседей из кластера.
                mean(map(lambda distance_tuple: distance_tuple[1], distance_tuples))
            )
            for cluster_index, distance_tuples
            in map(
                lambda group: (group[0], list(group[1])),
                groupby(nearest_neighbors, lambda distance_tuple: distance_tuple[0].cluster_index))]

        # Выбираем кластеры, максимальные по числу ближайших к point_to_classify соседей.
        max_neighbor_clusters = filter(
            lambda cluster_tuple: cluster_tuple[1] == max(grouped_by_clusters, key=lambda t: t[1])[1],
            grouped_by_clusters)

        # Среди кластеров, максисальных по числу ближайших соседей,
        # выбираем кластер с минимальным средним расстоянием от point_to_cluster до ближайших соседей.
        min_distance_cluster = min(max_neighbor_clusters, key=lambda cluster_tuple: cluster_tuple[2])

        cluster_index = min_distance_cluster[0]
        return ClassifiedPoint(point_to_classify.x, point_to_classify.y, cluster_index)

    # Получить ближайших соседей для точки point_to_classify из выборки training_dataset.
    def get_nearest_neighbors_with_distances(self,
        training_dataset : Iterable[ClassifiedPoint],
        point_to_classify : Point)\
        -> Iterable[Tuple[ClassifiedPoint, float]]:

        # Вычисляем расстояние от point_to_classify до каждой точки из обучающей выборки.
        dataset_with_distances = [
            (
                classified_point,
                point_to_classify.calculate_distance_to(classified_point)
            )
            for classified_point
            in training_dataset]

        # Получаем {nearest_neighbors_count} ближайших соседей.
        return sorted(
            dataset_with_distances, key=lambda distance_tuple: distance_tuple[1]) \
            [: self._nearest_neighbors_count]