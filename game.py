import pygame
import random
from math import floor
pygame.init()
gameWidth = 500
gameHeight = 500
playerSizePix = 20
appleSizePix = 20

class Player():
	def __init__(self, x, y):
		self.posX = x
		self.posY = y
		self.movX = 0
		self.movY = 0
		self.velocity = 0.25
		self.size = playerSizePix
		#lengthArray stores a list of body positions for the snake. The first position is the head
		#The last element should be deleted and the new positon should be added to the front every movement
		self.lengthArray = [(self.posX, self.posY)]

	def move(self, direction):
		if direction == "up":
			self.movX = 0
			self.movY = -1
		if direction == "down":
			self.movX = 0
			self.movY = 1
		if direction == "left":
			self.movX = -1
			self.movY = 0
		if direction == "right":
			self.movX = 1
			self.movY = 0

	def updatePos(self, x, y):
		self.posX = x
		self.posY = y
		self.lengthArray.insert(0,(x, y))
		#Delete last pos in array
		del self.lengthArray[-1]
		#print(self.lengthArray)

	def ateApple(self):
		self.lengthArray.append((self.posX, self.posY))
		print("NEW BODY LOC:", self.posX - 100, self.posY)

class Apple():
	def __init__(self, x, y):
		self.posX = x
		self.posY = y
		self.size = appleSizePix

	def moveApple(self):
		self.posX = random.randint(0, gameWidth)
		self.posY = random.randint(0, gameHeight)

def isTouching(objectA, objectB):
	yTouching = False
	xTouching = False
	if objectA.posY > objectB.posY and objectA.posY < (objectB.posY + objectB.size) or objectA.posY == objectB.posY:
		#print("top point within or equal to same Y")
		yTouching = True
	if (objectA.posY + objectA.size) > objectB.posY and (objectA.posY + objectA.size) < (objectB.posY + objectB.size):
		#print("bottom point within or equal to same Y")
		yTouching = True
	if objectA.posX > objectB.posX and objectA.posX < (objectB.posX + objectB.size) or objectA.posX == objectB.posX:
		#print("top point within or equal to same X")
		xTouching = True
	if (objectA.posX + objectA.size) > objectB.posX and (objectA.posX + objectA.size) < (objectB.posX + objectB.size):
		#print("bottom point within or equal to same X")
		xTouching = True

	if xTouching and yTouching:
		#print("TOUCHING!!")
		return True
	else:
		#print("no :(")
		return False

player = Player((gameWidth / 2) - playerSizePix, (gameHeight / 2) - playerSizePix)
apple = Apple((gameWidth / 2) - playerSizePix + 200, (gameHeight / 2) - playerSizePix)
screen = pygame.display.set_mode((500,500))

running = True
while running:
	clock = pygame.time.Clock()
	dt = clock.tick(144)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((0,0,0))
	#Move player
	newPlayerX = player.posX + (player.movX * player.velocity * dt)
	newPlayerY = player.posY + (player.movY * player.velocity * dt)
	player.updatePos(newPlayerX, newPlayerY)

	#Check if key  press
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player.move("up")
	if keys[pygame.K_DOWN]:
		player.move("down")
	if keys[pygame.K_LEFT]:
		player.move("left")
	if keys[pygame.K_RIGHT]:
		player.move("right")

	#Check if player is touching apple
	if isTouching(player,apple) == True:
		apple.moveApple()
		for x in range(15):
			player.ateApple()
	#Draw Apple
	pygame.draw.rect(screen, (255,0,0), (apple.posX, apple.posY, appleSizePix, appleSizePix))
	#Draw player
	for x in range(len(player.lengthArray)):
		pygame.draw.rect(screen, (0,0,255), (player.lengthArray[x][0], player.lengthArray[x][1], playerSizePix, playerSizePix))
	pygame.display.flip()




