import pygame, sys, os
from Model import *


class Player_action:
	WALK_LEFT=0
	WALK_RIGHT=1

class Direction:
	LEFT = 0
	RIGHT = 1

class Player:
	def __init__(self):
		self.animations = [None]*2
		self.animations[0] = Animation(pygame.image.load("sprite1.png"), (64,64), 2, 15)
		self.animations[1] = Animation(pygame.image.load("sprite2.png"), (64,64), 2, 15)
		self.direction = Direction.LEFT

	def get_image(self):
		if self.direction == Direction.LEFT:
			return self.animations[0].get_image()
		return self.animations[1].get_image()

class Animation:
	def __init__(self, image, dim, num_images, ticks):
		self.frames = []
		for img in range (0, num_images):
			self.frames.append(image.subsurface(pygame.Rect(img*dim[0], 0, dim[0], dim[1])))
		self.ticks = ticks
		self.cnt = 0
		self.cur_frame = 0
		self.num_images = num_images


	def tick(self):
		self.cnt += 1
		if(self.cnt > self.ticks):
			self.cnt = 0
			self.cur_frame += 1

	def get_image(self):
		self.tick()
		return self.frames[self.cur_frame % self.num_images]

def main():
	pygame.init()
	
	#time is specified in milliseconds
	#fixed simulation step duration
	step_size = 20
	#max duration to render a frame	
	max_frame_time = 100
	now = pygame.time.get_ticks()
	
	img = pygame.image.load("sprite1.png") 
	anim = Animation(img, (64,64) ,2,15)
	
	screen = pygame.display.set_mode((800, 600), 0, 32)
	active = True	
	p = Player()
	while(active):
	
		events = pygame.event.get()
		for e in events:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_SPACE:
					active = False
				if e.key == pygame.K_LEFT:
					p.direction = Direction.LEFT
				if e.key == pygame.K_RIGHT:
					p.direction = Direction.RIGHT

		T = pygame.time.get_ticks()
   
		#if elapsed time since last frame is too long...
		now = T - step_size
	
		while(T-now >= step_size):
			now += step_size
			#logics
		else:
			pygame.time.wait(10)
	
		#render
		BG_COLOR = 150, 150, 50
		screen.fill(BG_COLOR)
	#	screen = pygame.display.get_surface()
	#	fst = img.subsurface(pygame.Rect (0,0,64,64))
	#	snd = img.subsurface(pygame.Rect (64,0,64,64))
		
		screen.blit(p.get_image(), (0,0))

		pygame.display.flip()
	 
if __name__ == "__main__":
	main()

