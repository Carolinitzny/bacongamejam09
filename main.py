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

# http://freesound.org/people/klankbeeld/sounds/137109/
pygame.mixer.music.load('snd/background.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()

import resources
from player import Player
from base import *
from fish import Fish
from floor import Floor
from shark import Shark
from warning import WarningSign
from hideout import hideout_choices
from hunger import Hunger
from score import Score

fishtimer = 0
sharktimer = 10
left = 0
right = 0
tutorial = 3
tutorial_images = list(reversed([resources.tutorial_player, resources.tutorial_food, resources.tutorial_shark]))
game_running = False

def generate(start, end):
    # num = int(round(0.6 * (end - start) * random()))

    for x in range(int(round(start)), int(round(end))):
        if random() > 0.3: continue
        HideoutClass = choice(hideout_choices)
        hideout = HideoutClass(player, x + uniform(-0.5, 0.5))
        world.append(hideout)


    global left, right
    left = min(left,start)
    right = max(right, end)

world = []

def start_game():
    global world, game_running, player, warningSign, floor, hunger, score
    world = []
    floor = Floor()
    world.append(floor)
    player = Player(camera)
    world.append(player)
    warningSign = WarningSign()
    world.append(warningSign)
    hunger = Hunger(player)
    world.append(hunger)
    score = Score(player)
    world.append(score)

    generate(-10, 10)
    game_running = True

camera = Camera(scale=scalefactor)


lightSurface = pygame.Surface(screensize.tuple, pygame.SRCALPHA)
lightIntensity = 1

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
            elif event.key == pygame.K_s:
                world.append(Shark(player))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if tutorial > 0:
                tutorial -= 1
                if tutorial <= 0:
                    start_game()

            else:
                for a in world:
                    if isinstance(a, MouseClickListener):
                        a.onMouseClick(event.button, event.pos)

    #update
    if game_running:
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


    if game_running:
        f = dt * 2
        camera.translate.x = camera.translate.x * (1 - f) + f * player.pos.x
        # camera.translate.x += dt * 0.7

    def alive(a):
        return not isinstance(a, Mortal) or a.alive
    world = filter(alive, world)

    if game_running:
        # check for sharks
        warningSign.shark_alive = False
        for a in world:
            if isinstance(a, Shark):
                warningSign.shark_alive = True


    #draw
    screen.fill((18,40,70))

    for a in world:
        if isinstance(a, Drawable) and a.lighting:
            a.draw(screen, camera)

    if game_running:
        # light drawing
        if player.light: lightIntensity += dt * 2
        else: lightIntensity -= dt * 2
        lightIntensity = min(1, max(0, lightIntensity))

        f = 30 + lightIntensity * 90
        lightSurface.fill((f, f, f))

        lightPos = player.getLightPosition()
        size = 5 if player.light else 3
        draw(lightSurface, resources.gradient, lightPos, size=Vector(size, size), camera=camera)
        screen.blit(lightSurface, (0, 0), special_flags=pygame.BLEND_MULT)
        if player.light:
            draw(screen, resources.gradient, lightPos, size=Vector(0.5, 0.5), camera=camera)

        if not player.alive:
            game_running = False
            tutorial = 4
            world = []

    for a in world:
        if isinstance(a, Drawable) and not a.lighting:
            a.draw(screen, camera)

    if not game_running:
        if tutorial <= 3:
            img = tutorial_images[tutorial-1]
        else:
            img = [resources.tutorial_starved, resources.tutorial_gameover][player.death_reason]
            score.draw(screen, camera)
        camera.translate = Vector(0, 0)
        draw(screen, img, Vector(0, 0), size=Vector(2, None), camera=camera)
        draw(screen, resources.tutorial_next, worldsize * 0.4, size=Vector(0.5, None), camera=camera)

    pygame.display.flip()




