from pygame import Vector2
from sprites.game_sprite import GameSprite

class ActorSprite(GameSprite):
    """This class contains functionality specific to sprites that the player can interact with.

    Args:
        GameSprite: Inherits the GameSprite class.
    """
    def __init__(self, pos, path, max_speed=0, collides=True):
        super().__init__(pos, path, collides)
        self.velocity = Vector2()
        self.max_speed = max_speed
        self.max_fall_speed = 10


    def check_speed(self, direction=Vector2()):
        """Checks whether the given vector exceed the allowed speeds for the sprite and corrects if necessary.

        Args:
            direction: The direction vector that is being checked. Defaults to Vector2().

        Returns:
            direction: the rectified direction vector.
        """
        if abs(direction.x) > self.max_speed:
            direction.x = self.max_speed if direction.x > self.max_speed else -self.max_speed
        if abs(direction.y) > self.max_fall_speed:
            direction.y = self.max_fall_speed if direction.y > self.max_fall_speed else -self.max_fall_speed

        return direction

    def update_velocity(self, velocity):
        self.velocity = self.check_speed(self.velocity + velocity)

    def get_state(self):
        """Returns the instance variables alongside the parent class' variables.

        Returns:
            state: the current class' variable concatenated with the parent class variables.
        """
        data = {
            "velocity": self.velocity,
            "max_speed": self.max_speed,
            "max_fall_speed": self.max_fall_speed
        }
        return super().get_state() | data