import os
import unittest
import pygame
from gamelogic.level import Level
from utils.game_file import GameSave
from utils.settings import *


class TestSaveGame(unittest.TestCase):

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
        self.assertTrue(GameSave.save_game(level.get_state()))

    def test_can_load_game(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "saved_games", "testsave")
        game_state = GameSave.load_game(path)
        level = Level(LEVEL_MAP, self.screen, game_state)
        self.assertEqual(len(level.coins), 3)