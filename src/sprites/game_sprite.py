import pygame
from pygame import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class GameSprite(pygame.sprite.Sprite):
    """The parent class for all game sprites, containing functionality common to all sprites.

    """
    def __init__(self, pos, path, collides=True):
        """Initialise game sprite values.

        Args:
            pos (Vector2): initial position of the sprite
            path (path): path to the sprite image
            collides (bool, optional): Value indicating whether the sprite collides with other sprites. Defaults to True.

        Attributes:
            self.image: the image representing the sprite.
            self.img_left: the sprite facing left.
            self.img_right: the sprite facing right.
            self.rect: the rect object of the sprite, containing the coordinates of the sprite.
            self.collides: boolean value indicating whether the sprite detects collisions with other sprites
            self.active: boolean value indicating whether the sprite is still in the game
        """
        super().__init__()
        self.image = pygame.image.load(path)
        self.img_left = self.image
        self.img_right = pygame.transform.flip(self.img_left, True, False)
        self.rect = self.image.get_rect(topleft=pos)
        self.collides = collides
        self.active = True
        self._left = self.rect.topleft[0]
        self._top = self.rect.topleft[1]
        self._right = self.rect.bottomright[0]
        self._bottom = self.rect.bottomright[1]


    def update_pos(self, direction=pygame.Vector2()):
        self.rect.x += round(direction.x)
        self.rect.y += round(direction.y)
        
    def update(self, direction=Vector2()):
        self.rect.x = round(self._left)
        self.rect.y = round(self._top)
        
    def off_screen(self):
        """Returns a boolean value indicating whether the sprite is currently within screen bounds.

        Returns:
            Bool: value indicating whether sprite is within screen.
        """
        if self._right < 0 or self._left > SCREEN_WIDTH or self._top < 0 or self._bottom > SCREEN_HEIGHT:
            return True
        return False

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        x_shift = value - self._left
        self._left = value
        self._right += x_shift

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        x_shift = value - self._right
        self._right = value
        self._left += x_shift

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        y_shift = value - self._top
        self._top = value
        self._bottom += y_shift

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        y_shift = value - self._bottom
        self._bottom = value
        self._top += y_shift

    def get_state(self):
        """Returns the state of the instance variables.

        Returns:
            [type]: [description]
        """
        state = {
            "pos": self.rect.topleft,
            "collides": self.collides,
            "active": self.active,
        }
        return state
