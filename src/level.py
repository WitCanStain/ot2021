import pygame
from pygame import Vector2
from sprites.tile import Tile
from sprites.player import Player
from settings import TILE_SIZE, GRAVITY

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface

        self.player = None
        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()


        self.create(level_map)


    def draw(self):
        self.tiles.update()
        
        self.all_sprites.draw(self.display_surface)


    def move_player(self, velocity):
        if not self.sprite_touches_floor(self.player):
            self.set_velocity(self.player.get_velocity() + Vector2(velocity.x, GRAVITY))
        else:
            self.set_velocity(self.player.get_velocity() + Vector2(velocity.x, 0))

    def set_velocity(self, pos):
        sprite_collisions = self.sprite_collides(self.player, self.tiles, pos)
        if not sprite_collisions:
            self.player.update(pos)
        else:
            for sprite in sprite_collisions:
                rect = sprite.get_rect()
                sprite_topleft_y = rect.topleft[1]
                player_bottomleft_y = self.player.get_rect().bottomleft[1]
                
                if sprite_topleft_y > player_bottomleft_y:
                    new_pos = Vector2(0, sprite_topleft_y - player_bottomleft_y)
                    if not self.sprite_collides(self.player, self.tiles, new_pos):
                        self.player.update(new_pos)


    def create(self, level_map):
        self.tiles = pygame.sprite.Group()
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                norm_x = x * TILE_SIZE
                norm_y = y * TILE_SIZE

                cell = level_map[y][x]

                if cell == '0':
                    self.tiles.add(Tile((norm_x, norm_y)))
                elif cell == '1':
                    self.player = Player((norm_x, norm_y))

        self.all_sprites.add(self.tiles, self.player)


    def sprite_collides(self, actor_sprite, tile_sprite, pos):
        actor_sprite.update(pos)
        sprite_collisions = pygame.sprite.spritecollide(actor_sprite, tile_sprite, False)
        actor_sprite.update(-pos)
        return sprite_collisions

    def sprite_touches_floor(self, sprite):
        return self.sprite_collides(sprite, self.tiles, Vector2(0, 2))



    def get_player(self):
        return self.player

    def get_all_sprites(self):
        return self.all_sprites
