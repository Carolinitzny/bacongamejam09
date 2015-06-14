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

        self.x = player.pos.x - worldsize.x + 0.1
        self.y = -0.45 *worldsize.y
        self.pos = Vector(self.x, self.y)
        self.dir = 1
        self.size = 2
        self.angle = 0
        self.player = player
        self.velocity = Vector(5,0)
        self.alive = True
        self.sees_player = False


    def update(self, dt):
        dist = abs(self.player.pos.x - self.pos.x)

        if dist > worldsize.x*1.3:
            self.die()

        self.sees_player = (self.player.is_hidding_in == None)

        if self.sees_player:
            f = dt * 2
            diff = (self.player.pos - self.pos)
            if diff: diff = diff.normalize() * 4
            self.velocity = self.velocity * (1 - f) + f * diff

            if dist < 0.5:
                self.player.death_reason = 1
                self.player.die()
        else:
            self.velocity.y *= 1 - (2 * dt)

        self.pos += self.velocity * dt
        self.dir = 1 if self.velocity.x > 0 else -1

    def draw(self, surface, camera):
        draw(surface, shark, self.pos, size=Vector(self.size, None),scale=Vector(self.dir, 1), angle=self.angle, camera=camera)
