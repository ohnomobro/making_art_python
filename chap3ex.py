import pygame
import pygame.gfxdraw
import random

pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

blue = (100, 0, 255)
black = (0, 0 ,0)
pink = (255, 100, 180)
green = (80, 255, 200)

running = True

def draw_flat_line(screen, x, y, length, color):
	for i in range(length):
		pygame.gfxdraw.pixel(screen, x + i, y, color)

def draw_vertical_line(screen, x, y, length, color):
	for i in range(length):
		pygame.gfxdraw.pixel(screen, x, y + i, color)

def draw_diagonal_line(screen, x, y, length, color):
	for i in range(length):
		pygame.gfxdraw.pixel(screen, x + i, y + i, color)

while running:
	screen.fill(black)
	for i in range(100):
		thisX, thisY = (random.randrange(0, screenWidth), random.randrange(0, screenHeight))
		thisLength = random.randrange(0,100)
		draw_flat_line(screen, thisX, thisY, thisLength, blue)
		draw_vertical_line(screen, thisX, thisY, thisLength, pink)
		draw_diagonal_line(screen, thisX, thisY, thisLength, green)

	#for i in range(100):
		#thisX, thisY = (random.randrange(50, screenWidth), random.randrange(50, screenHeight))
		#thisLength = random.randrange(50,100)
		#draw_flat_line(screen, thisX, thisY, thisLength, blue)
		#draw_vertical_line(screen, thisX, thisY, thisLength, pink)
		#draw_diagonal_line(screen, thisX, thisY, thisLength, green)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()