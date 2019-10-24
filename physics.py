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


def collide_check_y(floor, entity):
    if entity.delta_y >= 0:
        direction = 1
    else:
        direction = -1
    entity.rect.bottom += entity.delta_y
    collision = collide_mask(entity, floor)
    if collision:
        entity.airborne = True
        entity.buffer_b = 11
    while collision is not None:
        entity.rect.bottom -= direction
        collision = collide_mask(entity, floor)
        if collision is None:
            entity.land()


def collide_check_x(wall, entity):
    if entity.delta_x == 0:
        return False
    elif entity.delta_x > 0:
        direction = 1
    else:
        direction = -1
    entity.rect.left += entity.delta_x
    entity.x += entity.delta_x
    collision = collide_mask(entity, wall)
    while collision is not None:
        entity.rect.left -= direction
        entity.x -= direction
        collision = collide_mask(entity, wall)
    entity.delta_x = 0
    return True
