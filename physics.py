from Settings import Settings
import pygame
from pygame.sprite import *
from masked_sprite import MaskedSprite
from pygame.mask import *
from itertools import combinations


def apply_gravity(settings, entity, swim=False):
    if not swim:
        if entity.delta_y < settings.gravity_max:
                entity.delta_y += settings.gravity
        else:
                entity.delta_y = settings.gravity_max

    else:
        if entity.delta_y < settings.sink_max_speed:
            entity.delta_y += settings.sink_speed
        else:
            entity.delta_y = settings.sink_max_speed


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
    if asset_id == 0:
        return False

    if asset_id == 1:
        return True

    if asset_id == 2 or asset_id == 36 or asset_id == 37:
        return True

    if asset_id == 10:
        return True

    if asset_id == 30 and entity.asset_id == 99:
        if collide_rect(entity, solid):
            entity.take_damage()
            return True

    return False


def check_event_collision_y(solid, entity, direction, asset_id):
    if asset_id < 0:
        return False

    if asset_id == 0:
        test_rect = entity.rect.copy()
        test_rect.y += direction
        if collide_rect(entity, solid) or pygame.Rect.colliderect(test_rect, solid.rect):
            if entity.rect.top - entity.delta_y >= solid.rect.bottom:
                if not solid.active:
                    entity.rect.top = solid.y_pos
                    if entity.asset_id == 99:
                        solid.hit(entity)

    elif asset_id == 1:
        if collide_rect(entity, solid):
            if entity.rect.top - entity.delta_y <= solid.rect.bottom:
                return True
            else:
                if entity.asset_id == 99:
                    solid.hit(entity)

    # Platform collision
    elif asset_id == 2:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top:
                entity.rect.bottom = solid.rect.top
                entity.land()
        return True
    
    elif asset_id == 36:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y - 2 <= solid.rect.top:
                entity.rect.bottom = solid.rect.top - 2
                entity.land()
        return True

    elif asset_id == 37:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top:
                entity.rect.bottom = solid.rect.top + 4
                entity.land()
        return True

    if asset_id == 10:
        return True

    if asset_id == 30 and entity.asset_id == 99:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top and direction > 0:
                entity.bounce()
                solid.hit()
            else:
                entity.take_damage()
            return True

    return False


def get_direction(delta):
    if delta == 0:
        return 0
    elif delta > 0:
        return 1
    else:
        return -1


def enemy_to_enemy_collision(enemies):
    for one, two in combinations(enemies, 2):
        if one.rect.colliderect(two.rect):
            one.delta_x *= -1
            two.delta_x *= -1

'''
def warp(gate, entity, level):
    entity.get_base_image()
    while entity.rect.centerx != gate.rect.centerx:
        if abs(entity.rect.centerx - gate.rect.centerx) < 1:
            entity.rect.centerx = gate.rect.centerx
            entity.x = gate.rect.centerx
        elif entity.rect.centerx < gate.rect.centerx:
            entity.rect.centerx += 1
            entity.x += 1
        elif entity.rect.centerx > gate.rect.centerx:
            entity.rect.centerx -= 1
            entity.x -= 1
        level.draw_screen()
        pygame.time.wait(10)

    while entity.rect.top < gate.rect.bottom:
        entity.rect.y += 1
        level.draw_screen()
        pygame.time.wait(10)
'''