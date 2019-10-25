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


def add_velocity_up(settings, entity):
    entity.delta_y -= settings


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
        if direction > 0:
            entity.rect.right = solid.rect.left
        else:
            entity.rect.left = solid.rect.right
    return True


def collide_solid_y(solid, entity, direction, special=False):
    # if colliding with a special kind of object that only allows collision when walking on it
    if direction == 0 or (special and entity.bottom < solid.top):
        return False
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        if direction > 0:
            entity.rect.bottom = solid.rect.top
        else:
            entity.rect.top = solid.rect.bottom
    return True


def get_direction(delta):
    if delta == 0:
        return 0
    elif delta > 0:
        return 1
    else:
        return -1
