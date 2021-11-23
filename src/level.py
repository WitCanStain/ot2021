import pygame
from sprites.tiles import Tile
from sprites.player import Player
from settings import tile_size

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface
        
        self.player = None
        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        
        
        self.create(level_map)
        

    def draw(self):
        self.all_sprites.draw(self.display_surface)
        


    def create(self, level_map):
        self.tiles = pygame.sprite.Group()
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                norm_x = x * tile_size
                norm_y = y * tile_size

                cell = level_map[y][x]

                if cell == '0':
                    self.tiles.add(Tile((norm_x, norm_y))) 
                elif cell == '1':
                    self.player = Player((norm_x, norm_y))
                    
        self.all_sprites.add(self.tiles, self.player)

    def get_player(self):
        return self.player

    def get_all_sprites(self):
        return self.all_sprites