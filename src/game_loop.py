import pygame
from pygame.locals import *
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map
from level import Level


class GameLoop:
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        self.level = Level(level_map, self.fake_screen)

    def start(self):
        while True:
            if self.handle_events() is False:
                break

            self.render()
            self.clock.tick(60)


    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.level.move_player((-2, 0))
        if keys[K_RIGHT]:
            self.level.move_player((2, 0))
        if keys[K_UP]:
            self.level.move_player((0, -2))
        if keys[K_DOWN]:
            self.level.move_player((0, 2))
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         self.level.move_player((-4, 0))
            #     if event.key == pygame.K_RIGHT:
            #         self.level.move_player((4, 0))
            #     if event.key == pygame.K_UP:
            #         self.level.move_player((0, -4))
            #     if event.key == pygame.K_DOWN:
            #         self.level.move_player((0, 4))
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            elif event.type == pygame.QUIT:
                return False
        return True

    def render(self):
        self.fake_screen.fill('black')        
        self.level.draw()
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.update()
