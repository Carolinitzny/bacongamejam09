import math
import pygame

from base import *
from vector import Vector
from resources import player


def mydraw(surface,img, position, angle=0, scale=None, origin=Vector(0.5,0.5)):
    if scale != None:
        #flip
        fx, fy = scale.x < 0 , scale.y < 0
        if fx or fy:
            img = pygame.transform.flip(img, fx, fy)

        w = abs(int(round(img.get_width() * scale.x)))
        h = abs(int(round(img.get_height() * scale.y)))

        if w == 0 or h == 0:
            return
        
        
        img = pygame.transform.scale(img, (w,h))

    origin =origin - Vector(0.5,0.5) 
    origin *= Vector(img.get_width(), img.get_height())
    origin = origin.rotate(angle)

    img = pygame.transform.rotate(img, math.degrees(angle))
    position = position - origin - Vector(img.get_width(), img.get_height())/2.0
    surface.blit(img, position.tuple)

class Player(Drawable, Updatable, MouseClickListener):
    def __init__(self):
        self.pos = Vector(400, 300)
        self.size = 1
        #Richtung in die er schaut (1 nach rechts, -1 nach links)
        self.dir = 1
        self.speed = 1
        self.time = 0

    def update(self, dt):
        self.time += dt





    def draw(self, surface):
        mydraw(surface, player, self.pos, scale=self.size * Vector(self.dir,1))
