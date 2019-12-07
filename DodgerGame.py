#Description: Several bad guys fall from the top of the screen, and the user must avoid them. 
#The player can be controlled with the arrow keys or more directly with the mouse. The longer 
#the player lasts without being hit, the higher the score.

#Variations: Have enemies fall at different rates and be different sizes. Have enemies fall 
#from more than one side of the game. Have power up pickups that grant invulnerability for a 
#while, slow down bad guys, give the player a temporary "reverse bad guys" power, etc.

import pygame
import random
import math

screenWidth = 800
screenHeight = 600

class Enemy:
    def __init__(self, enemyX, enemyY):
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyImg = pygame.image.load('enemy.png')

    def enemyDraw(self):
        screen.blit(self.enemyImg, (self.enemyY, self.enemyY))

class Player:
    def __init__(self, playerX, playerY):
        self.playerX = playerX
        self.playerY = playerY
        self.playerImg = pygame.image.load('player.png')

    def playerDraw(self):
        screen.blit(self.playerImg, (self.playerX, self.playerY))

    def playerMove(self, playerChangeX):
        self.playerX += playerChangeX

screen = pygame.display.set_mode((screenWidth, screenHeight))
player = Player(368, 536)
playerChangeX = 0

enemy = Enemy(random.randint(0, 768), 0)
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerChangeX -= 1
            if event.key == pygame.K_RIGHT:
                playerChangeX += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerChangeX = 0

    enemy.enemyDraw()

    player.playerMove(playerChangeX)
    player.playerDraw()
    
    pygame.display.update()