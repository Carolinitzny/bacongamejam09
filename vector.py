# Taken from https://gist.github.com/mcleonard/5351452, then modified

import math

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def length(self):
        return math.sqrt(sum( comp**2 for comp in self ))

    def normalize(self):
        l = self.length
        return Vector(x/l, y/l)

    def rotate(self, theta):
        dc, ds = math.cos(theta), math.sin(theta)
        return Vector(dc*self.x - ds*self.y, ds*self.x + dc*self.y)

    def __mul__(self, other):
        if type(other) == Vector:
            assert False, "Vector product not defined (yet)."

        assert type(other) in (int, float), "Vector multiplication only with scalars"

        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        assert type(other) in (int, float), "Vector division only with scalars"
        return Vector(self.x / other, self.y / other)

    def __add__(self, other):
        assert type(other) == Vector, "Vector addtion only with vectors"
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        assert type(other) == Vector, "Vector subtraction only with vectors"
        return Vector(self.x - other.x, self.y - other.y)

    def __iter__(self):
        return [self.x, self.y].__iter__()

    def __getitem__(self, key):
        return [self.x, self.y][key]

    def __repr__(self):
        return str((self.x, self.y))

    def __len__(self):
        return self.length

    @property
    def tuple(self):
        return (self.x, self.y)
