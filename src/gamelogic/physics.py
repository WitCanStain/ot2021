import pygame
from pygame import Vector2
from utils.settings import GRAVITY

def check_collision(colliding_sprite, sprites, direction=Vector2()):
    """This method checks whether the colliding_sprite collides with any of the sprites
    in the given sprites group if both of them are collidable objects.

    Args:
        colliding_sprite: the sprite whose collision is being checked.
        sprites: the sprites whose collision with the colliding_sprite is being checked.
        direction: The direction where the colliding_sprite's collisions are checked.
            Defaults to Vector2().

    Returns:
        sprite_collisions: a list of the collisions that occurred, if any did.
    """

    if not colliding_sprite.collides:
        return False
    colliding_sprite.update_pos(direction)
    collidable_sprites = filter(_sprite_collides, sprites)
    sprite_collisions = pygame.sprite.spritecollide(colliding_sprite, collidable_sprites, False)
    colliding_sprite.update_pos(-direction)
    return sprite_collisions

def move_sprite(sprite, walls, direction):
    """This method moves the given sprite in the given direction unless
    there is something blocking the way, in which case it moves the
    sprite as much as possible in the same direction.

    Args:
        sprite: the sprite that is being moved.
        direction: the direction the sprite is moving in.

    Returns:
        rectified_direction: the given direction, possibly rectified to give a
            measure of how much the sprite has moved.
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
    sprite_collisions = check_collision(sprite, walls, Vector2(direction.x, 0))
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
    sprite_collisions = check_collision(sprite, walls, Vector2(0, direction.y))
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

def apply_gravity(sprites, walls):
    """Applies gravity to all given sprites.

    Args:
        sprites: a group or list of sprites to which gravity is being applied.
    """
    for sprite in sprites:
        sprite.update_velocity(Vector2(0, GRAVITY))
        velocity = sprite.velocity
        move_sprite(sprite, walls, Vector2(velocity.x, velocity.y))

def sprite_touches_floor(sprite, walls):
    """Checks whether the given sprite is currently touching the floor.

    Args:
        sprite: the sprite that is being checked.

    Returns:
        bool: boolean value indicating whether the sprite touches the floor.
    """
    if check_collision(sprite, walls, Vector2(0, 1)):
        return True
    return False

def _sprite_collides(sprite):
    return sprite.collides
