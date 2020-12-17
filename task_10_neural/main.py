import pygame

from colors import Colors
from digit_recognizer import DigitRecognizer
from mouse_button import MouseButton


def main():
    screen = pygame.display.set_mode((280, 280))
    digit_recognizer = DigitRecognizer()

    while True:
        for event in pygame.event.get():

            if pygame.mouse.get_pressed(num_buttons = MouseButton.Left.value)[0]:
                position = pygame.mouse.get_pos()
                pygame.draw.circle(screen, Colors.white, (position[0], position[1]), 8)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == MouseButton.Right.value:
                recognizing_result_array = digit_recognizer.recognize_digit(screen)
                print(recognizing_result_array)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen.fill(Colors.black)

            elif event.type == pygame.QUIT:
                pygame.quit()
                break

        pygame.display.update()


if __name__ == "__main__":
    main()