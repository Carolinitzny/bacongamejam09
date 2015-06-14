import pygame

player = pygame.image.load("gfx/player.png")
head = pygame.image.load("gfx/head.png")
body = pygame.image.load("gfx/body.png")

bubble = pygame.image.load("gfx/bubble.png")

shark = pygame.image.load("gfx/shark.png")
warningSign = pygame.image.load("gfx/warning.png")
hunger = pygame.image.load("gfx/hunger.png")

fish01 = pygame.image.load("gfx/fish01.png")
fish02 = pygame.image.load("gfx/fish02.png")
fishes = [fish01, fish02]

floor = pygame.image.load("gfx/floor.png")
rock01 = pygame.image.load("gfx/rock01.png")
seaweed01 = pygame.image.load("gfx/seewead01.png")
seaweed02 = pygame.image.load("gfx/seewead02.png")
seaweed03 = pygame.image.load("gfx/seewead03.png")
seaweed04 = pygame.image.load("gfx/seewead04.png")
seaweed05 = pygame.image.load("gfx/seewead05.png")
seaweed06 = pygame.image.load("gfx/seewead06.png")
seaweed07 = pygame.image.load("gfx/seewead07.png")

seaweed = [seaweed01,seaweed02, seaweed03, seaweed04, seaweed05, seaweed06, seaweed07]

gradient = pygame.image.load("gfx/gradient.png")
rays = pygame.image.load("gfx/rays.png")

tutorial_food = pygame.image.load("gfx/tutorial/food.png")
tutorial_player = pygame.image.load("gfx/tutorial/player.png")
tutorial_shark = pygame.image.load("gfx/tutorial/shark.png")
tutorial_next = pygame.image.load("gfx/tutorial/next.png")
tutorial_gameover = pygame.image.load("gfx/tutorial/gameover.png")
tutorial_starved = pygame.image.load("gfx/tutorial/starved.png")

nom01 = pygame.mixer.Sound("snd/nom01.ogg")
nom02 = pygame.mixer.Sound("snd/nom02.ogg")
nom03 = pygame.mixer.Sound("snd/nom03.ogg")
nom04 = pygame.mixer.Sound("snd/nom04.ogg")
nom05 = pygame.mixer.Sound("snd/nom05.ogg")

nom = [nom01, nom02, nom03, nom04, nom05]

font = pygame.font.Font('font/Ranchers-Regular.ttf', 50)