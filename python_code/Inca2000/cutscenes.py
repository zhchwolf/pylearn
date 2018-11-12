import pygame
from images import *

def playLogo(res, window):
	clock = pygame.time.Clock()
	gscreen = pygame.Surface((100, 80))
	pygame.mixer.music.load('music/openinglogo.ogg')#load music
	pygame.mixer.music.play(1)
	playing = True
	c = 0
	d = 0
	dd = [28, 28, 28, 28, 55, 2, 2, 2, 
		10, 10, 10, 20, 20, 20, 3, 3,
		3, 3, 3, 3, 3, 3, 3, 120, 3,
		3, 3, 200, 0, 0, 0, 0]
	delay = dd[0]
	while playing is True:
		for e in pygame.event.get():  
			if e.type == pygame.KEYDOWN:
				playing = False
		clock.tick(60) # Tick so it runs the same speed on multiple hardware.

		ci = sprites["logo"][c].copy()
		gscreen.blit(ci, (0, 0))
		pygame.transform.scale(gscreen, res, window)
		pygame.display.flip()
		d += 1
		if d > delay:
			d = 0
			c += 1
			delay = dd[c]
			if c > 29:
				playing = False
