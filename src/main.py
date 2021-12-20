import sys
import pygame
from game_loop import GameLoop

def main(argv):
    pygame.init()

    if len(argv) > 1:
        if 's=' in argv[1]:
            game_loop = GameLoop(save_file=argv[1].split('=')[1])
        elif 'l=' in argv[1]:
            game_loop = GameLoop(level_map=argv[1].split('=')[1])
    else:
        game_loop = GameLoop()
    game_loop.start()



if __name__ == "__main__":
    main(sys.argv)
    