from numpy import random
from random import randrange
from typing import List

from generation_member import GenerationMember

# Фабрика создания представителей поколений.
class GenerationMemberFactory:

    # Создать представителя нового поколения на основании списка родителей.
    @staticmethod
    def create_new_generation_member(
        current_generation : List[GenerationMember],
        equation_parameters) -> GenerationMember:

        probability_distribution = [current_generation[x].accuracy for x in range(len(current_generation))]
        parent1, parent2 = random.choice(current_generation, 2, p=probability_distribution)
        if parent1 == parent2:
            parent2 = random.choice(current_generation, 1, p=probability_distribution)[0]
        rnd = randrange(len(equation_parameters))

        dominant_parent = randrange(2)
        if dominant_parent == 0:
            new_gen = parent1.values
            new_gen[rnd] = parent2.values[rnd]
        else:
            new_gen = parent2.values
            new_gen[rnd] = parent1.values[rnd]

        mutation_probability = randrange(101)
        mutation_chance = 10

        if mutation_probability < mutation_chance:
            rand2 = randrange(len(equation_parameters))
            new_gen[rand2] = randrange(31)

        return GenerationMember(new_gen)