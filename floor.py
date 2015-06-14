import pygame
import math

from base import *
from util import draw
from resources import floor, rays
from config import worldsize
from vector import Vector

class Floor(Drawable):
    def draw(self,surface,camera):
        w = worldsize.x
        x = math.floor(camera.translate.x / w) * w
        draw(surface, rays, Vector(0, 0), origin=Vector(0, 0))
        for dx in (-1, 0, 1):
            draw(surface, floor, Vector(x + dx * w, worldsize.y/2 + 0.1) , origin=Vector(0,1), size=Vector(worldsize.x, None), camera=camera)
