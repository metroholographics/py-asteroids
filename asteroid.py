import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
	def __init(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)
		if self.position.y < 0:
			self.position.y = SCREEN_HEIGHT - self.position.y
		if self.position.y > SCREEN_HEIGHT:
			self.position.y = 0 + self.position.y
		if self.position.x < 0:
			self.position.x = SCREEN_WIDTH - self.position.x
		if self.position.x > SCREEN_WIDTH:
			self.position.x = 0 + self.position.x

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		rand_angle = random.uniform(20, 50)
		dir_1 = self.velocity.rotate(rand_angle)
		dir_2 = self.velocity.rotate(-rand_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS

		new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid_1.velocity = dir_1 * 1.2
		new_asteroid_2.velocity = dir_2 * 1.2



