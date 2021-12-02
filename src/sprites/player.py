import os
from sprites.game_sprite import GameSprite

dirname = os.path.dirname(__file__)

class Player(GameSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_player_stand.png")
        super().__init__(pos, path)

    def update(self, pos):
        super().update(pos)
