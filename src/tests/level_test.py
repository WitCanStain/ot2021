import os
import unittest
import pygame
from pygame import Vector2
from gamelogic.level import Level
from utils.settings import *
class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.test_map_coin = [
        '021 ',
        '0000'
        ]
        self.test_map_mob = [
        '213',
        '000'
        ]
        self.test_map_two_coins = [
        '0212',
        '0000'
        ]
        

    def test_player_wins_when_all_coins_are_collected(self):

        

        level = Level(self.test_map_coin, self.screen)
        for i in range(100):
            if not level.game_win_flag:
                level.draw()
                level.move_player_left()
        self.assertTrue(level.game_win_flag)

    def test_player_loses_when_collide_with_mob(self):
        

        level = Level(self.test_map_mob, self.screen)
        for i in range(100):
            if not level.game_over_flag:
                level.draw()
                level.move_player_right()

        self.assertTrue(level.game_over_flag)

    def test_restarting_resets_coins(self):

        level = Level(self.test_map_two_coins, self.screen)
        self.assertEqual(len(level.coins), 2)

        for i in range(100):
                level.draw()
                level.move_player_left()
        self.assertEqual(len(level.coins), 1)
        level.restart()
        self.assertEqual(len(level.coins), 2)
    
    def test_player_can_jump(self):
        
        level = Level(self.test_map_coin, self.screen)
        y_coord = level.player.rect.top
        level.player_jump()
        level.draw()
        self.assertTrue(level.player.rect.top > y_coord)

    def test_menu_toggle_toggles_menu(self):

        level = Level(self.test_map_coin, self.screen)

        level.menu_toggle()
        self.assertTrue(level.menu_showing)

        level.menu_toggle()
        self.assertFalse(level.menu_showing)

    def test_pause_toggle_toggles_pause(self):

        level = Level(self.test_map_coin, self.screen)

        level.pause_toggle()
        self.assertTrue(level.paused)

        level.pause_toggle()
        self.assertFalse(level.paused)

    def test_clicking_on_resume_button_resumes_game(self):
        level = Level(self.test_map_coin, self.screen)
        self.assertFalse(level.menu_showing)
        level.menu_toggle()
        self.assertTrue(level.menu_showing)
        level.button_clicked(Vector2(level.resume_btn.left + 2, level.resume_btn.top + 2))
        self.assertFalse(level.menu_showing)

