import math
import pygame

from base import *
from vector import Vector
from resources import player
from config import screensize, worldsize
from util import draw
from random import random, randint

from bubble import Bubble

class Player(Drawable, Updatable, Mortal, MouseClickListener):
    def __init__(self):
        super(Player, self).__init__()

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

    def update(self, dt):
        from main import camera
        m = Vector(* pygame.mouse.get_pos())
        v = (camera.ray(m) - self.pos)
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
            boost = 5
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

        # sometimes, spawn bubbles
        if random() < dt*2:
            from main import world
            for x in range(randint(0, 10)):
                world.insert(0, Bubble(self.pos + Vector(random()-0.5, random()-0.5) * 0.1  ))


    def onMouseClick(self, button, position):
        if button == 3:
            self.light = 1 - self.light
        if button == 1:
            self.eating = 1



    def draw(self, surface, camera):
        draw(surface, player, self.pos, size=Vector(self.size, None),scale =Vector(self.dir, 1), angle=self.angle, camera=camera)
