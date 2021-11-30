import pygame
from game_loop import GameLoop

def main():
    pygame.init()
    game_loop = GameLoop()
    game_loop.start()



if __name__ == "__main__":
    main()
    