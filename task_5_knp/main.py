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

    connect_pnt[i_min] = 1
    connect_pnt[j_min] = 1


# Добавить в tree вершину, имеющую минимальный путь до существующего дерева
def link_all():
    minim = sys.maxsize
    i_min, j_min = None, None

    for i in range(n):
        if connect_pnt[i] == 1:
            for j in range(0, n):
                if connect_pnt[j] == 0:
                    if minim > weight[i][j]:
                        minim = weight[i][j]
                        i_min, j_min = i, j

    tree[i_min][j_min] = minim
    tree[j_min][i_min] = minim
    weight[i_min][j_min] = weight[j_min][i_min] = sys.maxsize
    connect_pnt[i_min] = connect_pnt[j_min] = 1


# Удалить из tree ребро с наибольшим весом
def delete_connection():
    maxim = 0
    i_max, j_max = 0, 0

    for i in range(n):
        for j in range(i+1, n):
            if tree[i][j] > maxim:
                maxim = tree[i][j]
                i_max, j_max = i, j

    tree[i_max][j_max] = tree[j_max][i_max] = 0


def cluster(cl):
    change = False
    for i in range(n):
        for j in range(n):
            if tree[i][j] != 0:
                clust_pnt[i] = clust_pnt[j] = cl
                tree[i][j] = tree[j][i] = 0
                change = True
    return change


# число вершин в графе
n = 5

# число кластеров
k = 2

weight = [[0 for i in range(n)] for i in range(n)]

for i in range(0, n):
    for j in range(i+1, n):
        weight[i][j] = numpy.random.randint(1, 100)
        weight[j][i] = weight[i][j]

tree = [[0 for i in range(n)] for i in range(n)]
connect_pnt = [0 for i in range(n)]

first_connection()

while 0 in connect_pnt:
    link_all()

for i in range(k-1):
    delete_connection()

clust_pnt = [0 for i in range(n)]

for i in range(k-1):
    flag = True
    while flag:
        flag = cluster(i)
