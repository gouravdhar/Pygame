#import modules
import pygame
import time
import random

pygame.init() #initiate pygame

#dimensions of game window
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))  #resolutoin of display for the game
pygame.display.set_caption('A bit racey')

black = (0,0,0)
white = (255,255,255)

#colors for obstacles
colors = [
(159, 53,  205),
(27, 243, 27),
(243, 27, 27),
(222, 243, 27 ),
(255,  153, 51 ),
(255, 51, 195 ),
(6, 31, 255 ),
(30,  30,  30),
(0, 0, 0) 
]



clock = pygame.time.Clock()


carImg = pygame.image.load('racecar.png')
car_width = 73

#calculate score by counting the number of dodged objects
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#function to create obstacles
def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#display car at x,y coordinates
def car(x,y):
	gameDisplay.blit(carImg, (x,y))

#display texg message
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center =((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	
	time.sleep(2)
	# game_loop()


def crash():
	message_display('You Crashed')

#game
def game_loop():

	x = 400
	y = 400
	x_change = 0 
	crashed = False
	dodged = 0 

	#specifications of obstacle
	thing_startx = random.randrange(0,display_width)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	
	#color of the obstacle
	val = random.randrange(0, 8)

	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed = True
			# print(event)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change
		gameDisplay.fill(white)
	
		#update the obstacle every instant
		things(thing_startx, thing_starty, thing_width, thing_height, colors[val])
		thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged)

		#check crash conditions i.e. if car touches the window boundary, it will be treated as crashed
		if x > display_width-car_width or x<0:
			crash()
			# crashed = True

		#if obstacle has passed the car, create a new obstacle
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			val = random.randrange(0, 8)
			# print (val)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)

		#checki if car ha touched the obstacles
		if y < thing_starty + thing_height:
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				crash()
				# crashed = True
                

		pygame.display.update()
		clock.tick(60)


game_loop()
pygame.quit()
quit()