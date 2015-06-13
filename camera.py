from vector import Vector
from config import screensize

class Camera(object):
    def __init__(self, translate=Vector(0, 0), scale=Vector(0, 0), rotate=0):
        self.translate = translate

    def apply(self, position=Vector(0, 0), angle=0, scale=Vector(1, 1)):
        position += -self.translate + screensize/2
        return position, angle, scale

