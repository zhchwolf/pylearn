import pygame
from operations import *
from images import *
from sounds import *
from random import *

#For display of text in .TTF format.
fontsize = 16
font = pygame.font.Font("fonts/pcsenior.ttf", fontsize)
class Text(object):
	def __init__(self, text, x, y, color=(128,128,128)):
		layers[10].append(self)
		self.x = x
		self.y = y
		self.ct = 0
		self.time = 1
		self.image = font.render(text, 0, color, (0, 0, 0))
		self.size = font.size(text)
		self.inf = inf

	def update(self, text):
		self.ct += 1
		if self.ct is self.time:
			removeEntity(self)

#Basic parameters that all entities share.
class Entity(object):
	def __init__(self, x, y, s, l):
		layers[l].append(self)
		self.visable = True
		self.rect = pygame.Rect(x, y, s, s)
		self.image = pygame.Surface((s, s))
		self.image.fill((255, 255, 255))

#Player class.
class Actor(Entity):
	def __init__(self,wx, x, char="enemy1", enemy=True):
		if char == "player":
			Entity.__init__(self, x, 65, 32, 5)
			self.dir = 1
		else:
			Entity.__init__(self, x, 67, 32, 6)
			self.dir = randint(0,1)
		self.state = "idle"
		self.xstate = "idle"
		self.skincolor = choice(((128, 64, 0), (128, 0,0), (255, 128, 128), (255, 64, 0)))
		self.sweatcolor = choice(( ((255, 0, 0), (128, 0, 0)), ((0, 255, 0), (0, 128, 0)), ((0, 0, 255), (0, 0, 128)),
			((255, 0, 255), (128, 0, 128)), ((0, 255, 255), (0, 128, 128)), ((255, 255, 0), (128, 128, 0))))
		self.speed = 1
		self.alive = True
		self.wx = wx

		self.frame = 0	
		self.a = 0
		self.framerate = 10
		self.prev = None
		self.enemy = enemy
		self.distance = 200
		self.clipsize = 4
		self.currentclip = self.clipsize
		self.backlash = 2
		self.char = char
		self.img = sprites[self.char][self.frame].copy()
		self.image = changeColor(self.img, (255, 128, 128), self.skincolor)
		self.shake = False
	def tic(self):
			self.a += 1
			if self.a == self.framerate:
				self.a = 0
				self.frame += 1
	def move(self, d):
		if self.state == "idle":
			self.state = "moving"
			self.framerate = 10
			if d == 0:
				if self.prev == 1:
					self.rect.x -= 16
				self.prev = d
				self.dir = d
				self.rect.x -= self.speed
			elif d == 1:
				if self.prev == 0:
					self.rect.x += 16
				self.prev = d
				self.dir = d
				self.rect.x += self.speed

			self.a += self.speed
			if self.a == self.framerate:
				self.a = 0
				self.frame += 1
				if self.frame == 1 or self.frame == 4:
					if self.wx == player.wx:
						playsound("step1")

				if self.frame > 5:
					self.frame = 0
			self.state = "idle"

			if self.wx == 0 and self.rect.x < 50:
				self.rect.x += self.speed


	def cover1(self):
		if self.state == "idle" or self.state == "walking":
			self.framerate = 2
			self.a = 0
			self.frame = 18
			self.state = "gocover1"
			playsound("swoosh1")
			if self.frame == 18:
				self.rect.y -= 1
			
	def leave1(self):
		if self.state == "gocover1":
			playsound("swoosh1")
			self.rect.y += 1
			self.frame = 20
			self.framerate = 2
			self.a = 0
			self.state = "leavecover1"

	def cover2(self):
		if self.state == "idle" or self.state == "walking":
			self.framerate = 2
			self.a = 0
			self.frame = 12
			self.state = "gocover2"
			playsound("swoosh1")
			if self.frame == 12:
				self.rect.y += 1
			
	def leave2(self):
		if self.state == "gocover2":
			playsound("swoosh1")
			self.rect.y -= 1
			self.frame = 14
			self.framerate = 2
			self.a = 0
			self.state = "leavecover2"

	def reload(self):
		if self.state == "idle" or self.state == "walking":
			self.framerate = 3
			self.state = "reload"
			self.frame = 23
			self.a = 0
			playsound("reload1")

	def fire(self):
		global secretpassword
		if self.currentclip > 0:
			if self.state == "idle" or self.state == "walking":
				if self.enemy:
					if player.alive:
						selfTotalX = self.wx * 200 + self.rect.centerx
						itTotalX = player.wx * 200 + player.rect.centerx
						self.distance = abs(selfTotalX - itTotalX)
						closestX = self.distance
						if self.aim == "m" and player.state != "gocover1" and player.state != "gocover2":
							player.die()
							playsound("dead", -1)
							URDED()
						elif (self.aim == "r" and player.state == "gocover1") or player.state == "leavecover1":
							player.die()
							playsound("dead", -1)
							URDED()
						elif (self.aim == "l" and player.state == "gocover2") or player.state == "leavecover2":
							player.die()
							playsound("dead", -1)
							URDED()
					
						else: 
							closestX = 200
							self.xstate = "idle"
							self.state = "idle"
					else:
						self.xstate = "idle"
						self.state = "idle"
				else:
					closestEnt = None
					closestX = 200
					for i, ent in enumerate(layers[6]):
						if ent.wx == self.wx:
							if ent.alive:
								no = False
								selfTotalX = self.wx * 200 + self.rect.centerx
								itTotalX = ent.wx * 200 + ent.rect.centerx
								self.distance = abs(selfTotalX - itTotalX)
								if self.distance < 200 and self.distance > 28:
									if (self.dir == 0 and itTotalX < selfTotalX) or (self.dir == 1 and itTotalX > selfTotalX):
										if self.distance < closestX:
											closestX = self.distance
											closestEnt = ent
					if closestEnt != None:
						if closestEnt.alive:
							closestEnt.die()
				self.framerate = 3
				self.state = "firing"
				self.frame = 6
				self.a = 0
				self.shake = True
				secretpassword = "'DoublesDigital'"
				if self.dir == 0:
					self.rect.x += self.backlash
				else:
					self.rect.x -= self.backlash
				playsound("gun1")
				try:
					if self.enemy:
						if self.aim == "l":
							Bullet(self.rect, self.dir, closestX, 8)
						if self.aim == "m":
							Bullet(self.rect, self.dir, closestX, 7)
						if self.aim == "r":
							Bullet(self.rect, self.dir, closestX, 4)
					else:
						Bullet(self.rect, self.dir, closestX, 2)
				except:
					pass
				Flash()
				self.currentclip -= 1
		else:
			if self.enemy:
				self.reload()

			elif self.state == "idle" or self.state == "walking":
				playsound("emptyclip1")
				self.frame = choice((10, 9, 0, 11))
				self.state = "idle"

	def die(self):
		self.alive = False
		self.a = 0
		self.frame = 30
		self.state = "dying"
		self.framerate = 8
		for i in range(20):
			Gore(self.rect)
		if self.enemy:
			playsound("barf" + str(randint(3,11)))
		else:
			playsound("barf" + str(randint(0,2)))
		stopsound("aiming")
		

	def update(self):
		if self.enemy:
			if self.wx == player.wx:
				self.visable = True
			else:
				self.visable = False
			if self.visable:
				if self.xstate == "idle" or self.xstate == "random_walking" :
					if randint(0,100) == 0:
						if self.xstate == "random_walking":
							self.xstate = "idle"
						else:
							self.xstate = "random_walking"
					if randint(0,100) == 0:
						if self.dir == 0: self.dir = 1
						elif self.dir == 1: self.dir = 0
					if player.alive:
						selfTotalX = self.wx * 200 + self.rect.centerx
						itTotalX = player.wx * 200 + player.rect.centerx
						self.distance = abs(selfTotalX - itTotalX)
						if self.distance < 200:
							if (self.dir == 0 and selfTotalX > itTotalX) or (self.dir == 1 and selfTotalX < itTotalX):
								self.xstate = "aim"
								playsound("aiming")
								if player.state != "gocover1" and player.state != "leavecover1" and player.state != "gocover2" and player.state != "leavecover2":  
									self.aim = "m"
									Arrow(0, self.rect.centerx, self)
								elif player.state == "gocover1" or player.state == "leavecover1":
									self.aim = "r"
									Arrow(1, self.rect.centerx, self)
								elif player.state == "gocover2" or player.state == "leavecover2":
									self.aim = "l"
									Arrow(2, self.rect.centerx, self)
								self.a = 0
		if self.state == "firing":
			self.tic()
			if self.frame == 10 :
				self.shake = False
				self.state = "idle"
			if self.frame > 11:
				self.state = "idle"
				self.frame = 0
		elif self.state == "gocover1":
			if self.frame < 20:
				self.tic()
		elif self.state == "leavecover1":
			self.tic()
			if self.frame > 22:
				self.state = "idle"
		elif self.state == "gocover2":
			if self.frame < 14:
				self.tic()
		elif self.state == "leavecover2":
			self.tic()
			if self.frame > 16:
				self.state = "idle"
		elif self.state == "reload":
			self.tic()
			if self.frame == 25:
					playsound("ready1")
			elif self.frame > 28:
				self.currentclip = self.clipsize
				self.state = "idle"
		elif self.state == "dying":
			self.tic()
			if self.frame > 34:
				removeEntity(self)
		elif self.xstate == "aim":
			self.a += 1
			if self.a > randint(20,40):
				self.fire()
		if self.xstate == "random_walking":
			self.move(self.dir)
		if self.dir == 0:
			self.img = pygame.transform.flip(sprites[self.char][self.frame].copy(), True, False)
		else:
			self.img = sprites[self.char][self.frame].copy()

		if self.enemy:
			self.img = changeColor(self.img, (0, 128, 0), self.sweatcolor[1])
			self.img = changeColor(self.img, (0, 255, 0), self.sweatcolor[0])

		self.image = changeColor(self.img, (255, 128, 128), self.skincolor)
		try:
			if self.rect.x > 190:
				self.wx += 1
				self.rect.x = 0
				if self.enemy == False:
					background.swap()
			elif self.rect.x < -20:
				self.wx -= 1
				self.rect.x = 160
				if self.enemy == False:
					background.swap()
		except:
			pass

class Gore(Entity):
	def __init__(self, origin):
		Entity.__init__(self, origin.x + 8, 65, 8, 7)
		if randint(0,2) == 0:
			self.image = sprites["gore"][randint(0, 50)]
		else:		
			self.image = sprites["gore"][randint(50, 99)]
		self.dir = randint(0,1)
		self.a = 0
		self.framerate = randint(1,7)

		self.Yspeed = randint(0,3)
		self.Xspeed = randint(0,10)
	def update(self):
		self.a += 1
		if self.a == self.framerate:
			self.a = 0
			self.Yspeed += 1
			self.Xspeed -= 1
			self.rect.y += self.Yspeed
			if self.dir == 0:
				self.rect.x += self.Xspeed
			else:
				self.rect.x -= self.Xspeed

		if self.rect.y > 128:
			removeEntity(self)

class URDED(object):
	def __init__(self):
		layers[9].append(self)
		self.visable = True
		self.rect = pygame.Rect(0, 32, 64, 32)
		self.im = sprites["urded"][0]
		self.image = self.im
	def update(self):
		self.image = changeColor(self.im, (255, 255, 255), randomColor())
		if player.alive:
			removeEntity(self)

class Arrow(object):
	def __init__(self, t, x, owner):
		layers[8].append(self)
		self.visable = True
		self.rect = pygame.Rect(x+8, 40, 8, 8)
		self.im = sprites["arr"][t]
		self.img = self.im
		self.image = pygame.Surface((8,8))
		self.a = 0
		self.owner = owner
	def update(self):
		self.img = changeColor(self.im, (255, 255, 255), randomColor())
		self.image.fill((1,1,1))
		self.image.fill((0,0,0), (1,1,6,6))
		self.image.blit(self.img, (0,1))		
		self.a += 1
		if self.a > 30 or self.owner.alive == False:
			removeEntity(self)


class Flash(object):
	def __init__(self):
		layers[9].append(self)
		self.visable = True
		self.time = 0
		self.lifespan = 5
		self.rect = pygame.Rect(0, 32, 200, 64)
		self.image = pygame.Surface((200,64)) 
		self.image.fill((255,255,255))
	def update(self):
		if randint(0,4) == 0:
			self.image.fill((255,255,0))
		elif randint(0,4) == 0:
			self.image.fill((0,255,0))
		elif randint(0,4) == 0:
			self.image.fill((255,0,255))
		elif randint(0,4) == 0:
			self.image.fill((0,255,255))
		else:
			self.image.fill((255,0,0))
		self.time += 1
		if self.time > self.lifespan:
			removeEntity(self)
		self.image.set_alpha(255 - int((self.time * 50)))

class Bullet(object):
	def __init__(self, origin, d, length, layer):
		self.visable = True
		self.time = 0
		self.lifespan = 200
		self.length = length
		layers[layer].append(self)
		if d == 0:
			x = origin.x - self.length
		else:
			x = origin.x+26
			self.length -= 26
			
		self.rect = pygame.Rect(x, 74, 200, 64)
		try:
			self.image = pygame.Surface((self.length,1)) 
			self.image.fill((255,255,0))
		except:
			pass
	def update(self):
		self.time += 1
		if randint(0,4) == 0:
			self.image.fill((255,255,0))
		elif randint(0,4) == 0:
			self.image.fill((0,255,0))
		elif randint(0,4) == 0:
			self.image.fill((255,0,255))
		elif randint(0,4) == 0:
			self.image.fill((0,255,255))
		else:
			self.image.fill((255,0,0))
		if self.time > self.lifespan:
			removeEntity(self)
		self.image.set_alpha(255 - int((self.time * 20)))



class Background(object):
	def __init__(self):
		self.visable = True
		layers[0].append(self)
		self.rect = pygame.Rect(0, 32, 200, 64)
		self.image = sprites["bg"][player.wx]
	def update(self):
		pass
	def swap(self):
		self.image = sprites["bg"][player.wx]

player = Actor(0, 80, "player", False)

def start():
	playsound("restart")
	stopsound("dead")
	global layers, player, background
	for layer in layers:
		del layer[:]
	#Init classes.
	player.__init__(0, 80, "player", False)
	background = Background()
	player.reload()
	Actor(1, randint(64,164), "enemy1", True)
	Actor(1, randint(64,164), "enemy1", True)
	Actor(2, randint(64,164), "enemy1", True)
	Actor(2, randint(64,164), "enemy1", True)
	Actor(2, randint(64,164), "enemy1", True)
	Actor(2, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(3, randint(64,164), "enemy1", True)
	Actor(4, randint(64,164), "enemy1", True)
	Actor(4, randint(64,164), "enemy1", True)
	Actor(4, randint(64,164), "enemy1", True)
	Actor(4, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(5, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	Actor(6, randint(64,164), "enemy1", True)
	
	background.swap()

