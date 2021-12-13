import os
import unittest
import pygame
from level import Level
from game_utils.game_save import save_game, load_game
from game_utils.settings import *


class TestSaveGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def test_can_save_game(self):
        level = Level(test_map_two_coins, self.screen)
        level.draw()
        level.move_player_left()
        level.draw()
        level.draw()
        self.assertTrue(save_game(level.get_state()))

    def test_can_load_game(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "saved_games", "testsave")
        game_state = load_game(path)
        level = Level(level_map, self.screen, game_state)
        self.assertEqual(len(level.coins), 3)