import pygame
import random

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (100,100,255)
darkblue = (80,80,150)
darkgreen = (34,177,76)
grey = (200,200,200)

dw = 900 
dh = 600

gd = pygame.display.set_mode((dw,dh))

bg1 = pygame.image.load("background1.png")
bg2 = pygame.image.load("background2.png")

pygame.display.set_caption('caption')

smallfont = pygame.font.SysFont("noteworthy" , 25)
mediumfont = pygame.font.SysFont("noteworthy" , 40)
largefont = pygame.font.SysFont("Bradley Hand" , 60)

clock = pygame.time.Clock()

#adding text to buttons
def t2b(msg , color , bx, by , bw , bh, size = "small"):
	textsurf , textrect = textobj(msg,color,size)
	textrect.center = ((bx + bw/2),(by + bh/2))
	gd.blit(textsurf , textrect)

#adding button functionality
def button(msg,bx,by,bw,bh,color1,color):
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if bx+bw > cur[0] > bx and by+bh > cur[1] > by:
		pygame.draw.rect(gd, color , (bx,by,bw,bh))
		if click[0] == 1:
			if msg == "play":
				gameloop()
			elif msg == "instructions":
				pass
			elif msg == "quit":
				pygame.quit()
				quit()
	
	else:
		pygame.draw.rect(gd, color1 , (bx,by,bw,bh))
	
	t2b(msg,black,bx,by,bw,bh)


def intro ():
	intro = True
	while intro :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.type == pygame.K_q:
					pygame.quit()
					quit()


		gd.blit(bg2 ,(0,0))
		message_to_screen("Welcome to caption" , blue , -50 , "large")
		message_to_screen("BURST THE BALLOONS!" , white , 0 , "small")

		
		button("play" , 50,350,150,50 ,blue , darkblue)
		button("instructions" ,325,350,150,50  ,white , grey)
		button("quit" ,600,350,150,50  ,blue , darkblue)

		pygame.display.update()
		clock.tick(15)	
def pause():
	ps = True
	message_to_screen("Paused" , white , -100 , size = "large")
	message_to_screen("click c to continue and q to quit" , white , 0 , size = "small")
	pygame.display.update()
	while ps:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					ps = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

			clock.tick(5)
def score (sc):
	text = smallfont.render("Score: "+str(sc),True ,white)
	gd.blit(text,[0,0])

def textobj(text , color, size):
	if size == "small":
		textsurf = smallfont.render(text , True ,color)
		return textsurf , textsurf.get_rect()
	if size == "medium":
		textsurf = mediumfont.render(text , True ,color)
		return textsurf , textsurf.get_rect()
	if size == "large":
		textsurf = largefont.render(text , True ,color)
	return textsurf , textsurf.get_rect()


def message_to_screen (msg , color = (0,0,0) , yd = 0 , size = "large"):
	textsurf , textrect = textobj(msg,color,size)
	textrect.center = (dw/2),(dh/2)+yd
	gd.blit(textsurf,textrect)


def gameloop():
	ex = False
	ov = False
	fps = 15
	while not ex:

		if ov == True:
			gd.fill((50,100,200))
			message_to_screen("game over",white,0,"large")
			message_to_screen("press c to pay again",white,40,"small")
			message_to_screen("press q to quit",white,70,"small")
			
			pygame.display.update()


		while ov:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					ex = True
					ov = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						ex = True
						ov = False
					if event.key == pygame.K_c:
						gameloop()
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				ex = True
		gd.blit(bg1 , (0,0))
		pygame.display.update()





intro()
gameloop()
