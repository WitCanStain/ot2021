import pygame

class EventQueue:
    def get(self):
        return pygame.event.get()

    def get_pressed(self):
        return pygame.key.get_pressed()
