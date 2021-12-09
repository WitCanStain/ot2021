import pygame
from pygame import Vector2
from sprites.tile import Tile
from sprites.player import Player
from sprites.coin import Coin
from sprites.mob import Mob
from sounds import collect_coin, player_death, mob_death
from settings import TILE_SIZE, GRAVITY

class Level:
    def __init__(self, level_map, surface):
        self.display_surface = surface

        self.player = None
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.game_objects = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.create(level_map)


    def draw(self):
        # self.tiles.update()
        self.apply_gravity(self.game_objects)
        self.collect_coins(self.player)
        self.mob_collide()
        self.all_sprites.update()
        for sprite in self.game_objects:
            if sprite.off_screen() and not sprite.active:
                sprite.kill()
        self.all_sprites.draw(self.display_surface)


    def apply_gravity(self, sprites):
        for sprite in sprites:
            sprite.update_velocity(Vector2(0, GRAVITY))
            velocity = sprite.get_velocity()
            self.move_sprite(sprite, Vector2(velocity.x, velocity.y))

    def sprite_jump(self, sprite):
        if self.sprite_touches_floor(sprite):
            sprite.update_velocity(Vector2(0, -10))

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


    def collect_coins(self, sprite, direction=Vector2()):
        sprite_collisions = self.check_collision(sprite, self.coins, direction)
        if sprite_collisions:
            for coin in sprite_collisions:
                self.player.coins += 1
                pygame.mixer.Sound.play(collect_coin)
                self.deactivate_sprite(coin)

    def mob_collide(self, direction=Vector2()):
        sprite_collisions = self.check_collision(self.player, self.mobs, direction)
        if sprite_collisions:
            for mob in sprite_collisions:
                if self.player.attack != True:
                    pygame.mixer.Sound.play(player_death)
                    self.deactivate_sprite(self.player)
                else:
                    pygame.mixer.Sound.play(mob_death)
                    self.deactivate_sprite(mob)


    def deactivate_sprite(self, sprite):
        sprite.active = False
        sprite.collides = False
        sprite.update_velocity(Vector2(0, -7))

    def check_collision(self, colliding_sprite, sprites, direction=Vector2()):
        if not colliding_sprite.collides:
            return False
        colliding_sprite.update_pos(direction)
        collidable_sprites = filter(self.sprite_collides, sprites)
        sprite_collisions = pygame.sprite.spritecollide(colliding_sprite, collidable_sprites, False)
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
                elif cell == '3':
                    self.mobs.add(Mob(Vector2(norm_x, norm_y)))

        self.game_objects.add(self.player, self.coins, self.mobs)
        self.all_sprites.add(self.tiles, self.game_objects)


    def get_player(self):
        return self.player

    def get_all_sprites(self):
        return self.all_sprites

    def sprite_collides(self, sprite):
        return sprite.collides
