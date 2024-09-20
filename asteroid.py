import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"grey",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        angle1 = self.velocity.rotate(random_angle)
        angle2 = self.velocity.rotate(-random_angle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        asteroidSmall1 = Asteroid(self.position.x,self.position.y,newRadius)
        asteroidSmall2 = Asteroid(self.position.x,self.position.y,newRadius)

        asteroidSmall1.velocity = angle1 * 1.2
        asteroidSmall2.velocity = angle2 * 1.2
        

