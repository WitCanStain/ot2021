import os
import unittest
import pygame

from level import Level
from game_save import save_game, load_game
from settings import *
class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        


    def test_player_wins_when_all_coins_are_collected(self):
        level = Level(test_map_coin, self.screen)
        level.draw()
        level.move_player_left()
        level.draw()
        level.draw()
        self.assertTrue(level.game_win_flag)

    def test_player_loses_when_collide_with_mob(self):
        level = Level(test_map_mob, self.screen)
        for i in range(100):
            if not level.game_over_flag:
                level.draw()
                level.move_player_right()

        self.assertTrue(level.game_over_flag)

    def test_can_save_game(self):
        level = Level(test_map_save, self.screen)
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

    