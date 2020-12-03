from typing import Callable
import pygame

# Интерактивное окно, выполняющее действия в цикле.
class InteractiveWindow:

    # window_width - ширина окна
    # window_height - высота окна
    def __init__(self, window_width: int, window_height: int):
        self._window = pygame.display.set_mode((window_width, window_height))

    # Запустить цикл, на каждой итерации выполняя действие game_loop_action
    def run(self, game_loop_action: Callable[[pygame.surface.Surface, pygame.event.Event], None]):
        pygame.init()
        self._window.fill((64, 64, 64))
        pygame.display.update()

        continue_game_loop = True
        while continue_game_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continue_game_loop = False

                game_loop_action(self._window, event)
                pygame.display.update()

        pygame.quit()