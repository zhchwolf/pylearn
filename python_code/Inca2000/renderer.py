from entities import *
from random import *

class Tut(object):
	def __init__(self):
		self.rect = pygame.Rect(0, 64+32 + 16, 200, 64)
		self.image = sprites["tut"][0]
	def update(self):
		pass
tut = Tut()

class Inca(object):
	def __init__(self):
		self.rect = pygame.Rect(0, 0, 200, 64)
		self.image = sprites["inca"][0]
	def update(self):
		pass
inca = Inca()

def render(screen):
	for layer in layers:
		for entity in layer:
			entity.update()
			if entity.visable:
				if player.shake:
					r1 = randint(-1, 1)
					r2 = randint(-1, 1)
				else:
					r1 = 0
					r2 = 0
				screen.blit(entity.image, (entity.rect.x+r1, entity.rect.y+r2))
	screen.fill((0,0,0), (0, 0, 200, 32))
	screen.fill((0,0,0), (0, 160-64, 200, 64))
	screen.blit(tut.image, tut.rect)
	screen.blit(inca.image, inca.rect)
	
