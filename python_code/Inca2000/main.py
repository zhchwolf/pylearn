#! /usr/bin/env python

import os
import pygame


os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("Inca2000, Wizardsoftopaz.com, v0.001")
clock = pygame.time.Clock()

res = (800, 640) #Actual window resolution.
window = pygame.display.set_mode(res) # Actual window display.
gscreen = pygame.Surface((200, 160)) # Surface for scale-blit to window display.

from renderer import *
from cutscenes import *

playLogo(res, window)
start()
#player.move(1)
playsong("permet")
running = True
while running:
	player.speed = 2
	clock.tick(30) # Tick so it runs the same(ish) on multiple hardware.
	# Basic single keystroke input.
	for e in pygame.event.get():  
		if e.type == pygame.QUIT:
			running = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
			running = False
		if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
			player.fire()

		if e.type == pygame.KEYDOWN and e.key == pygame.K_LCTRL:
			player.reload()
		if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
			if player.alive == False:
				start()
				Flash()
	key = pygame.key.get_pressed() # 
	if key[pygame.K_LEFT]:
		player.dir = 0
	if key[pygame.K_RIGHT]:
		player.dir = 1
	player.move(player.dir)

	if key[pygame.K_UP]:
		player.cover1()
	else:
		player.leave1()

	if key[pygame.K_DOWN]:
		player.cover2()
	else:
		player.leave2()

	render(gscreen) # Update logic and render screen, done by renderer.py. Blit to virtual surface.
	pygame.transform.scale(gscreen, res, window) # Scale virtual surface to fit window. 
	pygame.display.flip() # Update the window and repeat.

	if player.wx > 6:
		print("You won the pre-pre-pre-alpha version of this game. Congraturations! Tell me the secret password " + secretpassword)
		running = False

print("Bye!")
