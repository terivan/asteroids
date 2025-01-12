import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def collision_detection(self, circle):
        return pygame.math.Vector2.distance_squared_to(self.position,
            circle.position) <= self.radius + circle.radius



    def update(self, dt):
        # sub-classes must override
        pass
