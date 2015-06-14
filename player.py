import math
import pygame

from base import *
from vector import Vector
from resources import head, body
from config import screensize, worldsize
from util import draw
from random import random, randint

from bubble import Bubble

class Player(Drawable, Updatable, Mortal, MouseClickListener):
    def __init__(self, camera):
        Drawable.__init__(self)
        Mortal.__init__(self)

        self.pos = Vector(0, 0)
        self.size = 1
        #Richtung in die er schaut (1 nach rechts, -1 nach links)
        self.dir = 1
        self.speed = 2
        self.time = 0
        self.angle = 0
        self.light = 1
        self.velocity = Vector(0,0)
        self.eating = 0
        self.camera = camera
        self.is_hidding_in = None

    def update(self, dt):
        self.light = self.is_hidding_in == None
        self.is_hidding_in = None
        m = Vector(* pygame.mouse.get_pos())
        v = (self.camera.ray(m) - self.pos)
        #untere Grenze
        if self.pos.y > worldsize.y/2.0 - 0.5:
            self.pos.y = worldsize.y/2.0 - 0.5
        #obere Grenze
        if self.pos.y < - worldsize.y/2.0 :
            self.pos.y = - worldsize.y/2.0

        speed = (v.length - 0.5) / 2
        speed = min(1, max(0, speed))
        if v:
            v = v.normalize()

        boost = 1
        if self.eating > 0:
            boost = (1-self.eating) * 5
            self.eating -= dt

        v2 =  v * self.speed * speed
        f = dt * 2
        self.velocity = v2 * f + self.velocity * (1 - f)
        self.velocity.y *= (1 - dt * 0.1)
        self.pos += self.velocity * dt * boost

        self.dir = -1 if self.velocity.x < 0 else 1

        # winkel setzen in richtung der velocity
        self.angle = -self.velocity.angle
        # winkel richtung x-achse halbieren
        if abs(self.angle) > math.pi/2:
            self.angle = math.pi - (math.pi - self.angle)/2 + (math.pi if self.angle > 0 else 0)
        else:
            self.angle /= 2

        # create image to blit to
        self.imagesize = Vector(body.get_width(), body.get_height())
        self.image = pygame.Surface(self.imagesize.tuple, pygame.SRCALPHA)


    def onMouseClick(self, button, position):
        if button == 3:
            self.light = 1 - self.light
        if button == 1:
            self.eating = 1

    def relpos(self, pos):
        pos = pos.rotate(-self.angle)
        if self.dir < 0: pos *= -1
        return self.pos + pos

    def getMouthPosition(self):
        return self.relpos(Vector(0.3, 0))

    def getLightPosition(self):
        return self.relpos(Vector(0.47, -0.05))

    def draw(self, surface, camera):
        self.image.fill((0, 0, 0, 0))
        draw(self.image, body, Vector(0, 0), origin=Vector(0, 0))
        angle = (0 if self.eating <= 0 else 1-self.eating)
        draw(self.image, head, self.imagesize * Vector(0.55, 0.54), origin=Vector(0.1, 0.5), angle=angle)

        draw(surface, self.image, self.pos, size=Vector(self.size, None),scale=Vector(self.dir, 1), angle=self.angle, camera=camera)
