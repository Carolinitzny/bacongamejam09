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

        self.pos = screensize * Vector(0.5, 0.2)
        self.sharktimer = 0

    def draw(self, surface, camera):
        if self.sharktimer > 6: return
        if self.sharktimer < 4:
            blinkspeed = math.ceil(4-self.sharktimer) * 2 * 2 * math.pi
            if math.sin(self.sharktimer * blinkspeed) < 0: return
        draw(surface, warningSign, self.pos)
