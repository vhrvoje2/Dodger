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
    def __init__(self, objectX, objectY, objectChange):
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
        return random.randint(0, screenHeight//20)
    elif letter == 'C':
        return random.randint(1, 2)

#player settings
player = Object(screenWidth/2-32, screenHeight-64, 0)
player.defineImage('player.png')

#gift and enemy setting
objectList = []
objectCount = 10

for i in range(objectCount):

    if random.randint(1, 5) > 4:
        gift = Object(generateInt('X'), generateInt('Y'), generateInt('C'))
        gift.defineImage('gift.png')
        objectList.append(gift)
    else:
        enemy = Object(generateInt('X'), generateInt('Y'), generateInt('C'))
        enemy.defineImage('enemy.png')
        objectList.append(enemy)
        
#main loop
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.objectChange -= 1
            if event.key == pygame.K_RIGHT:
                player.objectChange += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.objectChange = 0


    for item in objectList:
        item.objectY += item.objectChange
        item.objectDraw()

        if item.objectY >= screenHeight:
            item.objectX = generateInt('X')
            item.objectY = generateInt('Y')
            item.objectChange = generateInt('C')

    player.objectMove()
    if player.objectX <= 0:
        player.objectX = 0
    elif player.objectX >= screenWidth-64:
        player.objectX = screenWidth-64
 
    player.objectDraw()
    
    pygame.display.update()

    #todo
    #add collision
    #add life points
    #add score
    #add background
    #add music
    #add sounds