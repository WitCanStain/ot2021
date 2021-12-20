import os
import unittest
import pygame
from gamelogic.level import Level
from utils.game_file import GameFile
from utils.settings import *


class TestGameFile(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def test_can_save_game(self):
        test_map_two_coins = [
        '0212',
        '0000'
        ]
        level = Level(test_map_two_coins, self.screen)
        level.draw()
        level.move_player_left()
        level.draw()
        level.draw()
        self.assertTrue(GameFile.save_game(level.get_state(), "testsave"))

    def test_can_load_game(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "saved_games", "testsave")
        game_state = GameFile.load_game(path)
        level = Level(LEVEL_MAP, self.screen, game_state)
        self.assertEqual(len(level.coins), 2)