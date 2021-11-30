import pygame

from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map
from level import Level


class GameLoop:
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(level_map, self.screen)

    def start(self):
        while True:
            if self.handle_events() is False:
                break

            self.render()
            self.clock.tick(60)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.level.move_player((-4, 0))
                if event.key == pygame.K_RIGHT:
                    self.level.move_player((4, 0))
                if event.key == pygame.K_UP:
                    self.level.move_player((0, -4))
                if event.key == pygame.K_DOWN:
                    self.level.move_player((0, 4))
            elif event.type == pygame.QUIT:
                return False
            return True

    def render(self):
        self.screen.fill('black')
        self.level.draw()
        pygame.display.update()
