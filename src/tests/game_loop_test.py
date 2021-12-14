import os
import unittest
import pygame
from game_loop import GameLoop
from gamelogic.level import Level
from utils.settings import *


class TestGameLoop(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game_loop = GameLoop()

    def test_mouse_pos_is_scaled_correctly(self):
        self.game_loop.screen = pygame.display.set_mode((2 * SCREEN_WIDTH, 2* SCREEN_HEIGHT))
        scaled_pos = self.game_loop.scale_mouse((2, 2))
        print(scaled_pos)
        self.assertEqual(scaled_pos, [1, 1])
