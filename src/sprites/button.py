import os
import pygame
from sprites.game_sprite import GameSprite

dirname = os.path.dirname(__file__)

class Button(GameSprite):
    def __init__(self, pos, img_file, name):
        self.img_file = img_file
        path = os.path.join(dirname, "..", "assets", img_file)
        self.name = name
        super().__init__(pos, path)
    
    def get_state(self):
        data = {
            "img_file": self.img_file,
            "name": self.name
        }
        return super().get_state() | data

    