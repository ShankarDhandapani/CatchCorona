import pygame, sys, random
pygame.init()

# get window....
window_size = (1000, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Corona Catch")


# get screen....
screen_color = (0, 255, 0)
screen = pygame.display.get_surface()

# Adding Background Music
pygame.mixer.music.load(r'C:\Users\Shankar\Desktop\PyGame\Sound\bg.wav')
pygame.mixer.music.play(-1)


# Adding Image
doctor_image = pygame.transform.scale((pygame.image.load(r'C:\Users\Shankar\Desktop\PyGame\Image\Doctor.jpg').convert_alpha()),(50,50))
corona_image = pygame.transform.scale((pygame.image.load(r'C:\Users\Shankar\Desktop\PyGame\Image\Corona.jpg').convert_alpha()),(70,50))

# doctor start....
doc_x = 500
doc_y = 300

# corona start....
corona_x = random.randint(1, 500)
corona_y = random.randint(1, 300)

# init the score....
score = 0

# setup the font to text....
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Score : '+str(score), False, (0, 0, 0))

#colors
screen_colors=[(15, 192, 252),(123, 29, 175),(255, 47, 185),(212, 255, 71)]

# start the game clock for timer to auto refresh....
clock = pygame.time.Clock()
while True: #Game loop....
	screen_color = screen_colors[random.randint(0,3)]
	for event in pygame.event.get(): # Event loop....

		# Quit if closed....
		if event.type == pygame.QUIT: 
			pygame.quit()
			sys.exit()

		# Quit if q pressed....
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
		
		# Quit if out of boundary....
		if doc_x > 1000 or doc_y > 600 or doc_x < 0 or doc_y < 0: 
			pygame.quit()
			sys.exit()
	
		# If Doctor kill the corona....
		if doc_x in range(corona_x-50, corona_x+50) and doc_y in range(corona_y-50, corona_y+50):
			corona_x = random.randint(1, 500)
			corona_y = random.randint(1, 300)
			score += 1

	# Continuous pressing of keys....
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: doc_y -= 5
	if pressed[pygame.K_DOWN]: doc_y += 5
	if pressed[pygame.K_LEFT]: doc_x -= 5
	if pressed[pygame.K_RIGHT]: doc_x += 5	

	# Refreshing the Screen for every timer....
	screen.fill(screen_color)
	'''Create the Corona'''
	window.blit(corona_image,(corona_x, corona_y))
	'''Create the Doctor'''
	window.blit(doctor_image,(doc_x, doc_y))
	'''Display the Score'''
	textsurface = myfont.render('Score : '+str(score), False, (0, 0, 0))
	screen.blit(textsurface,(0,0))
	'''Update the screen'''
	pygame.display.update()
	clock.tick(50+score*5)
