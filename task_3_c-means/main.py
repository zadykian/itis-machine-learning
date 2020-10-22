from matplotlib import pyplot
import numpy
import pandas


def get_dist2(list1, list2):
    return sum((i - j) ** 2 for i, j in zip(list1, list2))


class CMeansAlgorithm:

    def __init__(self, dataset):
        self.dataset = dataset

        self.n_clusters = 3
        self.fuzzy_c = 0.4
        self.cut_param = 0.9
        self.max_iter_num = 100
        self.tolerance = 0.01

        self.dist = numpy.zeros((self.dataset.shape[0], self.n_clusters))
        self.centroids = dataset[numpy.random.choice(dataset.shape[0], size=self.n_clusters, replace=False)]
        self.labels = numpy.array([])

    def distribute_data(self):
        self.dist = numpy.array([[get_dist2(i, j) for i in self.centroids] for j in self.dataset])

        self.result = (1 / self.dist) ** (1 / (self.fuzzy_c - 1))
        self.result = (self.result / self.result.sum(axis=1)[:, None])

        self.result[numpy.isnan(self.result)] = 1

    def recalculate_centroids(self):
        self.centroids = self.result.T.dot(self.dataset) / self.result.sum(axis=0)[:, None]

    def perform_clustering(self):
        current_iteration = 1

        while current_iteration < self.max_iter_num:
            prev_centroids = numpy.copy(self.centroids)
            self.distribute_data()
            self.recalculate_centroids()
            if max([get_dist2(i, k) for i, k in zip(self.centroids, prev_centroids)]) < self.tolerance:
                break

            current_iteration += 1

    def get_labels(self):
        for row in self.result:
            is_in = False
            for elem in row:
                if not is_in and elem > self.cut_param:
                    is_in = True
            if is_in:
                index = numpy.argmax(row) + 1
            else:
                index = 0
            self.labels = numpy.append(list(self.labels), index).astype(int)


def main():
    dataset = pandas.read_csv("data_set.csv")[['abscissa', 'ordinate']].values

    algorithm = CMeansAlgorithm(dataset)
    algorithm.perform_clustering()
    algorithm.get_labels()

    colors = numpy.array(['green', 'red', 'blue', 'yellow', 'brown'])

    pyplot.scatter(dataset[:, 0], dataset[:, 1], color=colors[algorithm.labels])
    pyplot.show()


if __name__ == "__main__":
    main()
