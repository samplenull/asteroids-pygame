from circleshape import CircleShape
import constants
import pygame
from logger import log_event
from random import uniform


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", self.position, self.radius, constants.LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        new_angle = uniform(20, 50)
        ast1_vector = self.velocity.rotate(new_angle)
        ast2_vector = self.velocity.rotate(-new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)  # type: ignore
        ast1.velocity = ast1_vector * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)  # type: ignore
        ast2.velocity = ast2_vector * 1.2
