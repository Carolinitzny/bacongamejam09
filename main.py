#!/usr/bin/env python2
import pygame
pygame.init()

import sys
from random import uniform

from vector import Vector
from config import screensize, fullscreen , scalefactor
from camera import Camera

screen = pygame.display.set_mode(screensize.tuple)
clock = pygame.time.Clock()


import resources
from player import Player
from base import *
from fish import Fish
from floor import Floor

fishtimer = 0

world = []
floor = Floor()
world.append(floor)
player = Player()
world.append(player)
fish = Fish(player)
world.append(fish)

camera = Camera(scale=scalefactor)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for a in world:
                if isinstance(a, MouseClickListener):
                    a.onMouseClick(event.button, event.pos)

    #update
    fishtimer -= dt
    if fishtimer <= 0:
        fish = Fish(player)
        world.append(fish)
        fishtimer = uniform(0, 2)

    for a in world:
        if isinstance(a, Updatable):
            a.update(dt)

    f = dt * 1
    camera.translate.x = camera.translate.x * (1 - f) + f * player.pos.x

    #draw
    screen.fill((5,12,20))

    for a in world:
        if isinstance(a, Drawable):
            a.draw(screen, camera)

    pygame.display.flip()




