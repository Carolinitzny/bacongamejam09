import math
import pygame

from base import *
from vector import Vector
from resources import player
from config import screensize
from util import draw

class Player(Drawable, Updatable, MouseClickListener):
    def __init__(self):
        self.pos = Vector(0, 0)
        self.size = 1
        #Richtung in die er schaut (1 nach rechts, -1 nach links)
        self.dir = 1
        self.speed = 1
        self.time = 0
        self.angle = 0

    def update(self, dt):
        self.time += dt
        m = Vector(* pygame.mouse.get_pos())
        v = (m - screensize/2.0)
        if v.length > 0 :
            v = v.normalize()
            self.pos += v * self.speed * dt
        self.dir = -1 if abs(v.angle) > math.pi/2 else 1
        self.angle = v.y/2* -self.dir

    def draw(self, surface, camera):
        draw(surface, player, self.pos, size=Vector(self.size, None),scale =Vector(self.dir, 1), angle=self.angle, camera=camera)
