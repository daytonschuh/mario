import pygame
from pygame.sprite import Sprite
from pygame import *

face_left = pygame.image.load('Resources/images/jumpman/face_left.png')
face_right = pygame.image.load('Resources/images/jumpman/face_right.png')
jump_left = pygame.image.load('Resources/images/jumpman/jump_left.png')
jump_right = pygame.image.load('Resources/images/jumpman/jump_right.png')
jump = [jump_left, jump_right]
turn_left = pygame.image.load('Resources/images/jumpman/turn_left.png')
turn_right = pygame.image.load('Resources/images/jumpman/turn_right.png')
walk_left_1 = pygame.image.load('Resources/images/jumpman/walk_left_1.png')
walk_left_2 = pygame.image.load('Resources/images/jumpman/walk_left_2.png')
walk_left_3 = pygame.image.load('Resources/images/jumpman/walk_left_3.png')
walk_left_cycle = [walk_left_1, walk_left_2, walk_left_3]
walk_right_1 = pygame.image.load('Resources/images/jumpman/walk_right_1.png')
walk_right_2 = pygame.image.load('Resources/images/jumpman/walk_right_2.png')
walk_right_3 = pygame.image.load('Resources/images/jumpman/walk_right_3.png')
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
        self.image = self.get_base_image()
        self.rect = self.image.get_rect()
        self.set_pos(start_pos)
        self.x = self.rect.centerx

        self.jump_velocity = 20
        self.gravity = 1
        self.max_fall_speed = 10
        self.velocity = 0

        self.buffer = 0
        self.airborne = False
        self.face = 0

    def get_base_image(self):
        return face_left

    def update_hitbox(self):
        bottom = self.rect.bottom
#        self.rect = self.image.get_rect()
        self.rect.bottom = bottom

    def set_pos(self, start_pos):
        self.rect.left, self.rect.bottom = start_pos

    def save_stage(self):
        return self.stage

    def move_right(self):
        if not self.airborne:
            if self.face is 1:
                self.face = 0
                self.buffer = 0
            self.image = walk_right_cycle[self.buffer // 9]
            self.buffer += 1
            if self.buffer >= 27:
                self.buffer = 0
            self.x += 5

    def move_left(self):
        if not self.airborne:
            if self.face is 1:
                self.face = 0
                self.buffer = 0
            self.image = walk_left_cycle[self.buffer // 9]
            self.buffer += 1
            if self.buffer >= 27:
                self.buffer = 0
            if self.rect.left - 5 >= 0:
              self.x -= 5

    def jump(self):
        pass

    def update(self):
        self.rect.centerx = self.x - self.camera.x_pos + (self.settings.WIDTH / 2)
        self.camera.center_camera(self)

    def draw(self):
        self.screen.blit(self.image, self.rect)
