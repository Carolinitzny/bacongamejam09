import pygame
from random import choice, randint, uniform

from base import *
from player import Player
from util import draw
from vector import Vector
from resources import rock01, seaweed
from config import worldsize

class Hideout(Drawable, Updatable):
    def __init__(self, player, x):
        self.size = 0.7

        self.pos = Vector(x, worldsize.y*0.5)
        self.image = choice([rock01, choice(seaweed)])
        self.player = player
        self.is_player_hiding = False

    def update(self,dt):
        pass
    def draw(self, surface, camera):
        draw(surface, self.image, self.pos, size=Vector(None,3),origin=Vector(0.5,1),camera=camera)