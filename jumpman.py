import pygame
from pygame.sprite import Sprite
from pygame import *
from physics import *

face_left = pygame.image.load('Resources/Images/jumpman/face_left.png')
face_right = pygame.image.load('Resources/Images/jumpman/face_right.png')
face = [face_left, face_right]
jump_left = pygame.image.load('Resources/Images/jumpman/jump_left.png')
jump_right = pygame.image.load('Resources/Images/jumpman/jump_right.png')
jump = [jump_left, jump_right]
turn_left = pygame.image.load('Resources/Images/jumpman/turn_left.png')
turn_right = pygame.image.load('Resources/Images/jumpman/turn_right.png')
walk_left_1 = pygame.image.load('Resources/Images/jumpman/walk_left_1.png')
walk_left_2 = pygame.image.load('Resources/Images/jumpman/walk_left_2.png')
walk_left_3 = pygame.image.load('Resources/Images/jumpman/walk_left_3.png')
walk_left_cycle = [walk_left_1, walk_left_2, walk_left_3]
walk_right_1 = pygame.image.load('Resources/Images/jumpman/walk_right_1.png')
walk_right_2 = pygame.image.load('Resources/Images/jumpman/walk_right_2.png')
walk_right_3 = pygame.image.load('Resources/Images/jumpman/walk_right_3.png')
walk_right_cycle = [walk_right_1, walk_right_2, walk_right_3]


class Jumpman(Sprite):
    def __init__(self, screen, settings, camera, stage, style, start_pos):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.stage = stage
        self.style = style
        self.state = 0
        self.image = face_right
        self.rect = self.image.get_rect()
        self.mask = None
        self.update_mask()
        self.set_pos(start_pos)

        self.x = self.rect.left
        self.delta_x = 0
        self.delta_y = 0
        self.buffer_a = 0
        self.buffer_b = 0
        self.airborne = False
        self.run = False
        self.face = 0

    def update_mask(self):
        self.mask = pygame.mask.from_surface(self.image)

    def update_hitbox(self):
        bottom = self.rect.bottom
        left = self.rect.left
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def set_pos(self, start_pos):
        self.rect.left, self.rect.bottom = start_pos

    def save_stage(self):
        pass

    def move_right(self, shift):
        if not self.airborne:
            if self.face is 0:
                self.face = 1
                self.buffer_a = 0
            self.image = walk_right_cycle[self.buffer_a // 8]
            self.buffer_a += 1
            if self.buffer_a >= 24:
                self.buffer_a = 0

        self.delta_x = self.settings.walk_speed

    def move_left(self, shift):
        if not self.airborne:
            if self.face is 1:
                self.face = 0
                self.buffer_a = 0
            self.image = walk_left_cycle[self.buffer_a // 8]
            self.buffer_a += 1
            if self.buffer_a >= 24:
                self.buffer_a = 0
        if self.rect.left - self.settings.walk_speed >= 0:
            self.delta_x = -self.settings.walk_speed

    def jump(self):
        if not self.airborne:
            self.airborne = True
            self.buffer_a = 0
            self.buffer_b = 0

        if self.buffer_b < 9 and self.buffer_b % 3 == 0:
            add_velocity_up(self.settings.jump_speed[self.buffer_b // 3], self)
        self.buffer_b += 1

    def run(self):
        pass

    def fire(self):
        pass

    def bounce(self):
        pass

    def land(self):
        self.airborne = False
        self.buffer_b = 0
        self.delta_y = 0

    def update_rel_pos(self):
        self.camera.center_camera(self)
        self.rect.left = self.x - self.camera.x_pos + (self.settings.WIDTH / 2)

    def update(self, floor, blocks):
        apply_gravity(self.settings, self)

        self.rect.left += self.delta_x
        self.x += self.delta_x
        direction_x = get_direction(self.delta_x)

        if self.airborne:
            self.image = jump[self.face]
        if collide_group_x(blocks, self, direction_x):
            direction_x = 0
        if (direction_x == 0 and not self.airborne)or collide_check_x(floor, self, direction_x):
            self.image = face[self.face]

        self.rect.bottom += self.delta_y
        direction_y = get_direction(self.delta_y)

        if collide_group_y(blocks, self, direction_y, "Block"):
            direction_y = 0
            self.delta_y = 0
        collide_check_y(floor, self, direction_y)

        self.update_rel_pos()
        self.delta_x = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)