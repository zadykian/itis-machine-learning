from numpy import random
from random import randrange
from typing import List

from generation_member import GenerationMember
from parameters import Parameters

# Фабрика создания представителей поколений.
class GenerationMemberFactory:

    # Создать представителя нового поколения на основании списка родителей.
    @staticmethod
    def create_new_generation_member(
        current_generation : List[GenerationMember]) -> GenerationMember:

        probability_distribution = [current_generation[x].accuracy for x in range(len(current_generation))]
        parent1, parent2 = random.choice(current_generation, 2, p=probability_distribution)
        if parent1 == parent2:
            parent2 = random.choice(current_generation, 1, p=probability_distribution)[0]
        rnd = randrange(len(Parameters.coefficients))

        dominant_parent = randrange(2)
        if dominant_parent == 0:
            new_generation_value = parent1.values
            new_generation_value[rnd] = parent2.values[rnd]
        else:
            new_generation_value = parent2.values
            new_generation_value[rnd] = parent1.values[rnd]

        if randrange(100) < 10:
            rand2 = randrange(len(Parameters.coefficients))
            new_generation_value[rand2] = randrange(Parameters.free_member)

        return GenerationMember(new_generation_value)