import os
import unittest
import pygame
from pygame.locals import K_LEFT, K_RIGHT
from game_loop import GameLoop
from gamelogic.level import Level
from utils.settings import *
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE
from gamelogic.level import Level
from utils.game_file import GameFile
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue
from utils.scale_mouse import scale_mouse

class EventQueueStub:
    def __init__(self, event_get=None, event_get_pressed={K_LEFT: False, K_RIGHT: False}):
        self._event_get = event_get
        self._event_get_pressed = event_get_pressed
    def get(self):
        return [self._event_get] if self._event_get else []
    def get_pressed(self):
        return self._event_get_pressed

class EventStub:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key



class TestGameLoop(unittest.TestCase):

    def setUp(self):
        pygame.init()

        level_map = [
            '0  1  202',
            '000000000'
        ]
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.fake_screen = self.screen.copy()
        self.level = Level(level_map, self.fake_screen)

        self.renderer = Renderer(self.screen, self.fake_screen, self.level)
        self.event_queue = EventQueue()

    def test_mouse_pos_is_scaled_correctly(self):
        game_loop = GameLoop(self.renderer, self.event_queue, self.level, self.screen, self.fake_screen)
        game_loop._screen = pygame.display.set_mode((2 * SCREEN_WIDTH, 2* SCREEN_HEIGHT))
        scaled_pos = scale_mouse((2, 2), self.screen, self.fake_screen)
        self.assertEqual(scaled_pos, [1, 1])

    def test_left_key_moves_player_left(self):
        event_queue = EventQueueStub(event_get_pressed={K_LEFT: True, K_RIGHT: False})
        game_loop = GameLoop(self.renderer, event_queue, self.level, self.screen, self.fake_screen)
        self.level.draw()
        player_left_pre = self.level.player.left
        game_loop._handle_events()
        player_left_post = self.level.player.left
        self.assertTrue(player_left_pre > player_left_post)

    def test_right_key_moves_player_right(self):
        event_queue = EventQueueStub(event_get_pressed={K_RIGHT: True, K_LEFT: False})
        game_loop = GameLoop(self.renderer, event_queue, self.level, self.screen, self.fake_screen)
        player_left_pre = self.level.player.left
        self.level.draw()
        game_loop._handle_events()
        player_left_post = self.level.player.left
        self.assertTrue(player_left_pre < player_left_post)

    def test_pressing_r_makes_game_restart(self):
        event = EventStub(pygame.KEYUP, pygame.K_r)
        event_queue = EventQueueStub(event_get=event)
        game_loop = GameLoop(self.renderer, event_queue, self.level, self.screen, self.fake_screen)
        self.level.draw()
        self.assertEqual(len(self.level.coins), 2)
        for i in range(200):
            self.level.move_player_right()
            self.level.draw()
        self.assertEqual(len(self.level.coins), 1)
        game_loop._handle_events()
        self.assertEqual(len(self.level.coins), 2)
