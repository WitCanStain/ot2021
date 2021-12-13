import os
import pygame

dirname = os.path.dirname(__file__)
pygame.mixer.init()

collect_coin = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "collect_coin.wav"))
mob_death = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "mob_death.wav"))
game_win = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "game_win.wav"))
game_over = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "game_over.wav"))
