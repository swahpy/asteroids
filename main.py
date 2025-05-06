import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Create two groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # create group for asteroids
    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updateable, drawable)
    # group for asteroidfield
    AsteroidField.containers = (updateable,)
    asteroidfield = AsteroidField()
    # shots group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface.fill("black")
        for item in drawable:
            item.draw(surface)
        pygame.display.flip()
        for asteroid in asteroids_group:
            if player.collide(asteroid):
                print("Game Over!")
                sys.exit(1)
        for asteroid in asteroids_group:
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()
        passed = clock.tick(60)
        dt = passed / 1000
        updateable.update(dt)


if __name__ == "__main__":
    main()
