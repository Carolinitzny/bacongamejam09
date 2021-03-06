import pygame
import math

import effects
from vector import Vector

def draw(surface,img, position, angle=0, scale=None, origin=Vector(0.5,0.5), camera=None, size=None, alpha=None, special_flags=0):
    if size != None:
        if scale == None:
            scale = Vector(1 , 1)
        if size.x == None:
            scale *= Vector(size.y * 1.0 / img.get_height(), size.y * 1.0 / img.get_height())
        elif size.y == None:
            scale *= Vector(size.x * 1.0 / img.get_width(), size.x * 1.0 / img.get_width())
        else:
            scale *= Vector(size.x * 1.0 / img.get_width(), size.y * 1.0 / img.get_height())

    if camera :
        position, angle, scale = camera.apply(position, angle, scale or Vector(1, 1))

    if scale != None:
        #flip
        fx, fy = scale.x < 0 , scale.y < 0
        if fx or fy:
            img = pygame.transform.flip(img, fx, fy)

        w = abs(int(round(img.get_width() * scale.x)))
        h = abs(int(round(img.get_height() * scale.y)))

        if w == 0 or h == 0:
            return

        img = pygame.transform.smoothscale(img, (w,h))

    origin = origin - Vector(0.5,0.5)
    origin *= Vector(img.get_width(), img.get_height())
    origin = origin.rotate(-angle)

    img = pygame.transform.rotate(img, math.degrees(angle))
    position = position - origin - Vector(img.get_width(), img.get_height())/2.0

    if alpha != None:
        alpha = min(1, max(0, alpha))
        img = effects.apply(img, effects.Fade(alpha))

    surface.blit(img, position.tuple, special_flags=special_flags)
