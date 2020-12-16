from point import Point

# Кластеризованная точка.
class ClassifiedPoint(Point):

    # Конструктор кластеризованной точки.
    # point - некластеризованная точка;
    # cluster_index - индекс кластера, к которому принадлежит точка.
    def __init__(self, point: Point, cluster_index: int):
        Point.__init__(self, point.x, point.y, point.z)
        self._cluster_index = cluster_index

    # Индекс кластера, к которому принадлежит точка.
    @property
    def cluster_index(self) -> int:
        return self._cluster_index

    #  Строковое представление точки (для отладки).
    def __str__(self) -> str:
        return f'{Point.__str__(self)} : {self.cluster_index}'