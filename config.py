import pygame
from vector import Vector

screensize = Vector(1000, 800)
fullscreen = True

if fullscreen:
    # screensize = Vector(*pygame.display.list_modes()[0])
    screensize = Vector(1920, 1080)
    print screensize

scalefactor = screensize.x/5.0
worldsize = screensize/scalefactor