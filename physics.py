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
    if direction > 0:
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


def collide_solid_x(solid, entity, direction, asset_id):
    if direction == 0:
        return False
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        if check_event_collision_x(solid, entity, direction, asset_id):
            return False
        old_x = entity.rect.left
        if direction > 0:
            entity.rect.right = solid.rect.left
        else:
            entity.rect.left = solid.rect.right
        entity.x += entity.rect.left - old_x
    return True


def collide_solid_y(solid, entity, direction, asset_id):
    if check_event_collision_y(solid, entity, direction, asset_id):
        return False
    if direction == 0:
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
    return True


def collide_group_x(group, entity, direction):
    collision_found = False
    for solid in group:
        if collide_solid_x(solid, entity, direction, solid.asset_id):
            collision_found = True
    return collision_found


def collide_group_y(group, entity, direction):
    collision_found = False
    for solid in group:
        if collide_solid_y(solid, entity, direction, solid.asset_id):
            collision_found = True
    return collision_found


def check_event_collision_x(solid, entity, direction, asset_id):
    if asset_id is 0:
        return False

    if asset_id is 1 or asset_id is 3:
        return True

    return False


def check_event_collision_y(solid, entity, direction, asset_id):
    if asset_id < 0:
        return False

    if asset_id is 3:
        return True

    if asset_id is 0:
        test_rect = entity.rect.copy()
        test_rect.y += direction
        if collide_rect(entity, solid) or pygame.Rect.colliderect(test_rect, solid.rect):
            if entity.rect.top - entity.delta_y >= solid.rect.bottom:
                if not solid.active:
                    entity.rect.top = solid.y_pos
                    solid.hit(entity)

    elif asset_id is 1:
        if collide_rect(entity, solid):
            if entity.rect.top - entity.delta_y <= solid.rect.bottom:
                return True
            else:
                solid.hit(entity)

    # Platform collision
    elif asset_id is 2:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top:
                entity.rect.bottom = solid.rect.top
                entity.land()
        return True

    return False


def get_direction(delta):
    if delta == 0:
        return 0
    elif delta > 0:
        return 1
    else:
        return -1

'''
def warp(gate, entity, screen):
    while entity.rect.center_x is not gate.rect.center_x
        if entity.rect.center_x < gate.rect.center_x:
            entity.rect.center_x += 1
        elif entity.rect.center_x > gate.rect.center_x:
            entity.rect.center_x -= 1
        entity.draw()
        pygame.time.sleep(1/60)

    while entity.rect.top is not gate.rect.top:
        entity.rect.y -= 1
        pygame.time.sleep(1/60)
'''