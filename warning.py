import math
from base import *
from vector import Vector
from resources import warningSign
from config import screensize
from util import draw

class WarningSign(Drawable):
    def __init__(self):
        Drawable.__init__(self)
        self.lighting = False
        self.sharktimer = 0

    def draw(self, surface, camera):
        should_draw = False
        if self.shark_alive:
            should_draw = True
        elif 0 < self.sharktimer < 4:
            should_draw = math.sin(self.sharktimer * math.pi * 2 * 4) < 0

        if should_draw:
            draw(surface, warningSign, Vector(screensize.x/2, 50), origin=Vector(0.5, 0), size=Vector(100, None))
