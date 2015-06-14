import pygame

from util import draw
from base import Drawable
from resources import hunger
from config import screensize
from vector import Vector

class Hunger(Drawable):
    def __init__(self, player):
        Drawable.__init__(self)
        self.lighting = False
        self.player = player

    def draw(self, surface, camera):
        draw(surface, hunger, Vector(50, screensize.y - 50))
        px, cy = 100, screensize.y - 50
        w, h, p = 150, 25, 4
        pygame.draw.rect(surface, (255, 255, 255), (px - p, cy - h/2 - p, w+p*2-1, h+p*2-1), 2)
        pygame.draw.rect(surface, (255, 255, 255), (px, cy - h/2, int(round(w * self.player.life)), h))
