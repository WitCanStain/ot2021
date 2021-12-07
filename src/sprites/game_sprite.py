import pygame
from pygame import Vector2

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = pos)

    def update_pos(self, pos=pygame.Vector2()):
        self.rect.x += pos.x
        self.rect.y += pos.y

    def get_pos(self):
        return Vector2(self.rect.x, self.rect.y)

    def get_rect(self):
        return self.rect

    def get_bounds(self):
        left = self.rect.topleft[0]
        top = self.rect.topleft[1]
        right = self.rect.bottomright[0]
        bottom = self.rect.bottomright[1]

        return left, top, right, bottom
