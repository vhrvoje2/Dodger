#Description: Several bad guys fall from the top of the screen, and the user must avoid them. 
#The player can be controlled with the arrow keys or more directly with the mouse. The longer 
#the player lasts without being hit, the higher the score.

#Variations: Have enemies fall at different rates and be different sizes. Have enemies fall 
#from more than one side of the game. Have power up pickups that grant invulnerability for a 
#while, slow down bad guys, give the player a temporary "reverse bad guys" power, etc.

import pygame
import random
import math

#screen settings
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

#object class
class Object:
    def __init__(self, isType, objectX, objectY, objectChange):
        self.isType = isType
        self.objectX = objectX
        self.objectY = objectY
        self.objectChange = objectChange

    def defineImage(self, path):  
        self.objectImage = pygame.image.load(path)

    def objectDraw(self):
        screen.blit(self.objectImage, (self.objectX, self.objectY))

    def objectMove(self):
        self.objectX += self.objectChange

def generateInt(letter):
    if letter == 'X':
        return random.randint(0, screenWidth-32)
    elif letter == 'Y':
        return random.randint(0, screenHeight//7)
    elif letter == 'C':
        return random.randint(1, 2)

def collision(item, player):
    if item.isType == 'bomb':
        itemYTemp = item.objectY + 32
        for x in range(int(player.objectX), int(player.objectX)+65):
            for y in range(item.objectX, item.objectX+9):
                distance = math.sqrt((math.pow(y-x, 2)) + (math.pow(itemYTemp-player.objectY,2)))
                if distance <= 1:
                    return True

    else:            
        itemYTemp = item.objectY + 30
        for x in range(int(player.objectX), int(player.objectX)+65):
            for y in range(item.objectX, item.objectX+29):
                distance = math.sqrt((math.pow(y-x, 2)) + (math.pow(itemYTemp-player.objectY,2)))
                if distance <= 1:
                    return True
    return False

def gameOver(score):
    print('Game over')
    return 1

def newItem():
    objectList.remove(item)
    objectList.append(spawnItem())
    return

def spawnItem():
    if random.randint(1, 5) > 4:
        gift = Object('gift', generateInt('X'), generateInt('Y'), generateInt('C'))
        gift.defineImage('gift.png')
        return gift
    else:
        bomb = Object('bomb', generateInt('X'), generateInt('Y'), generateInt('C'))
        bomb.defineImage('bomb.png')
        return bomb

#player settings
player = Object('player', screenWidth/2-32, screenHeight-42, 0)
player.defineImage('player.png')
playerSpeed = 3
health = 3
score = 0

#gift and bomb setting
objectList = []
objectCount = 10

for i in range(objectCount):
    objectList.append(spawnItem())
        
#main loop
running = True

while running:
    screen.fill((255, 255, 255))

    #keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.objectChange -= playerSpeed
            if event.key == pygame.K_RIGHT:
                player.objectChange += playerSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.objectChange = 0

    #move items
    for item in objectList:
        item.objectY += item.objectChange
        item.objectDraw()

        if collision(item, player):
            if item.isType == 'bomb':
                health -= 1
                print(health)
                if health == 0:
                    gameOver(score)
                newItem()
            else:
                score += 1
                print(score)
                newItem()

        if item.objectY >= screenHeight:
            newItem()
    player.objectMove()
    if player.objectX <= 0:
        player.objectX = 0
    elif player.objectX >= screenWidth-64:
        player.objectX = screenWidth-64
 
    player.objectDraw()
    
    pygame.display.update()

    #todo
    #add life points display
    #add score display