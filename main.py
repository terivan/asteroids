# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()

    if ('SCREEN_WIDTH' not in globals()) or ('SCREEN_HEIGHT' not in globals()):
        raise pygame.error("Screen width or heigt undefined")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill(color='black')
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
