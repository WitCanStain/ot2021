import pygame

class Renderer:

    def __init__(self, screen, fake_screen, level):
        self._screen = screen
        self._fake_screen = fake_screen
        self._level = level

    def render(self):
        """Renders the screen.
        """
        self._fake_screen.fill((135, 206, 250))
        self._level.draw()
        self._screen.blit(pygame.transform.scale(self._fake_screen, self._screen.get_rect().size), (0, 0))
        pygame.display.update()