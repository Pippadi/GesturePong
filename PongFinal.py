#!/usr/bin/python3

import math
import pygame
import random 
import time
from pygame.locals import * 
import serial

WIDTH = 400
HEIGHT = 400

PADDLE_INITIAL_X = 2
PADDLE_INITIAL_Y = HEIGHT//2

pygame.init()
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 48)
    
background = pygame.image.load("assets/bg.png")
ball = pygame.image.load("assets/Ball.png")
paddle = pygame.image.load("assets/Paddle.png")

angle = random.randint(20, 60)
xStep = 3
yStep = 3
x = 100
y = 100

paddleStep = 50
paddleX = PADDLE_INITIAL_X
paddleY = PADDLE_INITIAL_Y

points = 0

textx = WIDTH - 30
texty = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddleY = max(paddleY-paddleStep, 0)

            if event.key == pygame.K_DOWN:
                paddleY = min(paddleY+paddleStep, HEIGHT)
                        
    x += math.sin(math.radians(angle)) * xStep
    y += math.cos(math.radians(angle)) * yStep

    ballrect = ball.get_rect(topleft = (x + 23, y))
    paddlerect = paddle.get_rect(topleft = (paddleX + 23, paddleY))

    if x >= HEIGHT:
        xStep = -xStep
    if x <= 0:
        xStep = -xStep
        points -= 1
    if y >= WIDTH or y <= 0:
        yStep =  -yStep

    if ballrect.colliderect(paddlerect):
        points += 1
        xStep = -xStep
    
    pointsText = FONT.render(str(points), True, BLACK)

    screen.blit(background, (0, 0))
    screen.blit(pointsText, (textx, texty))
    screen.blit(ball, (x, y))
    screen.blit(paddle, (paddleX, paddleY))
    pygame.display.update()
    time.sleep(0.001)
