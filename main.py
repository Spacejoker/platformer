import pygame, sys, os

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
		self.rundir = None
		self.pos = (0,500)
		self.acceleration = 0
		self.speed = 0

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
			print e
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_SPACE:
					active = False

		
		left_pressed = pygame.key.get_pressed()[pygame.K_LEFT]
		right_pressed =	pygame.key.get_pressed()[pygame.K_RIGHT]
		if left_pressed != right_pressed:
			if left_pressed:
				p.rundir = Direction.LEFT
			else:
				p.rundir = Direction.RIGHT
		else:
			p.rundir = None

		T = pygame.time.get_ticks()
   
		#if elapsed time since last frame is too long...
		now = T - step_size
	
		while(T-now >= step_size):
			now += step_size
			#logics
			logic(p)
		else:
			pygame.time.wait(10)
	
		#render
		BG_COLOR = 50, 50, 50
		screen.fill(BG_COLOR)
		screen.blit(p.get_image(), p.pos)

		pygame.display.flip()
	
def logic(p):
	if p.rundir == None:
		p.acceleration = 0
		p.speed /= 2
		if(p.speed < 0.2):
			p.speed = 0
	elif p.rundir == Direction.LEFT:
		p.direction = Direction.LEFT
		p.acceleration = -5
		if p.speed > 0:
			p.speed /= 2
	elif p.rundir == Direction.RIGHT:
		p.direction = Direction.RIGHT
		p.acceleration = 5
		if p.speed < 0:
			p.speed /= 2

	p.speed += 0.1 * p.acceleration
	p.speed = max(-4.0, p.speed)
	p.speed = min(4.0, p.speed) 
	p.pos = (p.pos[0] + p.speed, p.pos[1])

if __name__ == "__main__":
	main()

