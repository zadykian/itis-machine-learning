import pygame
import sklearn.svm as svm
import numpy as np
from enum import Enum

from interactive_window import InteractiveWindow
from button import Button

class PointType(Enum):
    First = 1
    Second = 2

coordinates = []
classification = []

def perform_game_action(window: pygame.surface.Surface, event: pygame.event.Event):

    def draw_circle(coordinates_array, classification_array, current_event, current_class):
        color = (255, 0, 0) if current_class == 1 else (0, 255, 0)
        pygame.draw.circle(window, color, current_event.pos, 5)
        coordinates_array.append(current_event.pos)
        classification_array.append(current_class)

    if event.type == pygame.MOUSEBUTTONDOWN:

        if event.button == Button.LeftClick.value:
            draw_circle(coordinates, classification, event, PointType.First.value)
        elif event.button == Button.RightClick.value:
            draw_circle(coordinates, classification, event, PointType.Second.value)

    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

        clf = svm.SVC(kernel='linear', C=1.0)
        clf.fit(coordinates, classification)

        a = clf.coef_[0][0]
        b = clf.coef_[0][1]
        c = clf.intercept_

        x = np.linspace(0, window.get_width(), 2)
        y = (-1 * c - a * x) / b

        pygame.draw.line(window, (0, 0, 0), [x[0], y[0]], [x[1], y[1]], 2)


def main():
    interactive_window = InteractiveWindow(1280, 720)
    interactive_window.run(perform_game_action)


if __name__ == "__main__":
    main()
