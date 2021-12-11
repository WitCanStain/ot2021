import os
from pygame import Vector2
from sprites.actor_sprite import ActorSprite


dirname = os.path.dirname(__file__)

class Mob(ActorSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_mob.png")
        type = "mob"
        max_speed = 3
        self.coins = 0
        self.direction = Vector2(1, 0)
        super().__init__(pos, path, max_speed)
