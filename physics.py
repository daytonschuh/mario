from Settings import Settings
import pygame
from pygame.sprite import *
from masked_sprite import MaskedSprite
from pygame.mask import *


def apply_gravity(settings, entity):
    if entity.delta_y < settings.gravity_max:
        entity.delta_y += settings.gravity
    else:
        entity.delta_y = settings.gravity_max


def add_velocity_up(velocity, entity):
    entity.delta_y -= velocity


def collide_check_y(floor, entity, direction):
    if direction == 0:
        return False
    collision = collide_mask(entity, floor)
    if collision is None:
        return False
    while collision is not None:
        entity.rect.bottom -= direction
        collision = collide_mask(entity, floor)
    entity.land()
    return True


def collide_check_x(wall, entity, direction):
    if direction == 0:
        return False
    collision = collide_mask(entity, wall)
    if collision is None:
        return False
    while collision is not None:
        entity.rect.left -= direction
        entity.x -= direction
        collision = collide_mask(entity, wall)
    return True


def collide_solid_x(solid, entity, direction):
    if direction == 0:
        return False
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        old_x = entity.rect.left
        if direction > 0:
            entity.rect.right = solid.rect.left
        else:
            entity.rect.left = solid.rect.right
        entity.x += entity.rect.left - old_x
    return True


def collide_solid_y(solid, entity, direction, special=None):
    # if colliding with a special kind of object that only allows collision when walking on it
    if direction == 0 or (special is "Platform" and entity.bottom < solid.top):
        return False
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        if direction > 0:
            entity.rect.bottom = solid.rect.top
            entity.land()
        else:
            entity.rect.top = solid.rect.bottom
            if special is "Block":
                solid.hit(entity)
    return True


def collide_group_x(group, entity, direction):
    collision_found = False
    for solid in group:
        if collide_solid_x(solid, entity, direction):
            collision_found = True
    return collision_found


def collide_group_y(group, entity, direction, special=False):
    collision_found = False
    for solid in group:
        if collide_solid_y(solid, entity, direction, special):
            collision_found = True
    return collision_found


def get_direction(delta):
    if delta == 0:
        return 0
    elif delta > 0:
        return 1
    else:
        return -1
