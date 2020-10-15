import sys

import numpy


# Найти ребро в графе, имеющее минимальный вес, добавить его в tree
def first_connection():
    minim = weight[0][1]
    i_min, j_min = 0, 1

    for i in range(n):
        for j in range(i+1, n):
            if minim > weight[i][j]:
                minim = weight[i][j]
                i_min, j_min = i, j

    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim

    weight[i_min][j_min] = sys.maxsize
    weight[j_min][i_min] = sys.maxsize


def link_all():
    return -1


# число вершин в графе
n = 5

weight = [[0 for i in range(n)] for i in range(n)]

for i in range(0, n):
    for j in range(i+1, n):
        weight[i][j] = numpy.random.randint(1, 100)
        weight[j][i] = weight[i][j]

tree = [[0 for i in range(n)] for i in range(n)]
first_connection()

print(weight)
