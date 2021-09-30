#!/usr/bin/python3

import math
import pygame
import random 
import time

def main():
    pygame.init()
    
    pygame.display.set_caption("BingBong")

    WIDTH = 400
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    background = pygame.image.load("../assets/bg.png")
    img = pygame.image.load("../assets/Ball.png")

    angle = 20
    xStep = 5
    yStep = 5
    x = 0
    y = 0
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x += math.sin(math.radians(angle)) * xStep
        y += math.cos(math.radians(angle)) * yStep 

        if x >= HEIGHT or x <= 0:
            xStep = -xStep
        if y >= WIDTH or y <= 0:
            yStep =  -yStep

        screen.blit(background, (0, 0))
        screen.blit(img, (x, y))
        print(x, y)
        pygame.display.update()
        time.sleep(0.001)

if __name__ == "__main__":
    main()
