import os
from pygame import Vector2
from sprites.game_sprite import GameSprite
dirname = os.path.dirname(__file__)

class Tile(GameSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_dirt.png")
        super().__init__(pos, path)

    # def update(self, pos=Vector2(0,0)):
    #     super().update(pos)
