from sprites.game_sprite import GameSprite
from pygame import Vector2

class ActorSprite(GameSprite):
    def __init__(self, pos, path, max_speed):
        super().__init__(pos, path)
        self.direction = Vector2()
        self.max_speed = max_speed
        self.max_fall_speed = 10
        

    def update(self, direction=Vector2()):
        # if abs(direction.x) > self.max_speed:
        #     direction.x = self.max_speed if direction.x > self.max_speed else -self.max_speed
        # if abs(direction.y) > self.max_fall_speed:
        #     direction.y = self.max_fall_speed if direction.x > self.max_fall_speed else -self.max_fall_speed
        self.direction = direction
        super().update_pos(direction)

    def get_direction(self):
        return self.direction



    
