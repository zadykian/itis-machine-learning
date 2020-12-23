
# Представитель одного поколения.
class GenerationMember:

    def __init__(self, values, accuracy = 0.0):
        self._values = values
        self._accuracy = accuracy
        self._range_to_result = 0

    @property
    def accuracy(self) -> float:
        return self._accuracy