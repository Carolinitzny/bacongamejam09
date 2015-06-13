import pygame
import math
from random import randint, random, uniform, choice

import effects
from base import *
from vector import Vector
from resources import fish01
from config import screensize, worldsize
from util import draw
from player import Player



class Fish(Drawable, Updatable, Mortal):

    def __init__(self, player):
        super(Fish, self).__init__()
        self.size = 0.3
        self.color = (randint(100, 255),randint(100, 255),randint(100, 255))
        self.image = effects.apply(fish01, effects.Multiply(self.color))
        self.dir = 1
        self.angle = 0
        self.pos = Vector(choice((-1,1))* 1.1 * worldsize.x* 0.5 + player.pos.x, uniform(-0.5,0.5)*worldsize.y)
        
        self.player = player
        self.velocity = Vector(uniform(-1,1),0)

    def update(self, dt):
        dist = (self.player.pos - self.pos).length 
        #if ( dist < 0.5 :
            # self.dir *= -1

        self.pos += dt*self.velocity 
        #stirbt, wenn er zu weit vom Player weg ist
        if dist > 10:
            self.die()


    def draw(self, surface, camera):
        draw(surface, self.image, self.pos, size=Vector(self.size, None),scale =Vector(self.dir, 1), angle=self.angle, camera=camera)


