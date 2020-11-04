from typing import Iterable

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

        raise Exception('not implemented!')