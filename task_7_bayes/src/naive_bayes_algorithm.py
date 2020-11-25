# Наивный Байесовский классификатор.
class NaiveBayesAlgorithm:

    def __init__(self,
                 symptom,
                 disease,
                 input_data):

        self._symptom = symptom
        self._disease = disease
        self._input_data = input_data

    # Получить наиболее вероятное заболевание.
    def get_most_probable_disease(self):

        patients_count_table = self._disease['количество пациентов'].to_numpy()
        total_patients_count = patients_count_table[len(patients_count_table) - 1]

        diseases_general_probabilities = [patients_count_table[i]
                                          / total_patients_count for i in range(len(patients_count_table) - 1)]

        diseases_names = self._disease['Болезнь'].head(len(self._disease['Болезнь']) - 1)
        diseases_probability = [1 for _ in range(0, len(diseases_names))]

        for disease_name_index in range(len(diseases_names)):
            diseases_probability[disease_name_index] *= diseases_general_probabilities[disease_name_index]
            for symptom_index in range(len(self._symptom) - 1):
                if self._input_data[symptom_index] == 1:
                    diseases_probability[disease_name_index] *= \
                        float(self._symptom.iloc[symptom_index][disease_name_index + 1].replace(',', '.'))

        most_possible_disease_index = diseases_probability.index(max(diseases_probability))
        return self._disease['Болезнь'][most_possible_disease_index]