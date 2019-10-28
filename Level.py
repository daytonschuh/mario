import pygame
from pygame.sprite import Group
from Background import Background
from camera import Camera
from jumpman import Jumpman
from physics import *
from Scoring import *
from Block import *
from enemy import *
from Item import *


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
        self.score = 0
        self.world = "1-1"
        self.coins = 0
        self.loss = False

        self.enemies = Group()
        self.blocks = Group()
        self.items = Group()
        self.scores = Scoring(self.screen, self.score, self.world, self.coins)

    def place_item(self, item, x, y, block_spawn=False, true_x=None):
        if item is "Coin":
            new_item = Coin(self.screen, self.settings, self.camera, x, y, block_spawn, true_x)
        elif item is "Mushroom":
            new_item = Mushroom(self.screen, self.settings, self.camera, x, y, block_spawn, true_x)
        else:
            new_item = Coin(self.screen, self.settings, self.camera, x, y, block_spawn, true_x)
        self.items.add(new_item)

    def place_enemy(self, enemy, x, y):
        if enemy is 'goomba':
            new_enemy = Goomba(self.screen, self.settings, self.camera, x, y)
        else:
            new_enemy = Enemy(self.screen, self.settings, self.camera, x, y)
        self.enemies.add(new_enemy)

    def place_block(self, block_type, x, y, item=None):
        if block_type is 'q':
            if item is None:
                item = "Coin"
            new_block = QuestionBlock(self.screen, self.settings, self.camera, x, y, self, item)
        elif block_type is 'b':
            new_block = BrickBlock(self.screen, self.settings, self.camera, x, y, self, item)
        elif block_type is 'i':
            if item is None:
                item = "Coin"
            new_block = InvisibleBlock(self.screen, self.settings, self.camera, x, y, self, item)
        else:
            new_block = Block(self.screen, self.settings, self.camera, x, y, self, item)
        self.blocks.add(new_block)

    def mass_place_blocks(self, block_type, x, y, columns=1, rows=1, item=None):
        for column in range(columns):
            for row in range(rows):
                self.place_block(block_type, x + column, y + row, item)

    def update(self):
        self.mario.update(self.floor, self.blocks, self.items)
        self.enemies.update(self.enemies, self.floor, self.blocks, self.mario)
        self.items.update(self.floor, self.blocks)
        self.blocks.update()
        self.background.update()
        self.floor.update()
        self.scores.update_text()
        enemy_to_enemy_collision(self.enemies)

    def update_mario(self, left, right, space, shift, fire):
        if left:
            self.mario.move_left(shift)
        elif right:
            self.mario.move_right(shift)
        if space:
            self.mario.jump()
        if fire:
            self.mario.fire()

    def draw_screen(self):
        self.background.draw()
        self.floor.draw()
        self.mario.draw()
        self.enemies.draw(self.screen)
        self.scores.draw_text()
        self.items.draw(self.screen)
        self.blocks.draw(self.screen)
