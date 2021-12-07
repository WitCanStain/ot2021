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
        self.move_player(Vector2(0, GRAVITY))
        self.all_sprites.draw(self.display_surface)


    def move_player(self, direction):

        updated_pos = self.check_collision_and_correct(self.player, self.tiles, direction)
        self.player.update(updated_pos)


    def check_collision_and_correct(self, actor, sprites, direction):
        corrected_direction = Vector2(direction.x, direction.y)
        actor_left, actor_top, actor_right, actor_bottom = actor.get_bounds()

        # horizontal collision check
        sprite_collisions = self.check_collision(actor, sprites, Vector2(direction.x, 0))
        if sprite_collisions:
            for sprite in sprite_collisions:
                sprite_left, sprite_top, sprite_right, sprite_bottom = sprite.get_bounds()
                if direction.x > 0:
                    corrected_direction.x = sprite_left - actor_right
                elif direction.x < 0:
                    corrected_direction.x = sprite_right - actor_left

        # vertical collision check
        sprite_collisions = self.check_collision(actor, sprites, Vector2(0, direction.y))
        if sprite_collisions:
            for sprite in sprite_collisions:
                sprite_left, sprite_top, sprite_right, sprite_bottom = sprite.get_bounds()
                if direction.y > 0:
                    corrected_direction.y = sprite_top - actor_bottom
                elif direction.y < 0:
                    corrected_direction.y = sprite_bottom - actor_top

        return corrected_direction

    def check_collision(self, actor, sprites, direction):
        actor.update_pos(direction)
        sprite_collisions = pygame.sprite.spritecollide(actor, sprites, False)
        actor.update_pos(-direction)
        return sprite_collisions

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
