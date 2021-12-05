from sprites.game_sprite import GameSprite
from pygame import Vector2

class ActorSprite(GameSprite):
    def __init__(self, pos, path, max_speed):
        super().__init__(pos, path)
        self.velocity = Vector2()
        self.max_speed = max_speed
        self.max_fall_speed = 10
        

    def update_relative_velocity(velocity):
        self.velocity += velocity

    # def update(self, velocity):
    #     # self.velocity += velocity
    #     super().update(velocity)

    def update(self, velocity=Vector2()):
        if abs(velocity.x) > max_speed:
            velocity.x = max_speed
        if abs(velocity.y) > self.max_fall_speed:
            velocity.y = self.max_fall_speed
        super().update(velocity)

    def get_velocity():
        return self.velocity



    
