import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]