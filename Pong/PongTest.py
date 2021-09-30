#This is the botched implementation with everything in it.

import pygame
import random
from pygame.locals import * 

def main():
    pygame.init()

    pygame.display.set_caption("Pong")

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
    x_step = 20
    y_step = 20
    bx_step = 10
    by_step = 10
    screen.blit(ball, (xpos, ypos))
    screen.blit(paddle, (paddleposx, paddleposy))
    paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
    ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))

    clock = pygame.time.Clock()

    pts = 0 #Variable to keep track of how many times the player's successfully hit the ball. Using this as a points system.

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Part below is what controls the edge of the display bits. Still have no idea why the paddle doesn't bounce off the bottom and the ball doesn't bounce off the top though. 
            if xpos > WIDTH - 64 or xpos < 0:
                bx_step = -random.randint(2, 10)
            if ypos > HEIGHT - 64 or ypos < 0:
                by_step = -random.randint(2, 10)

            
            #The code below controls the paddle movement.
            if event.type == KEYDOWN: 

                if event.key == K_UP or event.key == K_w:
                    
                    if paddleposy < 0:
                        while paddleposy < 0:
                            paddleposy += y_step
                            paddlerect = paddle.get_rect(topleft = (paddleposx + 23, paddleposy))
                            ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                            screen.blit(background, (0, 0))
                            screen.blit(paddle, (paddleposx, paddleposy))
                            screen.blit(ball, (xpos, ypos))
                            pygame.display.update()
                            clock.tick(10)
                        
                    else:
                            
                        paddleposy -= y_step
                        paddlerect = paddle.get_rect(topleft = (paddleposx + 23, paddleposy))
                        ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                        screen.blit(background, (0, 0))
                        screen.blit(paddle, (paddleposx, paddleposy))
                        screen.blit(ball, (xpos, ypos))
                        pygame.display.update()
                        clock.tick(10)

                if event.key == K_DOWN or event.key == K_s:

                    if paddleposy > HEIGHT - 64:

                        while paddleposy > HEIGHT - 64: 

                            paddleposy += y_step
                            paddlerect = paddle.get_rect(topleft = (paddleposx + 23, paddleposy))
                            ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                            screen.blit(background, (0, 0))
                            screen.blit(paddle, (paddleposx, paddleposy))
                            screen.blit(ball, (xpos, ypos))
                            pygame.display.update()
                            clock.tick(10)

                    else:
                        paddleposy += y_step
                        paddlerect = paddle.get_rect(topleft = (paddleposx+23, paddleposy))
                        ballrect = paddle.get_rect(topleft = (xpos + 23, ypos))
                        screen.blit(background, (0, 0))
                        screen.blit(paddle, (paddleposx, paddleposy))
                        screen.blit(ball, (xpos, ypos))
                        pygame.display.update()
                        clock.tick(10)

            #This bit is what controls the ball's movement. Perhaps adding this chunk in to the paddle loops will make everything work except the edge of screen issues.
            screen.blit(background, (0, 0))
            screen.blit(ball, (xpos, ypos))
            screen.blit(paddle, (paddleposx, paddleposy))
            xpos += bx_step
            ypos += by_step
            pygame.display.update()
            clock.tick(10)
            

            #This bit is what increments the points. Collision detection works the same as it did in the collision detection program. 
            if ballrect.colliderect(paddlerect):
                pts += 1 
                text = FONT.render(str(pts), True, BLACK)
                screen.blit(text, (300, 300))
                bx_step = -random.randint(2, 10)
                by_step = -random.randint(2, 10)
                screen.blit(ball, (xpos, ypos))
                screen.blit(paddle, (paddleposx, paddleposy))
                pygame.display.update()


            
if __name__ == "__main__":
    main()
