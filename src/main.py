import pygame, os, sys
from settings import *
from sprites.tiles import Tile
from level import Level
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height), RESIZABLE)
clock = pygame.time.Clock()
level = Level(level_map, screen)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type == VIDEORESIZE:
        #     screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        #     pygame.display.update()

    screen.fill('black')
    level.draw()
    pygame.display.update()
    clock.tick(60)

