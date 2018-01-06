import pygame
import random
import string

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
bal = pygame.image.load("balloon_green.png")

pygame.display.set_caption('Key Stroke')

smallfont = pygame.font.SysFont("noteworthy" , 22)
mediumfont = pygame.font.SysFont("noteworthy" , 40)
largefont = pygame.font.SysFont("Bradley Hand" , 60)

clock = pygame.time.Clock()

#adding text to buttons
def t2b(msg , color , bx, by , bw , bh, size = "small"):
	textsurf , textrect = textobj(msg,color,size)
	textrect.center = ((bx + bw/2),(by + bh/2))
	gd.blit(textsurf , textrect)


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


def message_to_screen (msg , color = (0,0,0) ,xd=0 , yd = 0 , size = "large"):
	textsurf , textrect = textobj(msg,color,size)
	textrect.center = (dw/2)+xd,(dh/2)+yd
	gd.blit(textsurf,textrect)

#adding button functionality
def button(msg,bx,by,bw,bh,color1,color,action):

	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if bx+bw > cur[0] > bx and by+bh > cur[1] > by:
		pygame.draw.rect(gd, color , (bx,by,bw,bh))
		if click[0] == 1 :
			if action == "play":
				level_screen()
			elif action == "instructions":
				inst()
			elif action == "quit":
				pygame.quit()
				quit()
			elif action == "Easy":
				gameloop("Easy")
			elif action == "Medium":
				gameloop("Medium")
			elif action == "Hard":
				gameloop("Hard")



	
	else:
		pygame.draw.rect(gd, color1 , (bx,by,bw,bh))
	
	t2b(msg,black,bx,by,bw,bh)

#the first screen
def intro ():
	
	intro = True
	while intro :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		gd.blit(bg2 ,(0,0))
		message_to_screen("Welcome to caption" , blue , 0,-50 , "large")
		message_to_screen("BURST THE BALLOONS!" , white , 0,0 , "small")

		
		button("play" , 50,350,150,50 ,blue , darkblue,action="play")
		button("instructions" ,325,350,150,50  ,white , grey,action="instructions")
		button("quit" ,600,350,150,50  ,blue , darkblue,action="quit")

		pygame.display.update()
		clock.tick(15)	

#pause function
def pause():
	ps = True
	message_to_screen("Paused" , white , 0,-100 , size = "large")
	message_to_screen("click c to continue and q to quit" , white , 0,0 , size = "small")
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
sc = 0
#score function
def score (sc):
	message_to_screen("Score : "+str(sc) , black , -400,-290 , "small")
	pygame.display.update()

#instruction screen
def inst() :
	ins = True
	while ins :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
		gd.fill((50,100,200))
		message_to_screen("Instructions" , green ,0, -50 , "large")
		message_to_screen("The aim is to burst all the balloons before they reach the top" , white , 0,-10 , "small")
		message_to_screen("The balloons burst if the relevant key is pressed" , white ,0, 15 , "small")

		button("play" , 50,450,150,50 ,green , darkgreen,action="play")
		
		button("quit" ,600,450,150,50  ,green , darkgreen,action="quit")

		pygame.display.update()
		clock.tick(15)	

#screen to display diiferent levels
def level_screen():
	ls = True
	while ls :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()


		gd.blit(bg2 ,(0,0))
		pygame.display.update()
		message_to_screen("BURST THE BALLOONS!" , blue , 0,+50 , "large")

		
		button("Easy" , 50,200,150,50 ,blue , darkblue , action = "Easy")
		button("Medium" ,325,200,150,50  ,white , grey , action="Medium")
		button("Hard" ,600,200,150,50  ,blue , darkblue , action="Hard")

		pygame.display.update()
		clock.tick(15)	
rx = random.randrange(0,570)
c = random.choice(string.ascii_letters)
y = 570
#balloon function
def balloon():
	gd.blit(bal , (rx , y ) )
	message_to_screen(c,black,rx-435,y-290,"small")
	pygame.display.update()

balloonl=[]
balloonx=[]
balloony=[]


for i in range (0,20):
	balloonx.append(round(random.randrange(0,570)/20)*20)
	balloonl.append(random.choice(string.ascii_letters))
	balloony.append(y)


def gameloop(level):
	ex = False
	ov = False
	balloonlist=[]
	fps = 15
	number = 8
	global rx , c, y,sc	
	if level == "Easy":
		number = 8
	if level == "Medium":
		number = 15
	if level == "Hard":
		number = 20

	while not ex:

		if ov == True:
			gd.fill((50,100,200))
			message_to_screen("game over",white,0,0,"large")
			message_to_screen("press c to pay again",white,0,40,"small")
			message_to_screen("press q to quit",white,0,70,"small")
			
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
		
		gd.blit(bg1 , (0,0))
		pygame.display.update()
		for i in range (0,number):
			gd.blit(bal , (balloonx[i],balloony[i]))
			message_to_screen(balloonl[i],black,balloonx[i]-435,balloony[i]-290,"small")
			
			pygame.display.update()


		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				ex = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					for i in range(0,number):
						if  balloonl[i] == 'a':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_b:
					for i in range(0,number):
						if  balloonl[i] == 'b':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_c:
					for i in range(0,number):
						if  balloonl[i] =='c':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_d:
					for i in range(0,number):
						if  balloonl[i] == 'd':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_e:
					for i in range(0,number):
						if  balloonl[i] == 'e':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_f:
					for i in range(0,number):
						if  balloonl[i] == 'f':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_g:
					for i in range(0,number):
						if  balloonl[i] == 'g':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_h:
					for i in range(0,number):
						if  balloonl[i] == 'h':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_i:
					for i in range(0,number):
						if  balloonl[i] == 'i':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_j:
					for i in range(0,number):
						if  balloonl[i] == 'j':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_k:
					for i in range(0,number):
						if  balloonl[i] =='k':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_l:
					for i in range(0,number):
						if  balloonl[i] == 'l':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_m:
					for i in range(0,number):
						if  balloonl[i] == 'm':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_n:
					for i in range(0,number):
						if  balloonl[i] == 'n':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_o:
					for i in range(0,number):
						if  balloonl[i] == 'o':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_p:
					for i in range(0,number):
						if  balloonl[i] == 'p':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_q:
					for i in range(0,number):
						if  balloonl[i] == 'q':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_r:
					for i in range(0,number):
						if  balloonl[i] == 'r':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_s:
					for i in range(0,number):
						if  balloonl[i] =='s':
							sc = sc + 5
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_t:
					for i in range(0,number):
						if  balloonl[i] == 't':
							sc = sc + 5 
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_u:
					for i in range(0,number):
						if  balloonl[i] == 'u':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_v:
					for i in range(0,number):
						if  balloonl[i] == 'v':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_w:
					for i in range(0,number):
						if  balloonl[i] == 'w':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_x:
					for i in range(0,number):
						if  balloonl[i] == 'x':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_y:
					for i in range(0,number):
						if  balloonl[i] == 'y':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
				elif event.key == pygame.K_z:
					for i in range(0,number):
						if  balloonl[i] == 'z':
							sc = sc + 5
							
							balloonl[i] = random.choice(string.ascii_letters)
							balloony[i] = 570
		

		
		for i in range(0,number):
			balloony[i] = balloony[i] - 10
			if balloony[i]<= 0:
				ov = True
		score(sc)
	
		clock.tick(100)

intro()
