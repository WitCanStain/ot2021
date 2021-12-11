import os
from sprites.actor_sprite import ActorSprite
dirname = os.path.dirname(__file__)

class Coin(ActorSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_coin.png")
        sprite_type = "coin"
        super().__init__(pos, path)
