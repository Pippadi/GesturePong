#!/usr/bin/python3

import pygame
from pygame.locals import * 

def main():
    pygame.init()

    pygame.display.set_caption("Collision Detection")

    BLACK = (0, 0, 0)

    FONT = pygame.font.SysFont(None, 48)

    WIDTH = 400
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    background = pygame.image.load("bg.png")
    screen.blit(background, (0, 0))
    ball = pygame.image.load("Ball.png")
    paddle = pygame.image.load("Paddle.png")
    paddleposx = 5
    paddleposy = 10
    xpos = 200
    ypos = 100
    x_step = 5
    y_step = 5 
    screen.blit(ball, (xpos, ypos))
    screen.blit(paddle, (paddleposx, paddleposy))
    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))

    clock = pygame.time.Clock()

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if ypos > HEIGHT - 64 or ypos < 0:
                y_step = -y_step
            if xpos > WIDTH - 64 or xpos < 0:
                x_step = -x_step

            if event.type == KEYDOWN: 

                if event.key == K_UP or event.key == K_w:
                    ypos -= y_step
                    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                    screen.blit(background, (0, 0))
                    screen.blit(paddle, (paddleposx, paddleposy))
                    screen.blit(ball, (xpos, ypos))
                    pygame.display.update()

                if event.key == K_DOWN or event.key == K_s:
                    ypos += y_step
                    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                    screen.blit(background, (0, 0))
                    screen.blit(paddle, (paddleposx, paddleposy))
                    screen.blit(ball, (xpos, ypos))
                    pygame.display.update()

                if event.key == K_LEFT or event.key == K_d:
                    xpos -= x_step
                    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                    screen.blit(background, (0, 0))
                    screen.blit(paddle, (paddleposx, paddleposy))
                    screen.blit(ball, (xpos, ypos))
                    pygame.display.update()

                if event.key == K_RIGHT or event.key == K_a:
                    xpos += x_step
                    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                    screen.blit(background, (0, 0))
                    screen.blit(paddle, (paddleposx, paddleposy))
                    screen.blit(ball, (xpos, ypos))
                    pygame.display.update()

            if event.type == KEYUP:

                screen.blit(background, (0, 0))
                paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                screen.blit(paddle, (paddleposx, paddleposy))
                screen.blit(ball, (xpos, ypos))
                pygame.display.update()

            if ballrect.colliderect(paddlerect):
                text = FONT.render("Collision!", True, BLACK)
                screen.blit(background, (0, 0))
                screen.blit(text, (50, 50))
                pygame.display.update()


            
if __name__ == "__main__":
    main()
