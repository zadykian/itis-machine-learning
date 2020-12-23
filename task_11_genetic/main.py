from random import randrange
from typing import List

from generation_member import GenerationMember
from generation_member_factory import GenerationMemberFactory

def recalculate_accuracy(gen, sum):
    for s in range(len(gen)):
        gen[s].accuracy = (1.0 / gen[s].range_to_result) / sum

def create_generation(param_count : int, res : int, generation_size : int) -> List[GenerationMember]:
    return \
        [
            GenerationMember([randrange(res) for _ in range(param_count)])
            for _ in range(generation_size)
        ]

def step(gen, sum, size, eq_parameters):
    for i in range(size):
        value = 0
        for j in range(len(eq_parameters)):
            value += gen[i].values[j] * eq_parameters[j]
        absValue = abs(value - Parameters.result)
        if absValue == 0:
            print("Solution: " + str(gen[i].values))
            return True, sum
        gen[i].range_to_result = absValue
        sum += 1.0 / absValue
    return False, sum

class Parameters:

    max_iterations = 50000
    result = 30
    generation_size = 16


def main():

    equation_parameters = [1, 2, 3, 4]
    inverse_coefficients_sum = 0.0
    iterator = 0

    generation = create_generation(len(equation_parameters), Parameters.result, Parameters.generation_size)

    solved, inverse_coefficients_sum = step(generation, inverse_coefficients_sum, Parameters.generation_size, equation_parameters)

    recalculate_accuracy(generation, inverse_coefficients_sum)

    while not solved and iterator < Parameters.max_iterations:
        inverse_coefficients_sum = 0.0
        generation = \
            [
                GenerationMemberFactory.create_new_generation_member(generation, equation_parameters)
                for _ in range(Parameters.generation_size)
            ]

        solved, inverse_coefficients_sum = step(generation, inverse_coefficients_sum, Parameters.generation_size, equation_parameters)
        if solved:
            break

        recalculate_accuracy(generation, inverse_coefficients_sum)

        iterator += 1

    print("Потребовалось итераций: " + str(iterator))

if __name__ == "__main__":
    main()