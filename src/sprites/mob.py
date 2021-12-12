import os
from pygame import Vector2
from sprites.actor_sprite import ActorSprite


dirname = os.path.dirname(__file__)

class Mob(ActorSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_mob.png")
        max_speed = 3
        self.direction = Vector2(1, 0)
        super().__init__(pos, path, max_speed)

    def get_state(self):
        data = {"direction": self.direction}
        return super().get_state() | data