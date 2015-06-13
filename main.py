#!/usr/bin/env python2
import pygame 
import sys

pygame.init()
screen = pygame.display.set_mode((824, 720))
clock = pygame.time.Clock()


import resources
from player import Player 
from base import *


world = []
player = Player()
world.append(player)


#main loop
while True:
    #Zeit in Sekunden
    dt = clock.tick(60)/1000.0
    #eventloop
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            elif event.key == pygame.K_p:
                pygame.draw.rect( screen ,(0, 150,0), (0,0, 100 , 50))  
    
    for a in world:
        if isinstance(a, Updatable):
            a.update(dt)

    screen.fill((5,12,20))
    


    for a in world:
        if isinstance(a, Drawable):
            a.draw(screen)



    pygame.display.flip()




