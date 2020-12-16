from scipy.cluster.vq import kmeans2
from sklearn.linear_model import LogisticRegression
from numpy import (linspace, meshgrid)
from plotly import graph_objects

from point_generator import PointGenerator

def main():
    points = PointGenerator.generate_random_points(100)

    coordinates_array = list(map(lambda point: [point.x, point.y, point.z], points))
    _, label = kmeans2(coordinates_array, 2)
    colors = [{0: 'green', 1: 'red'}[l] for l in label]

    algorithm = LogisticRegression()
    algorithm.fit(coordinates_array, label)

    plane_func = lambda local_x, local_y: \
        (-algorithm.intercept_[0] - algorithm.coef_[0][0] * local_x - algorithm.coef_[0][1] * local_y) \
        / algorithm.coef_[0][2]

    space_coordinates = linspace(0, 100, 100)
    x_axis, y_axis = meshgrid(space_coordinates, space_coordinates)

    plot = graph_objects.Figure()

    plot.add_trace(graph_objects.Scatter3d(
        x=list(map(lambda point: point.x, points)),
        y=list(map(lambda point: point.y, points)),
        z=list(map(lambda point: point.z, points)),
        mode='markers',
        marker=dict(color=colors)))

    plot.add_trace(graph_objects.Surface(x=x_axis, y=y_axis, z=plane_func(x_axis, y_axis)))
    plot.show()

if __name__ == "__main__":
    main()