import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEED_SCALING


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        small_velocity_1 = self.velocity.rotate(angle) * ASTEROID_SPEED_SCALING
        small_velocity_2 = self.velocity.rotate(-angle) * ASTEROID_SPEED_SCALING
        small_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, small_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, small_radius)

        new_asteroid_1.velocity = small_velocity_1
        new_asteroid_2.velocity = small_velocity_2
