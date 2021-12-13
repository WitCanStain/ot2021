import sys
import pygame
from pygame import Vector2
from numpy import sign
from sprites.wall import Wall
from sprites.player import Player
from sprites.coin import Coin
from sprites.mob import Mob
from sprites.button import Button
from game_save import save_game
from physics import check_collision, move_sprite, apply_gravity, sprite_touches_floor
from sounds import collect_coin, game_win, game_over
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_BTN_WIDTH, TILE_SIZE


class Level:
    """This class contains most of the important functionality for running the game,
    such as lists of sprites in the world and methods for changing the game state.
    """
    def __init__(self, level_map, surface, game_state=None):
        """Initialise the instance.

        Args:
            level_map: the level map used to generate the game world.
            surface: the screen that all sprites will be drawn on.
            game_state: object containing game state information. If present, load
                information into instance. Defaults to None.

        Attributes:
            self.player: the player sprite.
            self.coins: pygame Group containing the coins in the game.
            self.mobs: pygame Group containing the mobs in the game
            self.interactive_objects: pygame Group containing all the sprites that can be
                interacted with during gameplay.
            self.all_sprites: pygame Group containing all non-button sprites.
            self.walls: pygame Group containing the wall tiles.
            self.menu_buttons: pygame Group containing the menu buttons.
            self.camera_direction: a vector indicating how all sprites should move in order
                to simulate the effect of the player moving.
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

    def draw(self):
        """This method forms the core of the game loop. It performs various
        movements and collision checks, and draws sprites on screen.
        """

        if not self.paused:
            apply_gravity(self.interactive_objects, self.walls)
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

    def player_jump(self):
        if sprite_touches_floor(self.player, self.walls):
            self.player.update_velocity(Vector2(0, -10))

    def move_player_left(self, direction=Vector2(-2, 0)):
        if not self.paused:
            rectified_direction = move_sprite(self.player, self.walls, direction)
            self.camera_direction = -rectified_direction

    def move_player_right(self, direction=Vector2(2, 0)):
        if not self.paused:
            rectified_direction = move_sprite(self.player, self.walls, direction)
            self.camera_direction = -rectified_direction

    def mob_move(self):
        for mob in self.mobs:
            rectified_direction = move_sprite(mob, self.walls, mob.direction)
            move_sprite(mob, self.walls, rectified_direction - mob.direction)
            if sign(mob.direction.x) != sign(rectified_direction.x):
                mob.direction = -mob.direction

    def collect_coins(self, direction=Vector2()):
        sprite_collisions = check_collision(self.player, self.coins, direction)
        if sprite_collisions:
            for coin in sprite_collisions:
                self.player.coins += 1
                pygame.mixer.Sound.play(collect_coin)
                coin.deactivate()
        if self.player.coins == self.coin_count:
            pygame.mixer.Sound.play(game_win)
            self.game_win_flag = True

    def mob_collide(self, direction=Vector2()):
        sprite_collisions = check_collision(self.player, self.mobs, direction)
        if sprite_collisions:
            pygame.mixer.Sound.play(game_over)
            self.player.deactivate()

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
        menu_button_x_pos = SCREEN_WIDTH / 2 - MENU_BTN_WIDTH / 2
        resume_btn = Button((menu_button_x_pos, SCREEN_HEIGHT / 4), "resume_btn.png", "resume")
        self.restart_btn = Button((menu_button_x_pos, resume_btn.bottom + 3), "restart_btn.png", "restart")
        save_btn = Button((menu_button_x_pos, self.restart_btn.bottom + 3), "save_btn.png", "save")
        quit_btn = Button((menu_button_x_pos, save_btn.bottom + 3), "quit_btn.png", "quit")
        self.pause_btn = Button((SCREEN_WIDTH - 64, 30), "pause_btn.png", "pause")
        self.game_win_btn = Button((SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12), "game_win.png", "game_win")
        self.game_over_btn = Button((SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 12), "game_over.png", "game_over")
        self.menu_buttons.add(resume_btn, self.restart_btn, save_btn, quit_btn)

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
                        sys.exit()

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

    def restart(self):
        """Re-initialises the instance and restarts the game.
        """
        self.__init__(self.level_map, self.surface)
