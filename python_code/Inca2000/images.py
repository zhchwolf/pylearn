import pygame  

def grabSpriteSheet(filename, w, h, **kwargs): #Originally written by Tom Eyerman, slightly altered.
	base_image = pygame.image.load(filename).convert()
	base_image.set_colorkey((111, 0, 111))
	sprite_width = w
	sprite_height = h
	columns = base_image.get_width() / w
	rows = base_image.get_height() / h
	current_row, current_column = kwargs.get('start', (0, 0))  
	end_row, end_column = kwargs.get('end', (rows - 1, columns - 1))  
	image_list = []  
	current_frame = pygame.Rect(0, 0, sprite_width, sprite_height)  
	while current_row <= end_row:  
		current_frame.top = sprite_height * current_row  
		while (current_row < end_row and current_column < columns) or (current_row == end_row and current_column <= end_column):  
			current_frame.left = sprite_width * current_column  
			image_list.append(base_image.subsurface(current_frame))
			current_column += 1  
		current_column = 0  
		current_row += 1
	return image_list

sprites = {}

sprites["player"] = grabSpriteSheet('images/player.png', 32, 32)
sprites["enemy1"] = grabSpriteSheet('images/enemy1.png', 32, 32)

sprites["gore"] = grabSpriteSheet('images/gore.png', 8, 8)

sprites["bg"] = grabSpriteSheet('images/bg1.png', 200, 64)
sprites["cover"] = grabSpriteSheet('images/cover.png', 8, 8)

sprites["tut"] = grabSpriteSheet('images/tut.png', 200, 37)
sprites["inca"] = grabSpriteSheet('images/inca2000.png', 200, 37)
sprites["urded"] = grabSpriteSheet('images/urded.png', 64, 32)

sprites["arr"] = grabSpriteSheet('images/arr.png', 8, 8)

sprites["logo"] = grabSpriteSheet('images/logo.png', 100, 80)
