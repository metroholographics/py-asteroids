import sys
import pygame 
from constants import *
from circleshape import *
from player	import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
	pygame.init()

	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("py-asteroids")

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	dt = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updateable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.check_collision(player):
				sys.exit("Game over!")

			for bullet in shots:
				if asteroid.check_collision(bullet):
					asteroid.split()
					bullet.kill()

		
		screen.fill("black")

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()