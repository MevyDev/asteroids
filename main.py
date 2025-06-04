import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, FPS_CAP


def game_over():
    print("GAME OVER!")
    exit()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Bullet.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for upd in updatable:
            upd.update(dt)

        for draw in drawable:
            draw.draw(screen)

        for asteroid in asteroids:
            if player.check_collisions(asteroid):
                game_over()

        pygame.display.flip()
        dt = game_clock.tick(FPS_CAP) / 1000


if __name__ == "__main__":
    main()
