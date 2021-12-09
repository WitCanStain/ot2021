import pygame
from pygame import Vector2
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, path, collides=True):
        super().__init__()
        self.image = pygame.image.load(path)
        self.img_left = self.image
        self.img_right = pygame.transform.flip(self.img_left, True, False)
        self.rect = self.image.get_rect(topleft = pos)
        self.collides = collides
        self.active = True
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
        
    def off_screen(self):
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
