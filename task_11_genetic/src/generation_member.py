# Представитель одного поколения.
class GenerationMember:

    def __init__(self, values, accuracy: float = 0.0):
        self._values = values
        self._accuracy = accuracy
        self._range_to_result = 0

    @property
    def values(self):
        return self._values

    @property
    def accuracy(self) -> float:
        return self._accuracy

    @accuracy.setter
    def accuracy(self, value: float):
        self._accuracy = value

    @property
    def range_to_result(self) -> float:
        return self._range_to_result

    @range_to_result.setter
    def range_to_result(self, value: float):
        self._range_to_result = value
