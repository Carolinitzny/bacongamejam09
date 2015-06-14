import pygame
import math
from random import randint, random, uniform, choice

from base import *
from vector import Vector
from resources import bubble
from util import draw


class Bubble(Drawable, Updatable, Mortal):

    def __init__(self, pos, scale=1):
        Drawable.__init__(self)
        Updatable.__init__(self)
        Mortal.__init__(self)

        self.size = uniform(0.01, 0.1) * scale
        self.pos = pos
        self.velocity = Vector(uniform(-0.02, 0.02), uniform(-0.4, -0.6))
        self.lifetime = 0

    def update(self, dt, world):
        self.lifetime += dt
        self.pos += self.velocity * dt
        self.size *= 1 + dt * 0.1

        if self.lifetime > 2:
            self.die()


    def draw(self, surface, camera):
        draw(surface, bubble, self.pos, size=Vector(self.size, None), camera=camera, alpha=1-0.5*self.lifetime)


