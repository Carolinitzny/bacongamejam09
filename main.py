#!/usr/bin/env python2
import pygame
pygame.init()

import sys
from random import uniform, random, choice


from vector import Vector
from config import screensize, fullscreen , scalefactor, worldsize
from camera import Camera
from util import draw

screen = pygame.display.set_mode(screensize.tuple)
clock = pygame.time.Clock()


import resources
from player import Player
from base import *
from fish import Fish
from floor import Floor
from shark import Shark
from warning import WarningSign
from hideout import hideout_choices

fishtimer = 0
sharktimer = 10
left = 0
right = 0

def generate(start, end):
    num = int(round(0.2 * (end - start) * random()))
    for i in range(num):
        HideoutClass = choice(hideout_choices)
        hideout = HideoutClass(player, uniform(start,end))
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

lightSurface = pygame.Surface(screensize.tuple, pygame.SRCALPHA)

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
        if isinstance(a, Drawable) and a.lighting:
            a.draw(screen, camera)

    # light drawing
    lightSurface.fill((10, 10, 10))
    lightPos = Vector(0.47, -0.05).rotate(-player.angle)
    if player.dir < 0: lightPos *= -1
    lightPos += player.pos
    if player.light:
        lightSurface.fill((100, 100, 100))
    size = 5 if player.light else 3
    draw(lightSurface, resources.gradient, lightPos, size=Vector(size, size), camera=camera)
    screen.blit(lightSurface, (0, 0), special_flags=pygame.BLEND_MULT)
    if player.light:
        draw(screen, resources.gradient, lightPos, size=Vector(0.5, 0.5), camera=camera)

    for a in world:
        if isinstance(a, Drawable) and not a.lighting:
            a.draw(screen, camera)


    pygame.display.flip()




