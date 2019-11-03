from pygame import *
from Fireball import *

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
walk_left_cycle = [[walk_left_1, walk_left_2, walk_left_3], [big_walk_left_1, big_walk_left_2, big_walk_left_3],
                   [fire_walk_left_1, fire_walk_left_2, fire_walk_left_3]]
walk_right_1 = pygame.image.load('Resources/Images/Baby_mario/walk_right_1.png')
walk_right_2 = pygame.image.load('Resources/Images/Baby_mario/walk_right_2.png')
walk_right_3 = pygame.image.load('Resources/Images/Baby_mario/walk_right_3.png')
big_walk_right_1 = pygame.image.load('Resources/Images/Papa_mario/walk_right_1.png')
big_walk_right_2 = pygame.image.load('Resources/Images/Papa_mario/walk_right_2.png')
big_walk_right_3 = pygame.image.load('Resources/Images/Papa_mario/walk_right_3.png')
fire_walk_right_1 = pygame.image.load('Resources/Images/Fire_mario/walk_right_1.png')
fire_walk_right_2 = pygame.image.load('Resources/Images/Fire_mario/walk_right_2.png')
fire_walk_right_3 = pygame.image.load('Resources/Images/Fire_mario/walk_right_3.png')
walk_right_cycle = [[walk_right_1, walk_right_2, walk_right_3], [big_walk_right_1, big_walk_right_2, big_walk_right_3],
                    [fire_walk_right_1, fire_walk_right_2, fire_walk_right_3]]
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
crouch_l = pygame.image.load('Resources/Images/Papa_mario/crouch_left.png')
crouch_r = pygame.image.load('Resources/Images/Papa_mario/crouch_right.png')
f_crouch_l = pygame.image.load('Resources/Images/Fire_mario/crouch_left.png')
f_crouch_r = pygame.image.load('Resources/Images/Fire_mario/crouch_right.png')
crouch = [[crouch_l, crouch_r], [f_crouch_l, f_crouch_r]]
l_grab = pygame.image.load('Resources/Images/Baby_mario/flagpole.png')
b_grab = pygame.image.load('Resources/Images/Papa_mario/flagpole.png')
f_grab = pygame.image.load('Resources/Images/Fire_mario/flagpole.png')
grab = [l_grab, b_grab, f_grab]
fire_left = pygame.image.load('Resources/Images/Fire_mario/fire_left.png')
fire_right = pygame.image.load('Resources/Images/Fire_mario/fire_right.png')
fire = [fire_left, fire_right]
swim_left_1 = pygame.image.load('Resources/Images/Baby_mario/swim_left_1.png')
swim_left_2 = pygame.image.load('Resources/Images/Baby_mario/swim_left_2.png')
swim_left_3 = pygame.image.load('Resources/Images/Baby_mario/swim_left_3.png')
swim_left_4 = pygame.image.load('Resources/Images/Baby_mario/swim_left_4.png')
swim_right_1 = pygame.image.load('Resources/Images/Baby_mario/swim_right_1.png')
swim_right_2 = pygame.image.load('Resources/Images/Baby_mario/swim_right_2.png')
swim_right_3 = pygame.image.load('Resources/Images/Baby_mario/swim_right_3.png')
swim_right_4 = pygame.image.load('Resources/Images/Baby_mario/swim_right_4.png')
b_swim_left_1 = pygame.image.load('Resources/Images/Papa_mario/swim_left_1.png')
b_swim_left_2 = pygame.image.load('Resources/Images/Papa_mario/swim_left_2.png')
b_swim_left_3 = pygame.image.load('Resources/Images/Papa_mario/swim_left_3.png')
b_swim_left_4 = pygame.image.load('Resources/Images/Papa_mario/swim_left_4.png')
b_swim_right_1 = pygame.image.load('Resources/Images/Papa_mario/swim_right_1.png')
b_swim_right_2 = pygame.image.load('Resources/Images/Papa_mario/swim_right_2.png')
b_swim_right_3 = pygame.image.load('Resources/Images/Papa_mario/swim_right_3.png')
b_swim_right_4 = pygame.image.load('Resources/Images/Papa_mario/swim_right_4.png')
f_swim_left_1 = pygame.image.load('Resources/Images/Fire_mario/swim_left_1.png')
f_swim_left_2 = pygame.image.load('Resources/Images/Fire_mario/swim_left_2.png')
f_swim_left_3 = pygame.image.load('Resources/Images/Fire_mario/swim_left_3.png')
f_swim_left_4 = pygame.image.load('Resources/Images/Fire_mario/swim_left_4.png')
f_swim_right_1 = pygame.image.load('Resources/Images/Fire_mario/swim_right_1.png')
f_swim_right_2 = pygame.image.load('Resources/Images/Fire_mario/swim_right_2.png')
f_swim_right_3 = pygame.image.load('Resources/Images/Fire_mario/swim_right_3.png')
f_swim_right_4 = pygame.image.load('Resources/Images/Fire_mario/swim_right_4.png')
s_swim_list = [[swim_left_1, swim_left_2, swim_left_3, swim_left_4],
               [swim_right_1, swim_right_2, swim_right_3, swim_right_4]]
b_swim_list = [[b_swim_left_1, b_swim_left_2, b_swim_left_3, b_swim_left_4],
               [b_swim_right_1, b_swim_right_2, b_swim_right_3, b_swim_right_4]]
f_swim_list = [[f_swim_left_1, f_swim_left_2, f_swim_left_3, f_swim_left_4],
               [f_swim_right_1, f_swim_right_2, f_swim_right_3, f_swim_right_4]]
swim_list = [s_swim_list, b_swim_list, f_swim_list]

pygame.mixer.init()
mariodie = pygame.mixer.Sound("Resources/Sounds/smb_mariodie.wav")


class Jumpman(Sprite):
    def __init__(self, screen, settings, camera, stage, style, start_pos, swim=False):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.stage = 2
        self.style = style
        self.state = 0
        self.image = face[self.stage][1]
        self.rect = self.image.get_rect()
        self.mask = None
        self.update_mask(self.image)
        self.set_pos(start_pos)
        self.swim = swim
        self.asset_id = self.settings.mario_id
        self.crouching = False
        self.fireball_delay = 0
        self.reset_timer = 240
        self.level = stage

        self.x = self.rect.left
        self.delta_x = 0
        self.delta_y = 0
        self.buffer_a = 0
        self.buffer_b = 0
        self.buffer_c = 0

        self.airborne = False
        self.run = False
        self.face = 1
        self.invincible = 0
        self.invulnerable = False
        self.invul_timer = 100
        self.death_timer = 240
        self.my_warp = None

    def update_mask(self, plyr_image):
        self.mask = pygame.mask.from_surface(plyr_image)

    def update_hitbox(self, hitbox_size):
        bottom = self.rect.bottom
        left = self.rect.left

        if hitbox_size == 0:
            self.rect = face_left.get_rect()
            self.update_mask(face_left)
        else:
            self.rect = big_face_right.get_rect()
            self.update_mask(big_face_left)
        self.rect.bottom = bottom
        self.rect.left = left
        return

    def crouch(self):
        if self.stage > 0 and not self.swim:
            self.update_hitbox(0)
            self.image = crouch[self.stage-1][self.face]
        self.crouching = False

    def transform(self, next_stage, level):
        self.update_hitbox(next_stage)

        if next_stage == 1:
            for i in range(9):
                self.image = transform[self.face][i % 2]
                level.draw_screen()
                pygame.display.flip()
                pygame.time.wait(50)

        if next_stage == 2:
            for i in range(9):
                self.image = fire_transform[self.face][i % 2]
                level.draw_screen()
                pygame.display.flip()
                pygame.time.wait(50)

    def power_up(self, items, level):
        for item in items:
            if collide_rect(item, self):
                if item.asset_id is self.settings.star_id:
                    item.eat_star()
                    self.invulnerable = True
                    self.invul_timer = 600
                    self.asset_id = self.settings.star_power_id
                elif item.asset_id is self.settings.mushroom_id and self.stage is 0:
                    item.eat_mushroom()
                    if self.stage == 0:
                        self.transform(1, level)
                        self.stage = 1
                elif item.asset_id is self.settings.green_mushroom_id:
                    item.eat_green_mushroom()
                elif item.asset_id is self.settings.flower_id:
                    if self.stage < 2:
                        self.transform(2, level)
                        self.stage = 2
                    item.eat_flower()
                elif item.asset_id is self.settings.coin_id:
                    item.eat_coin()
                if item.asset_id is not self.settings.no_collision_id:
                    item.kill()

    def set_pos(self, start_pos):
        self.rect.left = start_pos[0] * self.settings.block_size
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + start_pos[1]) * self.settings.block_size)

    def save_stage(self):
        pass

    def move_right(self, shift):
        if not self.crouching or self.airborne:
            if not self.airborne:
                if self.face is 0:
                    self.face = 1
                    self.buffer_a = 0
                self.image = walk_right_cycle[self.stage][self.buffer_a // 8]
                self.buffer_a += 1
                if shift:
                    self.buffer_a += 1
                if self.buffer_a >= 24:
                    self.buffer_a = 0

            if self.delta_x >= 0:
                if (self.delta_x < self.settings.walk_speed and not shift) or\
                        (self.delta_x < self.settings.run_speed and shift):
                    self.delta_x += self.settings.acceleration_x
            elif self.delta_x < 0:
                self.image = turn[self.stage][self.face]
                self.delta_x += self.settings.decceleration_x

    def swim_up(self):
        if self.buffer_b == 0:
            self.delta_y = 0
            self.airborne = True
            add_velocity_up(self.settings.swim_up_speed, self)
            self.buffer_b = 10

    def swim_right(self):
        if self.face is 0:
            self.face = 1
        if 0 <= self.delta_x < self.settings.swim_max_speed:
            self.delta_x += self.settings.acceleration_x
        elif self.delta_x < 0:
            self.delta_x += self.settings.decceleration_x

    def swim_left(self):
        if self.face is 1:
            self.face = 0
        if 0 >= self.delta_x > -self.settings.swim_max_speed:
            self.delta_x -= self.settings.acceleration_x
        elif self.delta_x > 0:
            self.delta_x -= self.settings.decceleration_x

    def move_left(self, shift):
        if not self.crouching or self.airborne:
            if not self.airborne:
                if self.face is 1:
                    self.face = 0
                    self.buffer_a = 0
                self.image = walk_left_cycle[self.stage][self.buffer_a // 8]
                self.buffer_a += 1
                if shift:
                    self.buffer_a += 1
                if self.buffer_a >= 24:
                    self.buffer_a = 0
            if self.delta_x <= 0:
                if (self.delta_x > -self.settings.walk_speed and not shift) or\
                        (self.delta_x > -self.settings.run_speed and shift):
                    self.delta_x -= self.settings.acceleration_x
            elif self.delta_x > 0:
                self.image = turn[self.stage][self.face]
                self.delta_x -= self.settings.decceleration_x

    def jump(self):
        if not self.airborne or self.swim:
            self.airborne = True
            self.buffer_a = 0
            self.buffer_b = 0

        if self.buffer_b < 9 and self.buffer_b % 3 == 0:
            run_bonus = 0
            if abs(self.delta_x) > self.settings.walk_speed:
                run_bonus = (abs(self.delta_x) - self.settings.walk_speed) / 6
            add_velocity_up(self.settings.jump_speed[self.buffer_b // 3] + run_bonus, self)
        self.buffer_b += 1

    def fire(self, fireballs):
        if self.stage == 2 and len(fireballs) < 2 and self.fireball_delay == 0:
            x = self.x + self.settings.WIDTH / 2 - self.settings.block_size / 6 +\
                self.face * face[self.stage][1].get_size()[1] / 2
            new_fireball = Fireball(self.screen, self.settings, self.camera, x, self.rect.centery, self.face)
            fireballs.add(new_fireball)
            self.fireball_delay = 20

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
                pygame.mixer.Sound.play(mariodie)
                self.delta_y = 0

    def land(self):
        self.airborne = False
        self.buffer_b = 0
        self.delta_y = 0

    def update_rel_pos(self):
        self.camera.center_camera(self)
        self.rect.left = self.x - self.camera.x_pos + (self.settings.WIDTH / 2)
        self.update_hitbox(self.stage)

    def warp(self, level):
        if self.my_warp.direction == "down":
            if self.rect.centerx != self.my_warp.rect.centerx:
                if abs(self.my_warp.rect.centerx - self.rect.centerx) < 1:
                    self.rect.centerx = self.my_warp.rect.centerx
                    self.x.centerx = self.my_warp.rect.centerx
                elif self.my_warp.rect.centerx > self.rect.centerx:
                    self.rect.centerx += 1.5
                    self.x += 1.5
                else:
                    self.rect.centerx -= 1
                    self.x += 1

            elif self.rect.top < self.my_warp.rect.centery:
                self.rect.top += 1

            else:
                self.my_warp.load_level()

            self.level = level

        else:
            if self.rect.bottom < self.my_warp.rect.bottom:
                self.rect.bottom = self.my_warp.rect.bottom
            if self.rect.left < self.my_warp.rect.centerx and self.my_warp.direction == "right":
                self.rect.left += 1.5
                self.x += 1.5

            elif self.rect.right > self.my_warp.rect.centerx and self.my_warp.direction == "left":
                self.rect.left -= 1.5
                self.x -= 1.5
            else:
                self.my_warp.load_level()

    def get_base_image(self):
        if not self.swim:
            self.image = face[self.stage][self.face]
        else:
            self.image = swim_list[self.stage][self.face][1]
        self.update_hitbox(self.stage)

    def update(self, floor, blocks, items, enemies, flag, level):
        if flag.grabbed is False:
            if self.my_warp is not None:
                self.get_base_image()
                self.warp(level)
                return

            if flag.asset_id == self.settings.auto_id:
                if not self.swim:
                    self.move_right(False)
                else:
                    self.swim_right()
                self.reset_timer -= 1

            if self.stage > -1:
                self.live_update(floor, blocks, items, enemies, flag, level)

            else:
                self.image = death
                if self.death_timer == 180:
                    add_velocity_up(15, self)
                elif self.death_timer < 180:
                    apply_gravity(self.settings, self)
                    self.rect.bottom += self.delta_y
                self.death_timer -= 1
                if self.death_timer == 0:
                    if level.level_id == level.respawn_id:
                        level.level_id = None
                    else:
                        level.level_id = level.respawn_id

        else:
            self.delta_x = 0
            if flag.castle is False:
                self.image = grab[self.stage]
                self.rect.right = flag.flag_rect.right
                if self.rect.bottom + self.settings.flag_fall < flag.rect.bottom:
                    self.rect.bottom += self.settings.flag_fall
                else:
                    self.rect.bottom = flag.rect.bottom

    def swim_update(self):
        if self.crouching and not self.airborne:
            self.crouch()
        elif self.fireball_delay > 4:
            self.image = fire[self.face]
        elif self.airborne and not self.crouching:
            self.image = swim_list[self.stage][self.face][0]
        elif self.delta_x == 0 and not self.airborne and not self.crouching:
            self.image = face[self.stage][self.face]

        self.image = swim_list[self.stage][self.face][self.buffer_a // 18]
        self.buffer_a += 1
        if self.buffer_a >= 72:
            self.buffer_a = 0

        if self.buffer_b > 0:
            self.buffer_b -= 1

    def land_update(self):
        if self.crouching:
            self.crouch()
        elif self.fireball_delay > 4:
            self.image = fire[self.face]
        elif self.airborne and not self.crouching:
            self.image = jump[self.stage][self.face]
        elif self.delta_x == 0 and not self.airborne and not self.crouching:
            self.image = face[self.stage][self.face]

    def live_update(self, floor, blocks, items, enemies, flag, level):
        if self.fireball_delay > 0:
            self.fireball_delay -= 1

        self.update_rel_pos()

        if not self.swim:
            self.land_update()
        else:
            self.swim_update()

        self.power_up(items, level)
        apply_gravity(self.settings, self, self.swim)

        self.rect.left += self.delta_x
        self.x += self.delta_x
        self.delta_x -= get_direction(self.delta_x) * self.settings.decceleration_x
        if abs(self.delta_x) < 0.5:
            self.delta_x = 0
        direction_x = get_direction(self.delta_x)
        if collide_group_x(blocks, self, direction_x) or collide_check_x(floor, self, direction_x):
            self.delta_x = 0
            direction_x = 0
        if self.rect.left < 0:
            c_x = self.rect.left
            self.rect.left = 0
            self.x -= c_x

        self.rect.bottom += self.delta_y
        direction_y = get_direction(self.delta_y)

        if collide_group_y(blocks, self, direction_y) or collide_check_y(floor, self, direction_y):
            direction_y = 0
            self.delta_y = 0
        elif self.delta_y > self.settings.gravity:
            self.airborne = True

        collide_group_y(enemies, self, direction_y)
        collide_group_x(enemies, self, direction_x)

        if self.invulnerable:
            if self.invul_timer % 4 == 0:
                self.image = pygame.image.load('Resources/Images/Blocks/i_block.png')

            if self.invul_timer == 0:
                self.invulnerable = False
                self.asset_id = self.settings.mario_id
            self.invul_timer -= 1

        if collide_rect(flag, self):
            flag.grab()
            for item in items:
                item.kill()
            for enemy in enemies:
                enemy.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
