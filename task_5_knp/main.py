import sys
import numpy


class KnpAlgorithm:
    
    # self.n - число вершин в графе
    # self.k - число кластеров
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k

    # Найти ребро в графе, имеющее минимальный вес, добавить его в tree
    def first_connection(self):
        minim = self.weight[0][1]
        i_min, j_min = 0, 1
    
        for i in range(self.n):
            for j in range(i+1, self.n):
                if minim > self.weight[i][j]:
                    minim = self.weight[i][j]
                    i_min, j_min = i, j
    
        self.tree[i_min][j_min] = minim
        self.tree[j_min][i_min] = minim
    
        self.weight[i_min][j_min] = sys.maxsize
        self.weight[j_min][i_min] = sys.maxsize
    
        self.connect_pnt[i_min] = 1
        self.connect_pnt[j_min] = 1

    # Добавить в tree вершину, имеющую минимальный путь до существующего дерева
    def link_all(self):
        minim = sys.maxsize
        i_min, j_min = None, None
    
        for i in range(self.n):
            if self.connect_pnt[i] == 1:
                for j in range(0, self.n):
                    if self.connect_pnt[j] == 0:
                        if minim > self.weight[i][j]:
                            minim = self.weight[i][j]
                            i_min, j_min = i, j

        self.tree[i_min][j_min] = minim
        self.tree[j_min][i_min] = minim
        self.weight[i_min][j_min] = self.weight[j_min][i_min] = sys.maxsize
        self.connect_pnt[i_min] = self.connect_pnt[j_min] = 1
    
    # Удалить из tree ребро с наибольшим весом
    def delete_connection(self):
        maxim = 0
        i_max, j_max = 0, 0
    
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.tree[i][j] > maxim:
                    maxim = self.tree[i][j]
                    i_max, j_max = i, j
    
        self.tree[i_max][j_max] = self.tree[j_max][i_max] = 0
    
    def cluster(self, cl):
        change = False
        for i in range(self.n):
            for j in range(self.n):
                if self.tree[i][j] != 0:
                    self.clust_pnt[i] = self.clust_pnt[j] = cl
                    self.tree[i][j] = self.tree[j][i] = 0
                    change = True
        return change
    
    def perform_clustering(self):
        self.weight = [[0 for i in range(self.n)] for i in range(self.n)]

        for i in range(0, self.n):
            for j in range(i + 1, self.n):
                self.weight[i][j] = numpy.random.randint(1, 100)
                self.weight[j][i] = self.weight[i][j]

        self.tree = [[0 for i in range(self.n)] for i in range(self.n)]
        self.connect_pnt = [0 for i in range(self.n)]

        self.first_connection()

        while 0 in self.connect_pnt:
            self.link_all()

        for i in range(self.k - 1):
            self.delete_connection()

        self.clust_pnt = [0 for i in range(self.n)]

        for i in range(self.k):
            flag = True
            while flag:
                flag = self.cluster(i)


def main():
    algorithm = KnpAlgorithm(5, 2)
    algorithm.perform_clustering()
    print(algorithm.clust_pnt)


if __name__ == "__main__":
    main()
