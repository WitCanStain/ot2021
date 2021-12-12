import os
import pygame
from sprites.game_sprite import GameSprite

dirname = os.path.dirname(__file__)

class Button(GameSprite):
    def __init__(self, pos, img, name):
        path = os.path.join(dirname, "..", "assets", img)
        self.name = name
        super().__init__(pos, path)
    