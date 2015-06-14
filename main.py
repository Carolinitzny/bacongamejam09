#!/usr/bin/env python2
import pygame
pygame.init()

import sys
from random import uniform, random


from vector import Vector
from config import screensize, fullscreen , scalefactor, worldsize
from camera import Camera

screen = pygame.display.set_mode(screensize.tuple)
clock = pygame.time.Clock()


import resources
from player import Player
from base import *
from fish import Fish
from floor import Floor
from shark import Shark
from warning import WarningSign
from hideout import Hideout

fishtimer = 0
sharktimer = 10
left = 0
right = 0

def generate(start, end):
    num = int(round(0.2 * (end - start) * random()))
    for i in range(num):
        hideout = Hideout(player, uniform(start,end))
        world.append(hideout)


    global left, right
    left = min(left,start)
    right = max(right, end)

world = []
floor = Floor()
world.append(floor)
player = Player()
world.append(player)
warningSign = WarningSign()
world.append(warningSign)

camera = Camera(scale=scalefactor)

generate(-10, 10)
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

    sharktimer -= dt
    if sharktimer <= 0:
        shark = Shark(player)
        world.append(shark)
        sharktimer = uniform(10, 20)
    warningSign.sharktimer = sharktimer

    if player.pos.x + worldsize.x > right:
        generate(right, right + worldsize.x)
    elif player.pos.x - worldsize.x < left:
        generate(left-worldsize.x, left)



    for a in world:
        if isinstance(a, Updatable):
            a.update(dt)

    f = dt * 1
    camera.translate.x = camera.translate.x * (1 - f) + f * player.pos.x

    def alive(a):
        return not isinstance(a, Mortal) or a.alive
    world = filter(alive, world)

    #draw
    screen.fill((18,40,70))

    for a in world:
        if isinstance(a, Drawable):
            a.draw(screen, camera)

    pygame.display.flip()




