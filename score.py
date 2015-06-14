import pygame

from util import draw
from base import Drawable
from resources import font
from config import screensize
from vector import Vector

class Score(Drawable):
    def __init__(self, player):
        Drawable.__init__(self)
        self.lighting = False
        self.player = player

        self.rendered_score = None
        self.img = None
        self.size = None

    def draw(self, surface, camera):
        if not self.img or (self.player.score != self.rendered_score):
            self.img = font.render(str(self.player.score), True, (255, 255, 255))
            self.rendered_score = self.player.score

        draw(surface, self.img, Vector(20, 20), origin=Vector(0, 0))
