from pandas import read_csv
from numpy import random

from naive_bayes_algorithm import NaiveBayesAlgorithm


def main():
    disease = read_csv(r'disease.csv', sep=';')
    symptom = read_csv(r'symptom.csv', sep=';')

    random_input_data = [random.randint(2) for _ in range(len(symptom) - 1)]
    symptom_names = list(map(lambda row: row[0], symptom.values))[1:]

    print('Список симптомов:')
    print(list(
        map(
            lambda pair: symptom_names[pair[0]],
            filter(
                lambda pair: pair[1] == 1,
                zip(
                    range(0, len(random_input_data) - 1),
                    random_input_data
                )))))

    algorithm = NaiveBayesAlgorithm(symptom, disease, random_input_data)
    most_probable_disease = algorithm.get_most_probable_disease()

    print('Наиболее вероятное заболевание:')
    print(most_probable_disease)


if __name__ == "__main__":
    main()
