from typing import Iterable
from classified_point import ClassifiedPoint
from plane import Plane

from sklearn import linear_model

# Алгоритм классификации на основе логистической регрессии.
class LogisticRegressionClassifier:

    # Выполнить классификацию коллекции точек.
    @staticmethod
    def perform_classification(input_points: Iterable[ClassifiedPoint]) -> Plane:
        classifier = linear_model.LogisticRegression()
        classifier.fit()