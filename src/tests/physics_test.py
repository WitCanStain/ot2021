import unittest
import pygame
from physics import check_collision, sprite_touches_floor
from settings import *
from level import Level
class TestPhysics(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.level = Level(test_map_walls, self.screen)

    
    def test_collision_detection_works(self):        
        self.assertTrue(check_collision(self.level.player, self.level.walls, pygame.Vector2(10, 0)))

    def test_sprite_touches_floor_works(self):
        self.assertTrue(sprite_touches_floor(self.level.player, self.level.walls))
        
