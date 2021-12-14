import os
import unittest
import pygame

from gamelogic.level import Level
from utils.settings import *
class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        


    def test_player_wins_when_all_coins_are_collected(self):
        level = Level(test_map_coin, self.screen)
        for i in range(100):
            if not level.game_win_flag:
                level.draw()
                level.move_player_left()
        self.assertTrue(level.game_win_flag)

    def test_player_loses_when_collide_with_mob(self):
        level = Level(test_map_mob, self.screen)
        for i in range(100):
            if not level.game_over_flag:
                level.draw()
                level.move_player_right()

        self.assertTrue(level.game_over_flag)

    def test_restarting_resets_player_coins(self):
        level = Level(test_map_two_coins, self.screen)
        for i in range(100):
                level.draw()
                level.move_player_left()
        self.assertEqual(level.player.coins, 1)
        level.restart()
        self.assertEqual(level.player.coins, 0)
    
    def test_player_can_jump(self):
        level = Level(test_map_coin, self.screen)
        y_coord = level.player.rect.top
        level.player_jump()
        level.draw()
        self.assertTrue(level.player.rect.top > y_coord)

    def test_menu_toggle_toggles_menu(self):

        level = Level(test_map_coin, self.screen)

        level.menu_toggle()
        self.assertTrue(level.menu_showing)

        level.menu_toggle()
        self.assertFalse(level.menu_showing)

    def test_pause_toggle_toggles_pause(self):

        level = Level(test_map_coin, self.screen)

        level.pause_toggle()
        self.assertTrue(level.paused)

        level.pause_toggle()
        self.assertFalse(level.paused)

