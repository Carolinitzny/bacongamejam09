import pygame
import math
from random import choice, randint, uniform

from base import *
from player import Player
from util import draw
from vector import Vector
from resources import rock01, seaweed
from config import worldsize
import effects

class Hideout(Drawable, Updatable):
    def __init__(self, player, x):
        Drawable.__init__(self)

        self.pos = Vector(x, worldsize.y*0.45)
        self.player = player
        self.is_player_hiding = False

    def update(self,dt):
        pass

class Rock(Hideout):
    def __init__(self, *args):
        Hideout.__init__(self, *args)

    def draw(self, surface, camera):
        draw(surface, rock01, self.pos, size=Vector(None,1.5),origin=Vector(0.5,1),camera=camera)

class Seaweed(Hideout):
    def __init__(self, *args):
        Hideout.__init__(self, *args)

        self.time = 0
        self.weeds = []
        for i in range(randint(10, 20)):
            f = randint(150, 255)
            img = choice(seaweed)
            # img = effects.apply(img, effects.Multiply([f, f, f]))
            self.weeds.append( ( img, uniform(-1, 1)*0.4, uniform(0, 0.5), uniform(1.2, 2.5)) )

    def update(self, dt):
        Hideout.update(self, dt)
        self.time += dt

    def draw(self, surface, camera):
        for weed in self.weeds:
            image, xOffset, phaseOffset, size = weed

            angle = math.sin(self.time + phaseOffset) * 0.1
            pos = self.pos + Vector(xOffset, 0)
            draw(surface, image, pos, size=Vector(None, size), origin=Vector(0.5,1), angle=angle, camera=camera)

hideout_choices = [Rock, Seaweed]