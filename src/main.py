import sys
import pygame
from game_loop import GameLoop

def main(argv):
    pygame.init()
    if len(argv) > 1:
        game_loop = GameLoop(argv[1])
    else:
        game_loop = GameLoop()
    game_loop.start()



if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv)
    