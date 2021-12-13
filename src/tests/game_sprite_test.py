import os
import unittest
import pygame
from pygame import Vector2

from sprites.game_sprite import GameSprite
from game_utils.settings import *

dirname = os.path.dirname(__file__)

class TestGameSprite(unittest.TestCase):

    def setUp(self):
        pygame.init()
        path = os.path.join(dirname, "..", "assets", "ot_dirt.png")
        self.sprite = GameSprite(Vector2(), path)

    def test_off_screen_detects_sprite_going_off_screen(self):
        self.sprite.right = -1
        self.assertTrue(self.sprite.off_screen())

    def test_setting_left_changes_right(self):
        
        right = self.sprite.right
        self.sprite.left += 1

        self.assertEqual(self.sprite.right, right + 1)

    