import pygame
from pygame.sprite import Sprite
from pygame import *
from physics import *

face_left = pygame.image.load('Resources/Images/Baby_mario/face_left.png')
face_right = pygame.image.load('Resources/Images/Baby_mario/face_right.png')
big_face_left = pygame.image.load('Resources/Images/Papa_mario/face_left.png')
big_face_right = pygame.image.load('Resources/Images/Papa_mario/face_right.png')
fire_face_left = pygame.image.load('Resources/Images/Fire_mario/face_left.png')
fire_face_right = pygame.image.load('Resources/Images/Fire_mario/face_right.png')
face = [[face_left, face_right], [big_face_left, big_face_right], [fire_face_left, fire_face_right]]
jump_left = pygame.image.load('Resources/Images/Baby_mario/jump_left.png')
jump_right = pygame.image.load('Resources/Images/Baby_mario/jump_right.png')
big_jump_left = pygame.image.load('Resources/Images/Papa_mario/jump_left.png')
big_jump_right = pygame.image.load('Resources/Images/Papa_mario/jump_right.png')
fire_jump_left = pygame.image.load('Resources/Images/Fire_mario/jump_left.png')
fire_jump_right = pygame.image.load('Resources/Images/Fire_mario/jump_right.png')
jump = [[jump_left, jump_right], [big_jump_left, big_jump_right], [fire_jump_left, fire_jump_right]]
turn_left = pygame.image.load('Resources/Images/Baby_mario/turn_left.png')
turn_right = pygame.image.load('Resources/Images/Baby_mario/turn_right.png')
big_turn_left = pygame.image.load('Resources/Images/Papa_mario/turn_left.png')
big_turn_right = pygame.image.load('Resources/Images/Papa_mario/turn_right.png')
fire_turn_left = pygame.image.load('Resources/Images/Fire_mario/turn_left.png')
fire_turn_right = pygame.image.load('Resources/Images/Fire_mario/turn_right.png')
turn = [[turn_left, turn_right], [big_turn_left, big_turn_right], [fire_turn_left, fire_turn_right]]
walk_left_1 = pygame.image.load('Resources/Images/Baby_mario/walk_left_1.png')
walk_left_2 = pygame.image.load('Resources/Images/Baby_mario/walk_left_2.png')
walk_left_3 = pygame.image.load('Resources/Images/Baby_mario/walk_left_3.png')
big_walk_left_1 = pygame.image.load('Resources/Images/Papa_mario/walk_left_1.png')
big_walk_left_2 = pygame.image.load('Resources/Images/Papa_mario/walk_left_2.png')
big_walk_left_3 = pygame.image.load('Resources/Images/Papa_mario/walk_left_3.png')
fire_walk_left_1 = pygame.image.load('Resources/Images/Fire_mario/walk_left_1.png')
fire_walk_left_2 = pygame.image.load('Resources/Images/Fire_mario/walk_left_2.png')
fire_walk_left_3 = pygame.image.load('Resources/Images/Fire_mario/walk_left_3.png')
walk_left_cycle = [[walk_left_1, walk_left_2, walk_left_3], [big_walk_left_1, big_walk_left_2, big_walk_left_3], [fire_walk_left_1, fire_walk_left_2, fire_walk_left_3]]
walk_right_1 = pygame.image.load('Resources/Images/Baby_mario/walk_right_1.png')
walk_right_2 = pygame.image.load('Resources/Images/Baby_mario/walk_right_2.png')
walk_right_3 = pygame.image.load('Resources/Images/Baby_mario/walk_right_3.png')
big_walk_right_1 = pygame.image.load('Resources/Images/Papa_mario/walk_right_1.png')
big_walk_right_2 = pygame.image.load('Resources/Images/Papa_mario/walk_right_2.png')
big_walk_right_3 = pygame.image.load('Resources/Images/Papa_mario/walk_right_3.png')
fire_walk_right_1 = pygame.image.load('Resources/Images/Fire_mario/walk_right_1.png')
fire_walk_right_2 = pygame.image.load('Resources/Images/Fire_mario/walk_right_2.png')
fire_walk_right_3 = pygame.image.load('Resources/Images/Fire_mario/walk_right_3.png')
walk_right_cycle = [[walk_right_1, walk_right_2, walk_right_3], [big_walk_right_1, big_walk_right_2, big_walk_right_3], [fire_walk_right_1, fire_walk_right_2, fire_walk_right_3]]
transform_a_r = pygame.image.load('Resources/Images/Mario_transitions/transition_to_adult_1.png')
transform_b_r = pygame.image.load('Resources/Images/Mario_transitions/transition_to_adult_2.png')
transform_a_l = pygame.image.load('Resources/Images/Mario_transitions/transition_to_adult_1_l.png')
transform_b_l = pygame.image.load('Resources/Images/Mario_transitions/transition_to_adult_2_l.png')
transform = [[transform_a_l, transform_b_l], [transform_a_r, transform_b_r]]
fire_transform_a_r = pygame.image.load('Resources/Images/Mario_transitions/fire_mario_1.png')
fire_transform_b_r = pygame.image.load('Resources/Images/Mario_transitions/fire_mario_2.png')
fire_transform_a_l = pygame.image.load('Resources/Images/Mario_transitions/fire_mario_1_l.png')
fire_transform_b_l = pygame.image.load('Resources/Images/Mario_transitions/fire_mario_2_l.png')
fire_transform = [[fire_transform_a_l, fire_transform_b_l], [fire_transform_a_r, fire_transform_b_r]]
death = pygame.image.load('Resources/Images/Baby_mario/death.png')


class Jumpman(Sprite):
    def __init__(self, screen, settings, camera, stage, style, start_pos, swim=False):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.stage = stage
        self.style = style
        self.state = 0
        self.image = face[self.stage][1]
        self.rect = self.image.get_rect()
        self.mask = None
        self.update_mask()
        self.set_pos(start_pos)
        self.swim = swim
        self.asset_id = 99

        self.x = self.rect.left
        self.delta_x = 0
        self.delta_y = 0
        self.buffer_a = 0
        self.buffer_b = 0
        self.airborne = False
        self.run = False
        self.face = 1
        self.invincible = 0
        self.invulnerable = False
        self.invul_timer = 100
        self.death_timer = 240

    def update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def update_hitbox(self, next_stage):
        if next_stage > 0:
            bottom = self.rect.bottom
            left = self.rect.left

            image_a = face[self.stage][1]
            size_a = image_a.get_size()

            self.stage = next_stage

            self.image = face[1][1]
            size_b = self.image.get_size()

            c_x = size_b[0] - size_a[0]
            c_y = size_b[1] - size_a[1]

            self.rect.inflate_ip(c_x, c_y)
            self.update_mask()

            self.rect.bottom = bottom
            self.rect.left = left

        if next_stage == 0:
            bottom = self.rect.bottom
            left = self.rect.left

            image_a = face[1][1]
            size_a = image_a.get_size()

            self.stage = next_stage

            self.image = face[0][1]
            size_b = self.image.get_size()

            c_x = size_b[0] - size_a[0]
            c_y = size_b[1] - size_a[1]

            self.rect.inflate_ip(c_x, c_y)
            self.update_mask()

            self.rect.bottom = bottom
            self.rect.left = left

    def crouch(self):
        pass

    def transform(self, next_stage, level):
        if next_stage == 1:
            for i in range(9):
                self.image = transform[self.face][i % 2]
                level.draw_screen()
                pygame.display.flip()
                pygame.time.wait(50)
            self.update_hitbox(next_stage)

        if next_stage == 2:
            for i in range(9):
                self.image = fire_transform[self.face][i % 2]
                level.draw_screen()
                pygame.display.flip()
                pygame.time.wait(50)
            self.update_hitbox(next_stage)

    def power_up(self, items, level):
        for item in items:
            if collide_rect(item, self):
                if item.asset_id is self.settings.star_id:
                    self.invincible = self.settings.invincible_time
                elif item.asset_id is self.settings.mushroom_id and self.stage is 0:
                    if self.stage == 0:
                        self.transform(1, level)
                elif item.asset_id is self.settings.green_mushroom_id:
                    pass
                elif item.asset_id is self.settings.flower_id:
                    self.transform(2, level)
                elif item.asset_id is self.settings.coin_id:
                    pass
                if item.asset_id is not self.settings.no_collision_id:
                    item.kill()

    def set_pos(self, start_pos):
        self.rect.left, self.rect.bottom = start_pos

    def save_stage(self):
        pass

    def move_right(self, shift):
        if not self.airborne:
            if self.face is 0:
                self.face = 1
                self.buffer_a = 0
            self.image = walk_right_cycle[self.stage][self.buffer_a // 8]
            self.buffer_a += 1
            if self.buffer_a >= 24:
                self.buffer_a = 0

        if self.delta_x >= 0:
            if (self.delta_x < self.settings.walk_speed and not shift) or (self.delta_x < self.settings.run_speed and shift):
                self.delta_x += self.settings.acceleration_x
        elif self.delta_x < 0:
            self.image = turn[self.stage][self.face]
            self.delta_x += self.settings.decceleration_x

    def move_left(self, shift):
        if not self.airborne:
            if self.face is 1:
                self.face = 0
                self.buffer_a = 0
            self.image = walk_left_cycle[self.stage][self.buffer_a // 8]
            self.buffer_a += 1
            if self.buffer_a >= 24:
                self.buffer_a = 0
        if self.delta_x <= 0:
            if (self.delta_x > -self.settings.walk_speed and not shift) or (self.delta_x > -self.settings.run_speed and shift):
                self.delta_x -= self.settings.acceleration_x
        elif self.delta_x > 0:
            self.image = turn[self.stage][self.face]
            self.delta_x -= self.settings.decceleration_x

    def jump(self):
        if not self.airborne:
            self.airborne = True
            self.buffer_a = 0
            self.buffer_b = 0

        if self.buffer_b < 9 and self.buffer_b % 3 == 0:
            run_bonus = 0
            if abs(self.delta_x) > self.settings.walk_speed:
                run_bonus = (abs(self.delta_x) - self.settings.walk_speed) / 6
            add_velocity_up(self.settings.jump_speed[self.buffer_b // 3] + run_bonus, self)
        self.buffer_b += 1

    def run(self):
        pass

    def fire(self):
        pass

    def bounce(self):
        self.buffer_b = 0
        self.delta_y = 0
        self.jump()

    def take_damage(self):
        if self.invulnerable is False:
            if self.stage > 0:
                print("Mario got hit!")
                self.invul_timer = 100
                self.invulnerable = True
                self.stage = 0
                self.update_hitbox(0)
            else:
                print("Mario died!")
                self.stage = -1
                self.image = death
                self.delta_y = 0

    def land(self):
        self.airborne = False
        self.buffer_b = 0
        self.delta_y = 0

    def update_rel_pos(self):
        self.camera.center_camera(self)
        self.rect.left = self.x - self.camera.x_pos + (self.settings.WIDTH / 2)

    def update(self, floor, blocks, items, enemies, level):
        if self.stage > -1:
            self.power_up(items, level)
            apply_gravity(self.settings, self)

            self.rect.left += self.delta_x
            self.x += self.delta_x
            direction_x = get_direction(self.delta_x)

            if self.airborne:
                self.image = jump[self.stage][self.face]
            if collide_group_x(blocks, self, direction_x):
                direction_x = 0
                self.delta_x = 0
            if (direction_x == 0 and not self.airborne) or collide_check_x(floor, self, direction_x):
                self.image = face[self.stage][self.face]
                self.delta_x = 0
                direction_x = 0
            self.delta_x -= direction_x * self.settings.decceleration_x
            if abs(self.delta_x) < 0.5:
                self.delta_x = 0

            self.rect.bottom += self.delta_y
            direction_y = get_direction(self.delta_y)

            if collide_group_y(blocks, self, direction_y):
                direction_y = 0
                self.delta_y = 0
            if collide_check_y(floor, self, direction_y):
                direction_y = 0
                self.delta_y = 0

            collide_group_y(enemies, self, direction_y)
            collide_group_x(enemies, self, direction_x)

            self.update_rel_pos()

            if self.invulnerable:
                if self.invul_timer % 4 == 0:
                    self.image = pygame.image.load('Resources/Images/Blocks/i_block.png')

                if self.invul_timer == 0:
                    self.invulnerable = False
                self.invul_timer -= 1
        else:
            self.image = death
            if self.death_timer == 180:
                add_velocity_up(15, self)
            elif self.death_timer < 180:
                apply_gravity(self.settings, self)
                self.rect.bottom += self.delta_y
            self.death_timer -= 1

    def draw(self):
        self.screen.blit(self.image, self.rect)
