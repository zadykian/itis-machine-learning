import pygame
from enum import Enum

from colors import Colors
from digit_recognizer import DigitRecognizer

class Button(Enum):
    Left = 1
    Right = 3

def main():
    screen = pygame.display.set_mode((256, 256))
    digit_recognizer = DigitRecognizer()

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                break
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == Button.Right.value:
                    digit_recognizer.recognize_digit(screen)
            elif i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                screen.fill(Colors.black)

        position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            pygame.draw.circle(screen, Colors.white, (position[0], position[1]), 8)
        pygame.display.update()


if __name__ == "__main__":
    main()