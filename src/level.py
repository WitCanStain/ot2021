import pygame
from pygame import Vector2
from sprites.tile import Tile
from sprites.player import Player
from sprites.coin import Coin
from settings import TILE_SIZE, GRAVITY

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface

        self.player = None
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.create(level_map)


    def draw(self):
        # self.tiles.update()
        self.apply_gravity(self.player)
        self.coin_collide(self.player)
        self.all_sprites.update()
        self.all_sprites.draw(self.display_surface)


    def apply_gravity(self, sprite):
        sprite.update_velocity(Vector2(0, GRAVITY))
        velocity = sprite.get_velocity()
        self.move_sprite(sprite, Vector2(velocity.x, velocity.y))

    def sprite_jump(self, sprite):
        if self.sprite_touches_floor(sprite):
            self.player.update_velocity(Vector2(0, -10))

    def move_sprite(self, sprite, direction):
        velocity = sprite.get_velocity()
        direction = sprite.check_speed(direction)
        # horizontal collision check
        sprite_collisions = self.check_collision(sprite, self.tiles, Vector2(direction.x, 0))
        if sprite_collisions:
            sprite.update_velocity(Vector2(-velocity.x, 0))
            for coll_sprite in sprite_collisions:
                if direction.x > 0:
                    sprite.right = coll_sprite.left
                elif direction.x < 0:
                    sprite.left = coll_sprite.right
        else:
            sprite.left += direction.x
        # vertical collision check
        sprite_collisions = self.check_collision(sprite, self.tiles, Vector2(0, direction.y))
        if sprite_collisions:
            sprite.update_velocity(Vector2(0, -velocity.y))
            for coll_sprite in sprite_collisions:
                if direction.y > 0:
                    sprite.bottom = coll_sprite.top
                elif direction.y < 0:
                    sprite.top = coll_sprite.bottom
            
        else:
            sprite.bottom += direction.y
        

    def coin_collide(self, sprite, direction=Vector2()):
        sprite_collisions = self.check_collision(sprite, self.coins, direction)
        if sprite_collisions:
            for coin in sprite_collisions:
                self.player.coins += 1
                coin.kill()


    def check_collision(self, colliding_sprite, sprites, direction=Vector2()):
        colliding_sprite.update_pos(direction)
        sprite_collisions = pygame.sprite.spritecollide(colliding_sprite, sprites, False)
        colliding_sprite.update_pos(-direction)
        return sprite_collisions

    def sprite_touches_floor(self, sprite):
        if self.check_collision(sprite, self.tiles, Vector2(0, 1)):
            return True
        return False

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
                elif cell == '2':
                    self.coins.add(Coin(Vector2(norm_x, norm_y)))


        self.all_sprites.add(self.tiles, self.coins, self.player)


    def get_player(self):
        return self.player

    def get_all_sprites(self):
        return self.all_sprites
