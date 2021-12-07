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
        # self.move_player(Vector2(0, GRAVITY))
        self.all_sprites.draw(self.display_surface)


    def move_player(self, direction):
        
        updated_pos = self.check_collision_and_correct(self.player, self.tiles, direction)
        self.player.update(updated_pos)
        

    def check_collision_and_correct(self, actor_sprite, sprites, direction):
        new_direction = Vector2(direction.x, direction.y)
        actor_sprite_left, actor_sprite_top, actor_sprite_right, actor_sprite_bottom = actor_sprite.get_bounds()
        
        # horizontal collision check
        actor_sprite.update_pos(Vector2(direction.x, 0))
        sprite_collisions = pygame.sprite.spritecollide(actor_sprite, sprites, False)
        if sprite_collisions:
            for sprite in sprite_collisions:
                sprite_left, sprite_top, sprite_right, sprite_bottom = sprite.get_bounds()
                if direction.x > 0:
                    new_direction.x = sprite_left - actor_sprite_right
                elif direction.x < 0:
                    new_direction.x = sprite_right - actor_sprite_left
                
        # vertical collision check
        actor_sprite.update_pos(Vector2(-direction.x, direction.y))
        sprite_collisions = pygame.sprite.spritecollide(actor_sprite, sprites, False)
        if sprite_collisions:
            for sprite in sprite_collisions:
                sprite_left, sprite_top, sprite_right, sprite_bottom = sprite.get_bounds()
                if direction.y > 0:
                    new_direction.y = sprite_top - actor_sprite_bottom
                elif direction.y < 0:
                    new_direction.y = sprite_bottom - actor_sprite_top
        
        actor_sprite.update_pos(Vector2(0, -direction.y))
        return new_direction


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
                    self.tiles.add(Tile(Vector2(norm_x, norm_y)))
                elif cell == '1':
                    self.player = Player(Vector2(norm_x, norm_y))

        self.all_sprites.add(self.tiles, self.player)


    def get_player(self):
        return self.player

    def get_all_sprites(self):
        return self.all_sprites
