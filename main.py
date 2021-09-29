#!/usr/bin/python3

import pygame
from pygame.locals import *
import serial
import serial.tools.list_ports

WIDTH = 400
HEIGHT = 400

PADDLE_INITIAL_X = 5
PADDLE_INITIAL_Y = HEIGHT//2
BALL_INITIAL_X = 200
BALL_INITIAL_Y = 100

pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("assets/bg.png")
paddle = pygame.image.load("assets/Paddle.png")
ball = pygame.image.load("assets/Ball.png")
paddleX = PADDLE_INITIAL_X
paddleY = PADDLE_INITIAL_Y

def getSerialPort():
    print("Which serial port is the gesture controller connected to?")
    ports = [port.device for port in serial.tools.list_ports.comports()]
    print("0) None")
    for i in range(0, len(ports)):
        print(i+1, end=") ")
        print(ports[i])
    sel = int(input("0 - "+str(len(ports))+": "))
    if sel != 0:
        return ports[sel - 1]
    return ""

def blitAll():
    screen.blit(background, (0, 0))
    screen.blit(paddle, (paddleX, paddleY))
    pygame.display.update()

serialPort = getSerialPort()
gestureEnabled = serialPort != ""
