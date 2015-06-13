import math
import pygame

from base import *
from vector import Vector
from resources import player
from config import screensize, worldsize
from util import draw

class Player(Drawable, Updatable, Mortal, MouseClickListener):
    def __init__(self):
        self.pos = Vector(0, 0)
        self.size = 1
        #Richtung in die er schaut (1 nach rechts, -1 nach links)
        self.dir = 1
        self.speed = 1
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
        self.pos += self.velocity * dt * boost

        self.dir = -1 if self.velocity.x < 0 else 1
        self.angle = v.y/2* -self.dir * speed

    def onMouseClick(self, button, position):
        if button == 3:
            self.light = 1 - self.light
        if button == 1:
            self.eating = 1



    def draw(self, surface, camera):
        draw(surface, player, self.pos, size=Vector(self.size, None),scale =Vector(self.dir, 1), angle=self.angle, camera=camera)
