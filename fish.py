import pygame
import math
from random import randint, random, uniform, choice

import effects
from base import *
from vector import Vector
from resources import fishes
from config import screensize, worldsize
from util import draw
from player import Player



class Fish(Drawable, Updatable, Mortal):

    def __init__(self, player):
        Drawable.__init__(self)
        Mortal.__init__(self)

        self.size = uniform(0.2, 0.35)
        self.color = (randint(100, 255),randint(100, 255),randint(100, 255))
        self.image = effects.apply(choice(fishes), effects.Multiply(self.color))
        self.dir = 1
        self.angle = 0
        self.pos = Vector(choice([-1, 1]) * 1.1 * worldsize.x * 0.5 + player.pos.x, uniform(-0.5,0.4)*worldsize.y)

        self.player = player
        self.velocity = Vector(uniform(-1, 1),0)
        self.time = uniform(0, math.pi)
        self.frequency = uniform(1, 15)
        self.fear = False

    def update(self, dt):
        dist = (self.player.pos - self.pos).length
        #if ( dist < 0.5 :
            # self.dir *= -1

        self.pos += dt*self.velocity * (3 if self.fear else 1)
        #stirbt, wenn er zu weit vom Player weg ist
        if dist > 10:
            self.die()
        if 0 < self.player.eating < 0.1 and dist < 0.5:
            self.player.score += 1
            self.player.life += 0.1
            self.die()

        self.fear = self.player.eating > 0.1 and dist < 2





        self.time += dt

        self.velocity.y = -self.velocity.x * math.sin(self.time * self.frequency) * 0.1
        self.angle = math.sin(self.time * self.frequency) * 0.1

        self.dir = -1 if self.velocity.x < 0 else 1


    def draw(self, surface, camera):
        draw(surface, self.image, self.pos, size=Vector(self.size, None),scale=Vector(self.dir, 1), angle=self.angle, camera=camera)


