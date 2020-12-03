import pygame
import sklearn.svm as svm
import numpy as np

from interactive_window import InteractiveWindow
from button import Button
from point_type import PointType

point_coordinates = []
point_types = []

# Выполнить одну итерацию.
def perform_loop_action(
        window: pygame.surface.Surface,
        event: pygame.event.Event):

    # Отрисовать точку в окне.
    def print_point(current_event, point_type: PointType):
        color = (255, 0, 0) if point_type == PointType.First else (0, 255, 0)
        pygame.draw.circle(window, color, current_event.pos, 5)

    if event.type == pygame.MOUSEBUTTONDOWN:
        current_point_type = PointType.First \
            if event.button == Button.LeftClick.value \
            else PointType.Second

        print_point(event, current_point_type)

        point_coordinates.append(event.pos)
        point_types.append(current_point_type.value)

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

        clf = svm.SVC(kernel='linear', C=1.0)
        clf.fit(point_coordinates, point_types)

        a = clf.coef_[0][0]
        b = clf.coef_[0][1]
        c = clf.intercept_

        x = np.linspace(0, window.get_width(), 2)
        y = (-1 * c - a * x) / b

        pygame.draw.line(window, (0, 0, 0), [x[0], y[0]], [x[1], y[1]], 2)


def main():
    interactive_window = InteractiveWindow(1280, 720)
    interactive_window.run(perform_loop_action)


if __name__ == "__main__":
    main()
