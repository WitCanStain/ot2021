import sys
import pygame
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE
from utils.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_MAP
from utils.game_file import GameFile
from gamelogic.level import Level
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue

def main(argv):
    save_file = None
    level_map = None
    if len(argv) > 1:
        if 's=' in argv[1]:
            save_file=argv[1].split('=')[1]
        elif 'l=' in argv[1]:
            level_map=argv[1].split('=')[1]

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), HWSURFACE|DOUBLEBUF|RESIZABLE)
    pygame.display.set_caption("OT Platformer")
    fake_screen = screen.copy()
    if save_file:
        game_state = GameFile.load_game(save_file)
        if game_state:
            saved_level_map = game_state["LEVEL_MAP"]
            level = Level(saved_level_map, fake_screen, game_state)
    elif level_map:
        level_map = GameFile.generate_level_map_from_file(level_map)
        if level_map:
            level = Level(level_map, fake_screen)
    else:
        level = Level(LEVEL_MAP, fake_screen)

    renderer = Renderer(screen, fake_screen, level)
    event_queue = EventQueue()


    game_loop = GameLoop(renderer, event_queue, level, screen, fake_screen)
    game_loop.start()



if __name__ == "__main__":
    main(sys.argv)
