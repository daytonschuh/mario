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


def collide_solid_x(solid, entity, direction):
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        if check_event_collision_x(solid, entity, direction):
            return False
        old_x = entity.rect.left
        if direction > 0:
            entity.rect.right = solid.rect.left
        elif direction < 0:
            entity.rect.left = solid.rect.right
        entity.x += entity.rect.left - old_x
    return True


def collide_solid_y(solid, entity, direction):
    collision = collide_rect(entity, solid)
    if not collision:
        return False
    if collision:
        if check_event_collision_y(solid, entity, direction):
            return False
        if direction > 0 and entity.rect.bottom - entity.delta_y < solid.rect.top:
            entity.rect.bottom = solid.rect.top
            entity.land()
        elif direction < 0 and entity.rect.bottom - entity.delta_y > solid.rect.bottom:
            entity.rect.top = solid.rect.bottom
    return True


def collide_group_x(group, entity, direction):
    collision_found = False
    for solid in group:
        if collide_solid_x(solid, entity, direction):
            collision_found = True
    return collision_found


def collide_group_y(group, entity, direction):
    collision_found = False
    for solid in group:
        if collide_solid_y(solid, entity, direction):
            collision_found = True
    return collision_found


def check_event_collision_x(solid, entity, direction):
    if solid.asset_id == 2 or solid.asset_id == 40 or solid.asset_id == 41:
        return True

    if solid.asset_id == 3:
        return True

    if solid.asset_id == 10:
        return True

    if 30 <= solid.asset_id <= 34 and entity.asset_id == 99:
        if collide_rect(entity, solid):
            if solid.asset_id != 33 or solid.delta_x != 0:
                entity.take_damage()
            else:
                if entity.rect.centerx > solid.rect.centerx:
                    solid.kick(-1)
                else:
                    solid.kick(1)
        return True

    if 30 <= solid.asset_id <= 34 and entity.asset_id == 100:
        if collide_rect(entity, solid):
            solid.fire_hit()
        return True

    return False


def check_event_collision_y(solid, entity, direction):
    if solid.asset_id == 0:
        test_rect = entity.rect.copy()
        test_rect.y += direction
        if collide_rect(entity, solid) or pygame.Rect.colliderect(test_rect, solid.rect):
            if entity.rect.top - entity.delta_y >= solid.rect.bottom:
                if not solid.active:
                    entity.rect.top = solid.rect.bottom
                    if entity.asset_id == 99:
                        solid.hit(entity)

    elif solid.asset_id == 1:
        if collide_rect(entity, solid):
            if entity.rect.top - entity.delta_y <= solid.rect.bottom:
                return True
            else:
                if entity.asset_id == 99:
                    solid.hit(entity)

    # Platform collision
    elif solid.asset_id == 2:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top:
                entity.rect.bottom = solid.rect.top
                entity.land()
        return True

    elif solid.asset_id == 3:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y < solid.rect.top:
                if 30 <= entity.asset_id <= 33:
                    entity.hit()
                    return True
                elif 20 <= entity.asset_id <= 23:
                    if entity.rect.left < solid.rect.left:
                        entity.delta_x = -abs(entity.delta_x)
                    elif entity.rect.left > solid.rect.left:
                        entity.delta_x = abs(entity.delta_x)
                    entity.rect.bottom = solid.rect.top
                    entity.delta_y = -1
                    add_velocity_up(6, entity)
                    return True
                else:
                    return False
    
    elif solid.asset_id == 40:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y - 2 <= solid.rect.top:
                entity.rect.bottom = solid.rect.top - 2
                entity.land()
        return True

    elif solid.asset_id == 41:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top:
                entity.rect.bottom = solid.rect.top + 4
                entity.land()
        return True

    if solid.asset_id == 10:
        return True

    if solid.asset_id == 30 and entity.asset_id == 99:
        if collide_rect(entity, solid):
            if entity.rect.bottom - entity.delta_y <= solid.rect.top and direction > 0:
                entity.bounce()
                solid.hit()
            else:
                entity.take_damage()
            return True

    if solid.asset_id == 33 and entity.asset_id == 99:
        if collide_rect(entity, solid):
            if solid.delta_x == 0:
                if entity.rect.centerx >= solid.rect.centerx:
                    solid.kick(-1)
                else:
                    solid.kick(1)
            else:
                solid.hit()
                entity.bounce()
        return True

    if 30 <= solid.asset_id <= 34 and entity.asset_id == 100:
        if collide_rect(entity, solid):
            solid.fire_hit()
            return True
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
            # if both enemies are ground enemies, both change directions
            if one.asset_id == 30 and two.asset_id == 30:
                one.delta_x *= -1
                two.delta_x *= -1

            # shells kill enemies that aren't bowser including other shells if they are moving
            # if shells are not moving ground enemies turn around when touching it
            id_1, dx1 = one.asset_id, one.delta_x
            id_2, dx2 = two.asset_id, two.delta_x
            if id_1 == 33 and 30 <= id_2 <= 33:
                if dx1 != 0:
                    two.fire_hit()
                elif id_1 == 30:
                    two.delta_x *= -1
            if id_2 == 33 and 30 <= id_2 <= 33:
                if dx2 != 0:
                    one.fire_hit()
                elif id_2 == 30:
                    two.delta_x *= -1
