from typing import List, Iterable
from pandas import read_csv
from matplotlib.pyplot import (scatter, show)
from random import (seed, random)

from point import Point
from classified_point import ClassifiedPoint
from knn_algorithm import KnnAlgorithm

def main():
    # Считываем список кластеризованных точек.
    training_dataset = read_dataset_from_csv('training_dataset')
    draw_dataset(training_dataset)

    knn_algorithm = KnnAlgorithm(16)

    # Генерируем случайные точки,
    # определяем кластер, к которому они принадлежат.
    classified_points = [knn_algorithm.classify_point(training_dataset, random_point)
                         for random_point
                         in generate_test_dataset(16)]

    draw_dataset(classified_points, 's')
    show()

# Чтитать из CSV-файла с именем file_name список точек.
def read_dataset_from_csv(file_name: str) -> List[ClassifiedPoint]:
    return list(map(
        lambda row: ClassifiedPoint(row[0], row[1], int(row[2])),
        read_csv(f'{file_name}.csv')[['abscissa', 'ordinate', 'cluster_index']].values))

# Сгенерировать тестовый набор данных для кластеризации.
def generate_test_dataset(rows_count: int) -> Iterable[Point]:
    seed()
    def random_coordinate(): return round(random(), 3)
    return [Point(random_coordinate(), random_coordinate()) for _ in range(1, rows_count)]

# Отрисовать коллекцию точек, используя маркер marker_style.
def draw_dataset(dataset: Iterable[ClassifiedPoint], marker_style: chr = '.'):
    colors = ["r", "g", "b", "c", "k"]
    for point in dataset:
        scatter(point.x, point.y, c=colors[point.cluster_index], marker=marker_style)

if __name__ == "__main__":
    main()