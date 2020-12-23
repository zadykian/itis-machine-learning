from typing import List
from random import randrange

from generation_member import GenerationMember
from parameters import Parameters

class GenerationRunner:

    @staticmethod
    def perform_generation_step(generation: List[GenerationMember], inverse_coefficients_sum: float):
        for gen_index in range(Parameters.generation_size):

            current_value = 0
            for c_index in range(len(Parameters.coefficients)):
                current_value += generation[gen_index].values[c_index] * Parameters.coefficients[c_index]

            abs_value = abs(current_value - Parameters.free_member)

            if abs_value == 0:
                print("Решение уравнения: " + str(generation[gen_index].values))
                return True, inverse_coefficients_sum

            generation[gen_index].range_to_result = abs_value
            inverse_coefficients_sum += 1.0 / abs_value

        return False, inverse_coefficients_sum

    @staticmethod
    def recalculate_accuracy(
            generation: List[GenerationMember],
            inverse_coefficients_sum: float):

        for s in range(len(generation)):
            generation[s].accuracy = (1.0 / generation[s].range_to_result) / inverse_coefficients_sum

    @staticmethod
    def create_generation() -> List[GenerationMember]:
        return \
            [
                GenerationMember([randrange(Parameters.free_member) for _ in range(len(Parameters.coefficients))])
                for _ in range(Parameters.generation_size)
            ]