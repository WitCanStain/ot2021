import pygame
import os


dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "ot_player_stand.png")
        )


        self.rect = self.image.get_rect(topleft = pos)

        print(self.rect.x)
        print(self.rect.y)