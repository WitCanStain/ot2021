import os
from sprites.game_sprite import GameSprite
dirname = os.path.dirname(__file__)

class Coin(GameSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_coin.png")
        super().__init__(pos, path)