import pygame #imports the pygame library

from pygame.locals import *
pygame.init() #initialises all the methods of pygame

red = (0,200,255)

screen = pygame.display.set_mode((400,500))
font = pygame.font.Font("freesansbold.ttf", 24)

while True:
    screen.fill((200,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #deavtivated the pygame library and then the program
            pygame.quit()

            quit()
        pygame.display.update()


