import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, pos=pygame.Vector2()):
        self.rect.x += pos.x
        self.rect.y += pos.y
    
    def get_rect(self):
        return self.rect