import os
import pygame
from pygame import Vector2
from numpy import sign
from sprites.wall import Wall
from sprites.player import Player
from sprites.coin import Coin
from sprites.mob import Mob
from sprites.button import Button
from game_save import save_game
from sounds import collect_coin, player_death, game_win, game_over
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_BTN_WIDTH, MENU_BTN_HEIGHT, TILE_SIZE, GRAVITY


class Level:
    """This class contains most of the important functionality for running the game, such as lists of sprites in the world and methods for changing the game state.
    """
    def __init__(self, level_map, surface, game_state=None):
        """Initialise the instance.

        Args:
            level_map: the level map used to generate the game world.
            surface: the screen that all sprites will be drawn on.
            game_state: object containing game state information. If present, load information into instance. Defaults to None.

        Attributes:
            self.player: the player sprite.
            self.coins: pygame Group containing the coins in the game.
            self.mobs: pygame Group containing the mobs in the game
            self.interactive_objects: pygame Group containing all the sprites that can be interacted with during gameplay.
            self.all_sprites: pygame Group containing all non-button sprites.
            self.walls: pygame Group containing the wall tiles.
            self.menu_buttons: pygame Group containing the menu buttons.
            self.camera_direction: a vector indicating how all sprites should move in order to simulate the effect of the player moving.
            self.pause_btn: button that shows when game is paused.
            self.restart_btn: a menu button that shows when menu is on and when the game is over.
            self.game_win_btn: a Button object that shows on screen when the player wins.
            self.game_over_btn: a Button object that shows on screen when the player loses.
            self.menu_showing: a boolean value indicating whether the menu is showing.
            self.paused: a boolean value indicating whether the game is paused.
            self.game_win_flag: a boolean value indicating whether the game has been won.
            self.game_over_flag: a boolean value indicating whether the game has been lost.
            self.coin_count: a number indicating the amount of coins in the level.
        """
        
        self.surface = surface
        self.level_map = level_map
        self.player = None
        self.coins = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        self.interactive_objects = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.menu_buttons = pygame.sprite.Group()
        self.camera_direction = Vector2()
        self.pause_btn = None
        self.restart_btn = None
        self.game_win_btn = None
        self.game_over_btn = None
        self.menu_showing = False
        self.paused = False
        self.game_win_flag = False
        self.game_over_flag = False
        if game_state:
            self.set_state(game_state)
        else:
            self.create(self.level_map)
        self.coin_count = len(self.coins)

    def set_state(self, game_state):
        """This method reloads information from a game_state object to enable loading games from memory.

        Args:
            game_state: a game_state object.
        """

        self.player = Player(game_state["player"]["pos"])
        for attribute in game_state["player"]:
            if attribute != "pos":
                vars(self.player)[attribute] = game_state["player"][attribute]
        
        self.mobs.add(self.create_sprites_from_game_state(game_state["mobs"], Mob))
        self.walls.add(self.create_sprites_from_game_state(game_state["walls"], Wall))
        self.coins.add(self.create_sprites_from_game_state(game_state["coins"], Coin))

        self.interactive_objects.add(self.player, self.coins, self.mobs)
        self.all_sprites.add(self.walls, self.interactive_objects)
        self.create_buttons()   

    def create_sprites_from_game_state(self, sprite_state_list, Tile):
        tiles = []
        for saved_tile in sprite_state_list:
            tile = Tile(saved_tile["pos"])
            for attribute in saved_tile:
                if attribute != "pos":
                    vars(tile)[attribute] = saved_tile[attribute]
            tiles.append(tile)
        return tiles


    def draw(self):
        """This method forms the core of the game loop. It performs various movements and collision checks, and draws sprites on screen. 
        """

        if not self.paused:
            self.apply_gravity(self.interactive_objects)
            self.collect_coins()
            self.mob_move()
            self.mob_collide()
            self.all_sprites.update()
            self.all_sprites.draw(self.surface)
            for sprite in self.all_sprites:
                sprite.left += self.camera_direction.x
                sprite.top += self.camera_direction.y
            self.camera_direction = Vector2()
        else:
            self.all_sprites.draw(self.surface)
            if self.menu_showing:
                self.menu_buttons.draw(self.surface)
            else:
                self.surface.blit(self.pause_btn.image, self.pause_btn.rect)

        for sprite in self.interactive_objects:
            if sprite.off_screen() and not sprite.active:
                sprite.kill()
                if sprite == self.player:
                    self.game_over_flag = True


        if self.game_win_flag:
            self.game_win()
        elif self.game_over_flag:
            self.game_over()
            

        
    def game_over(self):
        self.surface.fill("black")
        self.surface.blit(self.game_over_btn.image, self.game_over_btn.rect)
        self.surface.blit(self.restart_btn.image, self.restart_btn.rect)


    def game_win(self):
        self.paused = True
        self.surface.fill("black")
        self.surface.blit(self.game_win_btn.image, self.game_win_btn.rect)

    def menu_toggle(self):
        if self.menu_showing:
            self.paused = False
            self.menu_showing = False
        else:
            self.paused = True
            self.menu_showing = True

    def pause_toggle(self):
        if self.paused and not self.menu_showing:
            self.paused = False
        else:
            self.paused = True


    def apply_gravity(self, sprites):
        """Applies gravity to all given sprites.

        Args:
            sprites: a group or list of sprites to which gravity is being applied.
        """
        for sprite in sprites:
            sprite.update_velocity(Vector2(0, GRAVITY))
            velocity = sprite.velocity
            self.move_sprite(sprite, Vector2(velocity.x, velocity.y))

    def player_jump(self):
        if self.sprite_touches_floor(self.player):
            self.player.update_velocity(Vector2(0, -10))

    def move_sprite(self, sprite, direction):
        """This method moves the given sprite in the given direction unless there is something blocking the way,
        in which case it moves the sprite as much as possible in the same direction.

        Args:
            sprite: the sprite that is being moved.
            direction: the direction the sprite is moving in.

        Returns:
            rectified_direction: the given direction, possibly rectified to give a measure of how much the sprite has moved.
        """
        velocity = sprite.velocity
        direction = sprite.check_speed(direction)
        rectified_direction = Vector2(direction.x, direction.y)
        # setting sprite orientation
        if direction.x > 0:
            sprite.image = sprite.img_left
        elif direction.x < 0:
            sprite.image = sprite.img_right

        # horizontal collision check
        sprite_collisions = self.check_collision(sprite, self.walls, Vector2(direction.x, 0))
        if sprite_collisions:
            sprite.update_velocity(Vector2(-velocity.x, 0))
            for coll_sprite in sprite_collisions:
                if direction.x > 0:
                    rectified_direction.x = coll_sprite.left - sprite.right
                    sprite.right = coll_sprite.left
                elif direction.x < 0:
                    rectified_direction.x = sprite.left - coll_sprite.right
                    sprite.left = coll_sprite.right
        else:
            sprite.left += direction.x
        # vertical collision check
        sprite_collisions = self.check_collision(sprite, self.walls, Vector2(0, direction.y))
        if sprite_collisions:
            sprite.update_velocity(Vector2(0, -velocity.y))
            for coll_sprite in sprite_collisions:
                if direction.y > 0:
                    rectified_direction.y = coll_sprite.top - sprite.bottom
                    sprite.bottom = coll_sprite.top
                elif direction.y < 0:
                    rectified_direction.y = coll_sprite.bottom - sprite.top
                    sprite.top = coll_sprite.bottom

        else:
            sprite.bottom += direction.y

        return rectified_direction

    def collect_coins(self, direction=Vector2()):
        sprite_collisions = self.check_collision(self.player, self.coins, direction)
        if sprite_collisions:
            for coin in sprite_collisions:
                self.player.coins += 1
                pygame.mixer.Sound.play(collect_coin)
                self.deactivate_sprite(coin)
        if self.player.coins == self.coin_count:
            pygame.mixer.Sound.play(game_win)
            self.game_win_flag = True

    def mob_move(self):
        for mob in self.mobs:
            rectified_direction = self.move_sprite(mob, mob.direction)
            self.move_sprite(mob, rectified_direction - mob.direction)
            if sign(mob.direction.x) != sign(rectified_direction.x):
                mob.direction = -mob.direction

    def mob_collide(self, direction=Vector2()):
        sprite_collisions = self.check_collision(self.player, self.mobs, direction)
        if sprite_collisions:
            for mob in sprite_collisions:
                pygame.mixer.Sound.play(game_over)
                self.deactivate_sprite(self.player)
                # self.menu_toggle()

    def deactivate_sprite(self, sprite):
        """Deactivates a sprite, causing it to appear to jump and removing it from the game world.

        Args:
            sprite: the sprite that is deactivated.
        """
        sprite.active = False
        sprite.collides = False
        sprite.update_velocity(Vector2(0, -7))

    def check_collision(self, colliding_sprite, sprites, direction=Vector2()):
        """This method checks whether the colliding_sprite collides with any of the sprites
        in the given sprites group if both of them are collidable objects.

        Args:
            colliding_sprite: the sprite whose collision is being checked.
            sprites: the sprites whose collision with the colliding_sprite is being checked.
            direction: The direction where the colliding_sprite's collisions are checked. Defaults to Vector2().

        Returns:
            sprite_collisions: a list of the collisions that occurred, if any did.
        """
        if not colliding_sprite.collides:
            return False
        colliding_sprite.update_pos(direction)
        collidable_sprites = filter(self.sprite_collides, sprites)
        sprite_collisions = pygame.sprite.spritecollide(colliding_sprite, collidable_sprites, False)
        colliding_sprite.update_pos(-direction)
        return sprite_collisions

    def sprite_touches_floor(self, sprite):
        """Checks whether the given sprite is currently touching the floor.

        Args:
            sprite: the sprite that is being checked.

        Returns:
            bool: boolean value indicating whether the sprite touches the floor.
        """
        if self.check_collision(sprite, self.walls, Vector2(0, 1)):
            return True
        return False

    def create(self, level_map):
        """This method sets up the level from the map data.

        Args:
            level_map: a list that is being interpreted as a map.
        """
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                norm_x = x * TILE_SIZE
                norm_y = y * TILE_SIZE

                cell = level_map[y][x]

                if cell == '0':
                    self.walls.add(Wall(Vector2(norm_x, norm_y)))
                elif cell == '1':
                    self.player = Player(Vector2(norm_x, norm_y))
                elif cell == '2':
                    self.coins.add(Coin(Vector2(norm_x, norm_y)))
                elif cell == '3':
                    self.mobs.add(Mob(Vector2(norm_x, norm_y)))

        self.interactive_objects.add(self.player, self.coins, self.mobs)
        self.all_sprites.add(self.walls, self.interactive_objects)
        self.create_buttons()

        

    def create_buttons(self):
        """Creates the Button sprites that can be shown to the player
        """
        resume_btn  = Button((SCREEN_WIDTH / 2 - MENU_BTN_WIDTH / 2, SCREEN_HEIGHT / 4), "resume_btn.png", "resume")
        self.restart_btn = Button((SCREEN_WIDTH / 2 - MENU_BTN_WIDTH / 2, resume_btn.bottom + 3), "restart_btn.png", "restart")
        save_btn = Button((SCREEN_WIDTH / 2 - MENU_BTN_WIDTH / 2, self.restart_btn.bottom + 3), "save_btn.png", "save")
        quit_btn = Button((SCREEN_WIDTH / 2 - MENU_BTN_WIDTH / 2, save_btn.bottom + 3), "quit_btn.png", "quit")
        self.pause_btn = Button((SCREEN_WIDTH - 64, 30), "pause_btn.png", "pause")
        self.game_win_btn = Button((SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12), "game_win.png", "game_win")
        self.game_over_btn = Button((SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12), "game_over.png", "game_over")
        self.menu_buttons.add(resume_btn, self.restart_btn, save_btn, quit_btn)

    def move_player_left(self, direction=Vector2(-2, 0)):
        if not self.paused:
            rectified_direction = self.move_sprite(self.player, direction)
            self.camera_direction = -rectified_direction

    def move_player_right(self, direction=Vector2(2, 0)):
        if not self.paused:
            rectified_direction = self.move_sprite(self.player, direction)
            self.camera_direction = -rectified_direction

    def button_clicked(self, pos):
        """This method check whether the player has clicked on a button and calls the appropriat function if so.

        Args:
            pos: position of the mouse on the screen.
        """
        if self.menu_showing or self.game_over_flag:
            for button in self.menu_buttons:
                if button.rect.collidepoint(pos):
                    if button.name == "resume":
                        self.menu_toggle()
                    elif button.name == "restart":
                        self.restart()
                    elif button.name == "save":
                        save_game(self.get_state())
                    elif button.name == "quit":
                        quit()

    def restart(self):
        """Re-initialises the instance and restarts the game.
        """
        self.__init__(self.level_map, self.surface)


    def get_state(self):
        data = {
            "player": self.player.get_state(),
            "mobs": [mob.get_state() for mob in self.mobs],
            "coins": [coin.get_state() for coin in self.coins],
            "walls": [wall.get_state() for wall in self.walls],
            "level_map": self.level_map,
            "camera_direction": self.camera_direction,
            "menu_showing": self.menu_showing,
            "paused": self.paused,
            "game_win_flag": self.game_win_flag,
            "game_over_flag": self.game_over_flag

        }
        return data

    def sprite_collides(self, sprite):
        return sprite.collides
