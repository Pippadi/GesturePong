#!/usr/bin/python3

import pygame
import serial
from time import sleep
import math

s = serial.Serial("/dev/ttyACM0")

bgColor = (0, 0, 0)
paddleColor = (10, 100, 100)

paddlePos = 640

s.readline()

zerosum = 0
for i in range(0, 50):
    zerosum += int(s.readline().decode())
zero = zerosum // 50

canvas = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong")

def getReading():
    r = int(s.readline().decode()) - zero
    if (r < 2 and r > 0) or (r > -2 and r < 0):
        return 0
    return r

def updateWindow():
    canvas.fill(bgColor)
    pygame.draw.rect(canvas, paddleColor, pygame.Rect(10, paddlePos, 10, 50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

shouldRun = True

while shouldRun:

    reading = getReading()
    
    rising = reading > 0
    while (reading >= 0) == rising:
        reading = getReading()
        paddlePos = paddlePos - reading*4
        paddlePos = max(paddlePos, 0)
        paddlePos = min(paddlePos, 640)
        updateWindow()

    while (reading < 0) == rising:
        reading = getReading()
        paddlePos = paddlePos - reading*4
        paddlePos = max(paddlePos, 0)
        paddlePos = min(paddlePos, 640)
        updateWindow()
