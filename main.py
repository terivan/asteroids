# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroid import Asteroid
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    if ('SCREEN_WIDTH' not in globals()) or ('SCREEN_HEIGHT' not in globals()):
        raise pygame.error("Screen width or heigt undefined")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x,y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    while True:
        screen.fill(color='black')
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            collision = a.collision_detection(player)
            if collision:
                print("Game over!")
                return

        for a in asteroids:
            for b in shots:
                collision = a.collision_detection(b)
                if collision:
                    a.split()
                    b.kill()
        for d in drawable:
            d.draw(screen)

        # player.draw(screen)
        pygame.display.flip()
        # player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000




    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
