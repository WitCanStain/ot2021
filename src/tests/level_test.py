import unittest
import pygame

from level import Level
from settings import *
class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.level = Level(level_map, screen)


    def test_all_sprites_has_player(self):
        self.assertTrue(self.level.get_all_sprites().has(self.level.get_player()))
