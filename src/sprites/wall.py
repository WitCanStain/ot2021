import os
from sprites.game_sprite import GameSprite
dirname = os.path.dirname(__file__)

class Wall(GameSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_dirt.png")
        sprite_type = "wall"
        super().__init__(pos, path)
