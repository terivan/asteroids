from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):

    def __init__(self, x, y, radius=SHOT_RADIUS) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color='white',
            center = self.position,
            radius = self.radius,
            width=2)

    def update(self, dt):
        self.position += self.velocity*dt
