#!/usr/bin/python3

import math
import pygame
import random 
import time
from pygame.locals import * 
import serial
import serial.tools.list_ports
from gesture_control import GestureController

WIDTH = 400
HEIGHT = 400

PADDLE_INITIAL_X = 2
PADDLE_INITIAL_Y = HEIGHT//2
PADDLE_STEP = 50
TEXT_X = WIDTH - 60
TEXT_Y = 10

def getSerialPort():
    print("Which serial port is the gesture controller connected to?")
    ports = [port.device for port in serial.tools.list_ports.comports()]
    print("0) None")
    for i in range(0, len(ports)):
        print(i+1, end=") ")
        print(ports[i])
    try:
        sel = int(input("0 - "+str(len(ports))+": "))
    except:
        return ""
    if sel != 0:
        return ports[sel - 1]
    return ""

serialPort = getSerialPort()
gestureEnabled = serialPort != ""
if gestureEnabled:
    controller = GestureController(serialPort)

pygame.init()
pygame.display.set_caption("Pong")

BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 48)
    
background = pygame.image.load("assets/bg.png")
ball = pygame.image.load("assets/Ball.png")
paddle = pygame.image.load("assets/Paddle.png")

angle = random.randint(20, 60)
xStep = 6
yStep = 6
x = 100
y = 100

paddleX = PADDLE_INITIAL_X
paddleY = PADDLE_INITIAL_Y

points = 0
running = True
prevTime = time.perf_counter()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddleY = max(paddleY-PADDLE_STEP, 0)

            if event.key == pygame.K_DOWN:
                paddleY = min(paddleY+PADDLE_STEP, HEIGHT-30)
                        
    if gestureEnabled:
        paddleY = max(min(paddleY + controller.newPositionIncrement(), HEIGHT-30), 0)

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
    screen.blit(pointsText, (TEXT_X, TEXT_Y))
    screen.blit(ball, (x, y))
    screen.blit(paddle, (paddleX, paddleY))
    pygame.display.update()
    now = time.perf_counter()
    time.sleep((10 - (now - prevTime)) / 1000)
    prevTime = now
