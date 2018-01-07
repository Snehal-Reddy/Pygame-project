import pygame
import random
import string

pygame.init()
pygame.mixer.init()
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

#game images
bg1 = pygame.image.load("background1.png")
bg2 = pygame.image.load("background2.png")
bal = pygame.image.load("balloon_green.png")
heart = pygame.image.load("heart0024.png")
button = pygame.image.load("button.png")

#game sounds
wrongkey = pygame.mixer.Sound("wrongkey.wav")
burst = pygame.mixer.Sound("burst.wav")

#music
pygame.mixer.music.load("theme.wav")
pygame.mixer.music.play()

pygame.display.set_caption('Key Stroke')

 
smallfont = pygame.font.SysFont("noteworthy" , 22)
mediumfont = pygame.font.SysFont("noteworthy" , 40)
largefont = pygame.font.SysFont("Planet Benson Two" , 60)

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
		message_to_screen("Welcome to KeyStroke" , blue , 0,-50 , "large")
		message_to_screen("BURST THE BALLOONS!" , white , 0,0 , "small")

		
		button("play" , 50,350,150,50 ,blue , darkblue,action="play")
		button("instructions" ,325,350,150,50  ,white , grey,action="instructions")
		button("quit" ,600,350,150,50  ,blue , darkblue,action="quit")

		pygame.display.update()	

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

			clock.tick(15)
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

#balloon function
def balloon():
	gd.blit(bal , (rx , y ) )
	message_to_screen(c,black,rx-435,y-290,"small")
	pygame.display.update()

balloonl=[]
balloonx=[]
balloony=[]


for i in range (0,20):
	balloonx.append(round(random.randrange(0,870)//20)*20)
	balloonl.append(random.choice(string.ascii_letters))
	balloony.append(random.randrange(600,650))
	

def gameloop(level):
	global balloony
	global balloonx
	global balloonl
	life = 3
	ov = False
	ex = False
	#ov = False
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
			message_to_screen("press c to play again",white,0,40,"small")
			message_to_screen("press q to quit",white,0,70,"small")
			
			pygame.display.update()


		while ov:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					if event.key == pygame.K_c:
						ov = False
						ex = False
						balloonl=[]
						balloonx=[]
						balloony=[]
						sc = 0
						for i in range (0,20):
							balloonx.append(round(random.randrange(0,870)//20)*20)
							balloonl.append(random.choice(string.ascii_letters))
							balloony.append(random.randrange(600,650))
						intro()
		
		gd.blit(bg1 , (0,0))
		if life == 3:
			gd.blit(heart,(790,0))
			gd.blit(heart,(820,0))
			gd.blit(heart,(850,0))
		if life == 2:
			#gd.blit(heart,(790,0))
			gd.blit(heart,(820,0))
			gd.blit(heart,(850,0))
		if life == 1:
			#gd.blit(heart,(790,0))
			#gd.blit(heart,(820,0))
			gd.blit(heart,(850,0))		
		pygame.display.update()
		for i in range (0,number):
			gd.blit(bal , (balloonx[i],balloony[i]))
			message_to_screen(balloonl[i],black,balloonx[i]-435,balloony[i]-290,"small")
			
		pygame.display.update()

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:	
				if event.key == pygame.K_a:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						A1 = True
						for i in range(0,number):
							if  balloonl[i] == 'A':
								sc = sc + 5
								A1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(A1):
							wrongkey.play()
							sc = sc - 10

					else:
						a1 = True
						for i in range(0,number):
							if  balloonl[i] == 'a':
								sc = sc + 5
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
								a1 = False
								burst.play()
						if(a1):
							wrongkey.play()
							sc = sc - 10

				elif event.key == pygame.K_b:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						B1 = True
						for i in range(0,number):
							if  balloonl[i] == 'B':
								sc = sc + 5
								B1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(B1):
							wrongkey.play()
							sc = sc - 10
					else:
						b1 = True
						for i in range(0,number):
							if  balloonl[i] == 'b':
								sc = sc + 5
								b1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(b1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_c:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						C1 = True
						for i in range(0,number):
							if  balloonl[i] == 'C':
								sc = sc + 5
								C1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(C1):
							wrongkey.play()
							sc = sc - 10
					else:
						c1 = True
						for i in range(0,number):
							if  balloonl[i] == 'c':
								sc = sc + 5
								c1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(c1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_d:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						D1 = True
						for i in range(0,number):
							if  balloonl[i] == 'D':
								sc = sc + 5
								D1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(D1):
							wrongkey.play()
							sc = sc - 10
					else:
						d1 = True
						for i in range(0,number):
							if  balloonl[i] == 'd':
								sc = sc + 5
								d1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(d1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_e:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						E1 = True
						for i in range(0,number):
							if  balloonl[i] == 'E':
								sc = sc + 5
								E1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(E1):
							wrongkey.play()
							sc = sc - 10
					else:
						e1 = True
						for i in range(0,number):
							if  balloonl[i] == 'e':
								sc = sc + 5
								e1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(e1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_f:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						F1 = True
						for i in range(0,number):
							if  balloonl[i] == 'F':
								sc = sc + 5
								F1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(F1):
							wrongkey.play()
							sc = sc - 10
					else:
						f1 = True
						for i in range(0,number):
							if  balloonl[i] == 'f':
								sc = sc + 5
								f1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(f1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_g:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						G1 = True
						for i in range(0,number):
							if  balloonl[i] == 'G':
								sc = sc + 5
								G1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(G1):
							wrongkey.play()
							sc = sc - 10
					else:
						g1 = True
						for i in range(0,number):
							if  balloonl[i] == 'g':
								sc = sc + 5
								g1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(g1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_h:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						H1 = True
						for i in range(0,number):
							if  balloonl[i] == 'H':
								sc = sc + 5
								H1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(H1):
							wrongkey.play()
							sc = sc - 10
					else:
						h1 = True
						for i in range(0,number):
							if  balloonl[i] == 'h':
								sc = sc + 5
								H1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(h1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_i:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						I1 = True
						for i in range(0,number):
							if  balloonl[i] == 'I':
								sc = sc + 5
								I1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(I1):
							wrongkey.play()
							sc = sc - 10
					else:
						i1 = True
						for i in range(0,number):
							if  balloonl[i] == 'i':
								sc = sc + 5
								i1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(i1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_j:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						J1 = True
						for i in range(0,number):
							if  balloonl[i] == 'J':
								sc = sc + 5
								J1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(J1):
							wrongkey.play()
							sc = sc - 10
					else:
						j1 = True
						for i in range(0,number):
							if  balloonl[i] == 'j':
								sc = sc + 5
								j1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(j1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_k:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						K1 = True
						for i in range(0,number):
							if  balloonl[i] == 'K':
								sc = sc + 5
								K1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(K1):
							wrongkey.play()
							sc = sc - 10
					else:
						k1 = True
						for i in range(0,number):
							if  balloonl[i] == 'k':
								sc = sc + 5
								k1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(k1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_l:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						L1 = True
						for i in range(0,number):
							if  balloonl[i] == 'L':
								sc = sc + 5
								L1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(L1):
							wrongkey.play()
							sc = sc - 10
					else:
						l1 = True
						for i in range(0,number):
							if  balloonl[i] == 'l':
								sc = sc + 5
								l1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(l1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_m:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						M1= True
						for i in range(0,number):
							if  balloonl[i] == 'M':
								sc = sc + 5
								M1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(M1):
							wrongkey.play()
							sc = sc - 10
					else:
						m1 = True
						for i in range(0,number):
							if  balloonl[i] == 'm':
								sc = sc + 5
								m1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(m1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_n:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						N1 = True
						for i in range(0,number):
							if  balloonl[i] == 'N':
								sc = sc + 5
								N1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(N1):
							wrongkey.play()
							sc = sc - 10
					else:
						n1 = True
						for i in range(0,number):
							if  balloonl[i] == 'n':
								sc = sc + 5
								n1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(n1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_o:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						O1 = True
						for i in range(0,number):
							if  balloonl[i] == 'O':
								sc = sc + 5
								O1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(O1):
							wrongkey.play()
							sc = sc - 10
					else:
						o1 = True
						for i in range(0,number):
							if  balloonl[i] == 'o':
								sc = sc + 5
								o1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(o1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_p:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						P1 = True
						for i in range(0,number):
							if  balloonl[i] == 'P':
								sc = sc + 5
								P1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(P1):
							wrongkey.play()
							sc = sc - 10
					else:
						p1  = True
						for i in range(0,number):
							if  balloonl[i] == 'p':
								sc = sc + 5
								p1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(p1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_q:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						Q1 = True
						for i in range(0,number):
							if  balloonl[i] == 'Q':
								sc = sc + 5
								Q1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(Q1):
							wrongkey.play()
							sc = sc - 10
					else:
						q1 = True
						for i in range(0,number):
							if  balloonl[i] == 'q':
								sc = sc + 5
								q1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(q1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_r:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						R1 = True
						for i in range(0,number):
							if  balloonl[i] == 'R':
								sc = sc + 5
								R1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(R1):
							wrongkey.play()
							sc = sc - 10
					else:
						r1 = True
						for i in range(0,number):
							if  balloonl[i] == 'r':
								sc = sc + 5
								r1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(r1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_s:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						S1 = True
						for i in range(0,number):
							if  balloonl[i] == 'S':
								sc = sc + 5
								S1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(S1):
							wrongkey.play()
							sc = sc - 10
					else:
						s1 = True
						for i in range(0,number):
							if  balloonl[i] == 's':
								sc = sc + 5
								s1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(s1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_t:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						T1 = True
						for i in range(0,number):
							if  balloonl[i] == 'T':
								sc = sc + 5
								T1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(T1):
							wrongkey.play()
							sc = sc - 10
					else:
						t1 = True
						for i in range(0,number):
							if  balloonl[i] == 't':
								sc = sc + 5
								t1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(t1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_u:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						U1 = True
						for i in range(0,number):
							if  balloonl[i] == 'U':
								sc = sc + 5
								U1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(U1):
							wrongkey.play()
							sc = sc - 10
					else:
						u1 = True
						for i in range(0,number):
							if  balloonl[i] == 'u':
								sc = sc + 5
								u1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(u1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_v:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						V1 = True
						for i in range(0,number):
							if  balloonl[i] == 'V':
								sc = sc + 5
								V1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(V1):
							wrongkey.play()
							sc = sc - 10
					else:
						v1 = True
						for i in range(0,number):
							if  balloonl[i] == 'v':
								sc = sc + 5
								v1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(v1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_w:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						W1 = True
						for i in range(0,number):
							if  balloonl[i] == 'W':
								sc = sc + 5
								W1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(W1):
							wrongkey.play()
							sc = sc - 10
					else:
						w1 = True
						for i in range(0,number):
							if  balloonl[i] == 'w':
								sc = sc + 5
								w1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(w1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_x:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						X1 = True
						for i in range(0,number):
							if  balloonl[i] == 'X':
								sc = sc + 5
								X1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(X1):
							wrongkey.play()
							sc = sc - 10
					else:
						x1 = True
						for i in range(0,number):
							if  balloonl[i] == 'x':
								sc = sc + 5
								x1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(x1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_y:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						Y1 = True
						for i in range(0,number):
							if  balloonl[i] == 'Y':
								sc = sc + 5
								Y1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(Y1):
							wrongkey.play()
							sc = sc - 10
					else:
						y1 = True
						for i in range(0,number):
							if  balloonl[i] == 'y':
								sc = sc + 5
								y1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(y1):
							wrongkey.play()
							sc = sc - 10
				elif event.key == pygame.K_z:
					if pygame.key.get_mods() & pygame.KMOD_SHIFT:
						Z1 = True
						for i in range(0,number):
							if  balloonl[i] == 'Z':
								sc = sc + 5
								Z1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(Z1):
							wrongkey.play()
							sc = sc - 10
					else:
						z1 = True
						for i in range(0,number):
							if  balloonl[i] == 'z':
								sc = sc + 5
								z1 = False
								burst.play()
								balloonl[i] = random.choice(string.ascii_letters)
								balloony[i] = random.randrange(600,650)
						if(z1):
							wrongkey.play()
							sc = sc - 10
		

		
		for i in range(0,number):
			balloony[i] = balloony[i] - 1
			if balloony[i]== 0:
				balloonl[i] = random.choice(string.ascii_letters)
				balloony[i] = random.randrange(600,650)
				life -= 1

		if life == 0:
			ov = True	
							
		score(sc)
	
		#clock.tick(10000)

intro()
