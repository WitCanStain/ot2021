import pygame, os
dirname = os.path.dirname(__file__)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "ot_dirt.png")
        )
        self.rect = self.image.get_rect(topleft = pos)