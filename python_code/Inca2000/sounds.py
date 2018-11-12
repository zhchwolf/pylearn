import pygame
FREQ = 22050   # same as audio CD
BITSIZE = -8  # unsigned 16 bit
CHANNELS = 1   # 1 == mono, 2 == stereo
BUFFER = 8  # audio buffer size in no. of samples
try:
	pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
except pygame.error:
	print >>sys.stderr, "Could not initialize sound system: %s" % exc
def playsound(n, l=0):
	sound[n].stop()
	sound[n].play(l)

def stopsound(n):
	sound[n].stop()

def playsong(n):
	pygame.mixer.music.load("music/" + n + ".ogg")
	pygame.mixer.music.set_volume(0.4)
	pygame.mixer.music.play(-1)

sound = {}
sound["swoosh1"] = pygame.mixer.Sound("sounds/swoosh1.wav")
sound["gun1"] = pygame.mixer.Sound("sounds/gun1.wav")
sound["step1"] = pygame.mixer.Sound("sounds/step1.wav")
sound["reload1"] = pygame.mixer.Sound("sounds/reload1.wav")
sound["ready1"] = pygame.mixer.Sound("sounds/ready1.wav")
sound["emptyclip1"] = pygame.mixer.Sound("sounds/emptyclip1.wav")
sound["aiming"] = pygame.mixer.Sound("sounds/aiming.wav")
sound["dead"] = pygame.mixer.Sound("sounds/dead.wav")
sound["restart"] = pygame.mixer.Sound("sounds/restart.wav")
sound["restart"].set_volume(0.4)

for i in range(12):
	sound["barf" + str(i)] = pygame.mixer.Sound("sounds/barfs/" + str(i) + ".wav")
	sound["barf" + str(i)].set_volume(0.8)
