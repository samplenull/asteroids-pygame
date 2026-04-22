import pygame
import constants
import sys
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # type: ignore
    Asteroid.containers = (updatable, drawable, asteroids)  # type: ignore
    AsteroidField.containers = updatable  # type: ignore
    Shot.containers = (updatable, drawable, shots)  # type: ignore

    asteroid_field = AsteroidField()
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt / 1000)
        for ast in asteroids:
            if player.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for s in shots:
                if s.collides_with(ast):
                    log_event("asteroid_shot")
                    s.kill()
                    ast.split()
                    break

        for obj_upd in drawable:
            obj_upd.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)


if __name__ == "__main__":
    main()
