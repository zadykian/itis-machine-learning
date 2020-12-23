from generation_member_factory import GenerationMemberFactory
from parameters import Parameters
from generation_runner import GenerationRunner

def main():
    print(f'Коэффициенты при неизвестных: {Parameters.coefficients}')
    print(f'Свободный член: {Parameters.free_member}')

    inverse_coefficients_sum = 0.0
    generation = GenerationRunner.create_generation()

    solutions_is_found, inverse_coefficients_sum = GenerationRunner.perform_generation_step(
        generation,
        inverse_coefficients_sum)

    GenerationRunner.recalculate_accuracy(generation, inverse_coefficients_sum)

    current_iteration = 0
    while not solutions_is_found and current_iteration < Parameters.max_iterations:
        inverse_coefficients_sum = 0.0
        generation = \
            [
                GenerationMemberFactory.create_new_generation_member(generation)
                for _ in range(Parameters.generation_size)
            ]

        solutions_is_found, inverse_coefficients_sum = GenerationRunner.perform_generation_step(
            generation,
            inverse_coefficients_sum)

        if solutions_is_found:
            break

        GenerationRunner.recalculate_accuracy(generation, inverse_coefficients_sum)
        current_iteration += 1

    if solutions_is_found:
        print(f'Потребовалось итераций: {current_iteration}')
    else:
        print(f'Превышено максимальное число итераций ({Parameters.max_iterations})')

if __name__ == "__main__":
    main()