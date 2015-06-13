import pygame
import math

from vector import Vector

def draw(surface,img, position, angle=0, scale=None, origin=Vector(0.5,0.5)):
    if scale != None:
        #flip
        fx, fy = scale.x < 0 , scale.y < 0
        if fx or fy:
            img = pygame.transform.flip(img, fx, fy)

        w = abs(int(round(img.get_width() * scale.x)))
        h = abs(int(round(img.get_height() * scale.y)))

        if w == 0 or h == 0:
            return
        
        img = pygame.transform.scale(img, (w,h))

    origin =origin - Vector(0.5,0.5) 
    origin *= Vector(img.get_width(), img.get_height())
    origin = origin.rotate(angle)

    img = pygame.transform.rotate(img, math.degrees(angle))
    position = position - origin - Vector(img.get_width(), img.get_height())/2.0
    surface.blit(img, position.tuple)
