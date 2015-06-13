from vector import Vector
from config import screensize

class Camera(object):
    def __init__(self, translate=Vector(0, 0), scale=Vector(0, 0), rotate=0):
        self.translate = translate
        self.scale = scale
        self.rotate = rotate

    def apply(self, position=Vector(0, 0), angle=0, scale=Vector(1, 1)):
        position = self.scale * (position - self.translate) + screensize/2

        scale *= self.scale

        # TODO: rotation
        return position, angle, scale

    def ray(self, pos):
        return (pos - screensize/2) * 1.0 / self.scale + self.translate

