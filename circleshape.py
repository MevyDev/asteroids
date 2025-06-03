import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def check_collisions(self, target):
        distance = pygame.Vector2.distance_to(self.position, target.position)
        radius_sum = self.radius + target.radius
        if distance < radius_sum:
            return True
        return False
