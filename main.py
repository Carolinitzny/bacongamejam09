#!/usr/bin/env python2
import pygame
pygame.init()

import sys

from vector import Vector
from config import screensize, fullscreen
from camera import Camera

screen = pygame.display.set_mode(screensize.tuple)
clock = pygame.time.Clock()


import resources
from player import Player
from base import *

world = []
player = Player()
world.append(player)

camera = Camera(scale=screensize.x/5)

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

    for a in world:
        if isinstance(a, Updatable):
            a.update(dt)
    camera.translate = player.pos

    screen.fill((5,12,20))



    for a in world:
        if isinstance(a, Drawable):
            a.draw(screen, camera)



    pygame.display.flip()




