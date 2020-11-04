from point import Point

# Кластеризованная точка в двумерном пространстве.
class ClassifiedPoint(Point):

    # Конструктор точки.
    # x - абсцисса
    # y - ордината
    # cluster_index - индекс кластера, к которому принадлежит точка.
    def __init__(self, x: float, y: float, cluster_index: int):
        Point.__init__(self, x, y)
        self._cluster_index = cluster_index

    # Индекс кластера, к которому принадлежит точка.
    @property
    def cluster_index(self) -> int:
        return self._cluster_index

    #  Строковое представление точки (для отладки).
    def __str__(self) -> str:
        return f'{Point.__str__(self)} : {self.cluster_index}'