import os
import pygame

dirname = os.path.dirname(__file__)
pygame.mixer.init()

collect_coin = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "collect_coin.wav"))
player_death = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "player_death.wav"))
mob_death = pygame.mixer.Sound(os.path.join(dirname, "assets", "sounds", "mob_death.wav"))