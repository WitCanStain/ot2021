import os
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE, VIDEORESIZE, K_LEFT, K_RIGHT
from pygame import Vector2
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, level_map
from gamelogic.level import Level
from utils.game_save import GameSave


class GameLoop:
    def __init__(self, save_file=None):

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
        pygame.display.set_caption("OT Platformer")
        self.fake_screen = self.screen.copy()
        self.clock = pygame.time.Clock()
        if save_file:
            dirname = os.path.dirname(__file__)
            path = os.path.join(dirname, "..", "saved_games", save_file)
            game_state = GameSave.load_game(path)
            saved_level_map = game_state["level_map"]
            self.level = Level(saved_level_map, self.fake_screen, game_state)
        else:
            self.level = Level(level_map, self.fake_screen)

    def start(self):
        while True:
            if self.handle_events() is False:
                break

            self.render()
            self.clock.tick(60)


    def handle_events(self):
        """Check what input the player gives and call appropriate functions.

        Returns:
            bool: boolean value indicating whether the player has closed the game.
        """
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.level.move_player_left()
        if keys[K_RIGHT]:
            self.level.move_player_right()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.level.player_jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.level.menu_toggle()
                elif event.key == pygame.K_p:
                    self.level.pause_toggle()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.level.button_clicked(self.scale_mouse(event.pos))
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

    def scale_mouse(self, pos):
        """Scales mouse coordinates so that the correct coordinates are produced even if
        player resizes window.

        Args:
            pos: position of the mouse cursor.

        Returns:
            scaled_pos: the scaled coordinates of the mouse cursor.
        """
        ratio_x = self.screen.get_rect().width / self.fake_screen.get_rect().width
        ratio_y = self.screen.get_rect().height / self.fake_screen.get_rect().height
        scaled_pos = Vector2(pos[0] / ratio_x, pos[1] / ratio_y)
        return scaled_pos
