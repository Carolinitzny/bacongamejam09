import pygame
import math

from player import Player
from base import *
from resources import shark
from config import screensize, worldsize
from util import draw
from vector import Vector

class Shark(Drawable, Mortal, Updatable):
    def __init__(self, player):
        Drawable.__init__(self)
        Mortal.__init__(self)

        self.x = player.pos.x-worldsize.x
        self.y = -0.45 *worldsize.y
        self.pos = Vector(self.x,self.y)
        self.dir = 1
        self.size = 2
        self.angle = 0
        self.player = player
        self.velocity = Vector(3,0)
        self.alive = True

    def update(self, dt):

        self.pos += self.velocity * dt

    def draw(self, surface, camera):
        draw(surface, shark, self.pos, size=Vector(self.size, None),scale=Vector(self.dir, 1), angle=self.angle, camera=camera)
