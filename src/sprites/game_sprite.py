import pygame
from pygame import Vector2

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = pos)
        self._left = self.rect.topleft[0]
        self._top = self.rect.topleft[1]
        self._right = self.rect.bottomright[0]
        self._bottom = self.rect.bottomright[1]

    def update_pos(self, direction=pygame.Vector2()):
        self.rect.x += round(direction.x)
        self.rect.y += round(direction.y)
        
    def update(self):
        self.rect.x = round(self._left)
        self.rect.y = round(self._top)
        
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
