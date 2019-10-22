import pygame
from pygame.sprite import Group
from Background import Background
from camera import Camera
from jumpman import Jumpman


class Level:
    def __init__(self, screen, settings, bg_img, floor_img, mario_pos, flag_pos, time):
        self.screen = screen
        self.settings = settings
        self.camera = Camera(self.settings, pygame.image.load(bg_img))
        self.background = Background(self.screen, self.settings, self.camera, bg_img)
        self.floor = Background(self.screen, self.settings, self.camera, floor_img)

        self.mario = Jumpman(self.screen, self.settings, self.camera, 0, 0, mario_pos)
        self.flag_pos = flag_pos
        self.time = time

        self.enemies = Group()
        # self.objects = Group()

    def place_enemy(self, enemy):
        pass

    def place_block(self, block):
        pass

    def update(self):
        self.mario.update()
        self.background.update()
        self.floor.update()

    def draw_screen(self):
        self.background.draw()
        self.floor.draw()
        self.mario.draw()
        self.enemies.draw(self.screen)

