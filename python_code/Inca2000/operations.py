from random import *
import pygame

# Layers for entities. Barebones render-sorting.
layers = []
for i in range(10):
	layers.append([])
# List of random numbers.
r = []
for i in range(16):
	r.append(0)

# Scramble all random numbers.
def calcRands():
	global r
	for i in range(16):
		r[i] = randint(0, 255)

# Change color in image to diferent color.
def changeColor(image, oldColor, newColor):
	b = image.copy()
	image_pixel_array = pygame.PixelArray(b)
	image_pixel_array.replace(oldColor, newColor)
	return b

# Basic collision detection.
def hitTest(target0, target1):
	if target0.rect.colliderect(target1.hitrect):
		return True
	else:
		return False

# Delete entity.
def removeEntity(target):
	for a, layer in enumerate(layers):
		for b, entity in enumerate(layer):
			if entity == target:
				del layers[a][b]

def randomColor():
	r0 = choice((0, 128, 255))
	pos = ((r0, 0,0), (0, r0, 0), (0, 0, r0), (0,r0, r0), (r0, r0, 0), (r0, 0, r0))
	d = choice(pos)
	return d
