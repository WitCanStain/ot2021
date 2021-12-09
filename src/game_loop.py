import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE, VIDEORESIZE, K_LEFT, K_RIGHT, K_DOWN
from pygame import Vector2
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, level_map
from level import Level


class GameLoop:
    def __init__(self):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        self.level = Level(level_map, self.fake_screen)
        self.player = self.level.player

    def start(self):
        while True:
            if self.handle_events() is False:
                break

            self.render()
            self.clock.tick(60)


    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.level.move_player_left()
            
        if keys[K_RIGHT]:
            self.level.move_player_right()
            # self.level.move_sprite(self.player, Vector2(2, 0))
        if keys[K_DOWN]:
            self.level.move_sprite(self.player, Vector2(0, 2))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.level.sprite_jump(self.player)
            # elif event.type == pygame.KEYUP:
            #     if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            #         self.level.move_sprite(-self.level.player.get_direction())
            elif event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            elif event.type == pygame.QUIT:
                return False
        return True

    def render(self):
        self.fake_screen.fill((135, 206, 250))
        self.level.draw()
        self.screen.blit(pygame.transform.scale(self.fake_screen, self.screen.get_rect().size), (0, 0))
        pygame.display.update()
