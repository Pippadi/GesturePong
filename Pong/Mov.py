#This is the code that controls the movement of the ball. 

import pygame
import random 

def main():
    pygame.init()
    
    pygame.display.set_caption("BingBong")

    WIDTH = 400
    HEIGHT = 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    background = pygame.image.load("bg.png")
    screen.blit(background, (0,0))
    xpos = 5
    ypos = 50
    step_x = 10
    step_y = 10
    img = pygame.image.load("Ball.png")
    screen.blit(img, (xpos, ypos))
    
    pygame.display.update()

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if ypos > HEIGHT - 64 or ypos < 0:
            step_y = -random.randint(2, 10)

            #This bit is what makes the ball bounce off with a random velocity.

        if xpos > WIDTH - 64 or xpos < 0:
            step_x = -random.randint(2, 10)

        #This part is what controls the ball's actual movement.    
        screen.blit(background, (0, 0))
        screen.blit(img, (xpos, ypos))
        xpos += step_x
        ypos += step_y
        pygame.display.update()
        clock.tick(10)



if __name__ == "__main__":
    main()
