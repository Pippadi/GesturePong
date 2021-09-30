import math
import pygame
import random 
import time
from pygame.locals import * 

def main():
    pygame.init()
    
    pygame.display.set_caption("Pong")

    WIDTH = 400
    HEIGHT = 400
    BLACK = (0, 0, 0)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FONT = pygame.font.SysFont(None, 48)
    
    background = pygame.image.load("bg.png")
    ball = pygame.image.load("Ball.png")
    paddle = pygame.image.load("Paddle.png")


    angle = 20
    xStep = 3
    yStep = 3
    x = 100
    y = 100

    paddleStep = 10
    X = 10
    Y = 10


    p = 0

    points = FONT.render(str(p), True, BLACK)

    textx = WIDTH - 30
    texty = 10
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Y -= paddleStep

                if event.key == pygame.K_DOWN:
                    Y += paddleStep
                        

        

        x += math.sin(math.radians(angle)) * xStep
        y += math.cos(math.radians(angle)) * yStep

        ballrect = ball.get_rect(topleft = (x + 23, y))
        paddlerect = paddle.get_rect(topleft = (X + 23, Y))

        if x >= HEIGHT or x <= 0:
            xStep = -xStep
        if y >= WIDTH or y <= 0:
            yStep =  -yStep

        if ballrect.colliderect(paddlerect):
            p += 1

        
        points = FONT.render(str(p), True, BLACK)

        screen.blit(background, (0, 0))
        screen.blit(points, (textx, texty))
        screen.blit(ball, (x, y))
        screen.blit(paddle, (X, Y))
        pygame.display.update()
        time.sleep(0.001)

            
if __name__ == "__main__":
    main()
