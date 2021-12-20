import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE, VIDEORESIZE, K_LEFT, K_RIGHT
from utils.scale_mouse import scale_mouse


class GameLoop:
    """This class is responsible for the main loop of the program, which consists of running the
    renderer every frame and waiting for user input.
    """
    def __init__(self, renderer, event_queue, level, screen, fake_screen):

        self._clock = pygame.time.Clock()
        self._renderer = renderer
        self._event_queue = event_queue
        self._level = level
        self.screen = screen
        self.fake_screen = fake_screen

    def start(self):
        while True:
            if self._handle_events() is False:
                break
            self._render()
            self._clock.tick(60)


    def _handle_events(self):
        """Check what input the player gives and call appropriate functions.

        Returns:
            bool: boolean value indicating whether the player has closed the game.
        """
        keys = self._event_queue.get_pressed()
        if keys[K_LEFT]:
            self._level.move_player_left()
        elif keys[K_RIGHT]:
            self._level.move_player_right()

        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._level.player_jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self._level.menu_toggle()
                elif event.key == pygame.K_p:
                    self._level.pause_toggle()
                elif event.key == pygame.K_r:
                    self._level.restart()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._level.button_clicked(scale_mouse(event.pos, self.screen, self.fake_screen))
            elif event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            elif event.type == pygame.QUIT:
                return False
        return True

    def _render(self):
        self._renderer.render()
