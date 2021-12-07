import os
import pygame
from sprites.actor_sprite import ActorSprite

dirname = os.path.dirname(__file__)

class Player(ActorSprite):
    def __init__(self, pos):
        path = os.path.join(dirname, "..", "assets", "ot_player_stand.png")
        max_speed = 3
        super().__init__(pos, path, max_speed)
        

    

