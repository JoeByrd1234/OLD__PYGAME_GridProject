import pygame
pygame.init()

maxX = 1200
maxY = 800
cWHITE = (255,255,255)
cRED = (255,0,0)
cBLUE = (0,0,255)
cGREEN = (0,255,0)
cBLACK = (0,0,0)
cGREY = (50,50,50)

gameDisplay = pygame.display.set_mode((maxX,maxY))
pygame.display.set_mode((maxX,maxY))
gameExit = False
BGCOLOR = cGREY
mousePos = (0,0)

class Grid:
	def __init__(self,row,col):
		self.rows = row
		self.cols = col
		self.data = []
		self.boundryW = (50 / self.cols)
		self.boundryH = (50 / self.rows)
		self.recW = (maxX / self.cols) - self.boundryW
		self.recH = (maxY / self.rows) - self.boundryH
		for i in range(0,self.rows):
			self.data.append([])
			for r in range(0,self.cols):
				self.data[i].append(0)

	def nextStep(self):
		temp = []
		for i in range(0,self.rows):
			temp.append([])
			for r in range(0,self.cols):
				temp[i].append(self.data[i][r])
		for r in range(0,len(self.data)):
			for c in range(0,len(self.data[r])):
				if r-1 >= 0:
					if self.data[r-1][c] == 1:
						temp[r][c] = 1
				if r+1 < self.rows: 
					if self.data[r+1][c] == 1:
						temp[r][c] = 1
				if c+1 < self.cols: 
					if self.data[r][c+1] == 1:
						temp[r][c] = 1
				if c-1 >= 0:
					if self.data[r][c-1] == 1:
						temp[r][c] = 1
		self.data = temp


	def print(self):
		#self.data[4][4] = 1
		for r in range(0,len(self.data)):
			for c in range(0,len(self.data[r])):
				if self.data[r][c] == 0:
					gameDisplay.fill(cGREEN, rect = [(c * self.recW) + (c * self.boundryW) + self.boundryW,(r * self.recH) + (r * self.boundryH) + self.boundryH,self.recW,self.recH])
				elif self.data[r][c] == 1:
					gameDisplay.fill(cRED, rect = [(c * self.recW) + (c * self.boundryW) + self.boundryW,(r * self.recH) + (r * self.boundryH) + self.boundryH,self.recW,self.recH])
				else:
					gameDisplay.fill(cBLUE, rect = [(c * self.recW) + (c * self.boundryW) + self.boundryW,(r * self.recH) + (r * self.boundryH) + self.boundryH,self.recW,self.recH])

#print("Enter the rows and cols")
#r, c = input().split()
#grid = Grid(int(r),int(c))
grid = Grid(50,50)
#print("Enter the starting red")
#r, c = input().split()
#grid.data[int(r)][int(c)] = 1


gameDisplay.fill(BGCOLOR)
grid.print()
pygame.display.update()
while not gameExit:
	for event in pygame.event.get():
		print(event)
		mousePos = pygame.mouse.get_pos()
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			gameExit = True
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if event.button == 1:
				grid.data[int((pos[1]/maxY*grid.rows))][int((pos[0]/maxX*grid.cols))] = 1
			elif event.button == 3:
				grid.data[int((pos[1]/maxY*grid.rows))][int((pos[0]/maxX*grid.cols))] = 2
			gameDisplay.fill(BGCOLOR)
			grid.print()
			pygame.display.update()
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_SPACE:
				grid.nextStep()
				gameDisplay.fill(BGCOLOR)
				grid.print()
				pygame.display.update()
		#if keys[pygame.K_SPACE]
