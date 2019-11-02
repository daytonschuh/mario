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
from Fireball import *
from LevelCreator import *


class Level:
    def __init__(self, screen, settings, bg_img, floor_img, mario_pos, flag_pos, time, world, level_id, next_id, respawn_id, swim=False, castle=False):
        self.screen = screen
        self.settings = settings
        self.camera = Camera(self.settings, pygame.image.load(bg_img))
        self.background = Background(self.screen, self.settings, self.camera, bg_img)
        self.floor = Background(self.screen, self.settings, self.camera, floor_img)

        self.mario = Jumpman(self.screen, self.settings, self.camera, 0, 0, mario_pos, swim)
        self.flag = FlagPole(self.screen, self.settings, self.camera, flag_pos[0], flag_pos[1], castle)
        self.time = time
        self.score = 0

        self.world = world
        self.level_id = level_id
        self.next_id = next_id
        self.respawn_id = respawn_id
        self.coins = 0
        self.loss = False

        self.enemies = Group()
        self.blocks = Group()
        self.items = Group()
        self.warps = Group()
        self.fireballs = Group()
        self.scores = Scoring(self.screen, self.score, self.world, self.coins)

        self.screen_fill = False

    def place_warp(self, level_name, direction, x, y):
        new_warp = Warp(self.screen, self.settings, self.camera, x, y, direction, level_name)
        self.warps.add(new_warp)

    def place_item(self, item, x, y, block_spawn=False, true_x=None):
        if item == "Coin":
            new_item = Coin(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
        elif item == "Power-Up":
            if self.mario.stage == 0:
                new_item = Mushroom(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
            else:
                new_item = FireFlower(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
        elif item == "1-Up":
            new_item = GreenMushroom(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
        elif item == "Star":
            new_item = Star(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
        else:
            new_item = Coin(self.screen, self.settings, self.camera, x, y, self.scores, block_spawn, true_x)
        self.items.add(new_item)

    def place_enemy(self, enemy, x, y):
        if enemy is 'goomba':
            new_enemy = Goomba(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'koopa':
            new_enemy = Koopa_Troopa(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'piranha_plant':
            new_enemy = Piranha_Plant(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'koopa_paratroopa':
            new_enemy = Koopa_Paratroopa(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'fire_bar':
            new_enemy = Fire_Bar(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'bowser':
            new_enemy = Bowser(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'blooper':
            new_enemy = Blooper(self.screen, self.settings, self.camera, x, y)
        elif enemy is 'cheep_cheep':
            new_enemy = Cheep_Cheep(self.screen, self.settings, self.camera, x, y, self.mario.swim)
        elif enemy is 'lava_bubble':
            new_enemy = Lava_Bubble(self.screen, self.settings, self.camera, x, y)
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
        elif block_type is 'ub':
            new_block = UndergroundBrickBlock(self.screen, self.settings, self.camera, x, y, self, item)
        elif block_type is 'plt':
            new_block = Platform(self.screen, self.settings, self.camera, x, y, self)
        elif block_type is 'invert_plt':
            new_block = invert_Platform(self.screen, self.settings, self.camera, x, y, self)
        elif block_type is 'horiz_plt':
            new_block = horizontal_Platform(self.screen, self.settings, self.camera, x, y, self)
        elif block_type is 'invert_horiz_plt':
            new_block = invert_horizontal_Platform(self.screen, self.settings, self.camera, x, y, self)
        elif block_type is 'vert_plt':
            new_block = vertical_Platform(self.screen, self.settings, self.camera, x, y, self)
        elif block_type is 'invis_plt':
            new_block = Uni_directional_platform(self.screen, self.settings, self.camera, x, y, self)
        else:
            new_block = Block(self.screen, self.settings, self.camera, x, y, self, item)
        self.blocks.add(new_block)

    def mass_place_blocks(self, block_type, x, y, columns=1, rows=1, item=None):
        for column in range(columns):
            for row in range(rows):
                self.place_block(block_type, x + column, y + row, item)

    def update(self):
        if self.flag.grabbed is False:
            self.mario.update(self.floor, self.blocks, self.items, self.enemies, self.flag, self)
            self.enemies.update(self.enemies, self.floor, self.blocks, self.mario)
            self.items.update(self.floor, self.blocks)
            self.blocks.update()
            self.background.update()
            self.floor.update()
            self.scores.update_text()
            enemy_to_enemy_collision(self.enemies)
            self.flag.update()
            self.warps.update()
            self.fireballs.update(self.floor, self.enemies, self.blocks)

        else:
            self.mario.update(self.floor, self.blocks, self.items, self.enemies, self.flag, self)
            self.blocks.update()
            self.background.update()
            self.floor.update()
            self.flag.update()
            self.fireballs.update(self.floor, self.enemies, self.blocks)

    def update_mario(self, left, right, space, shift, down, fire):
        for warp in self.warps:
            warp.check(self.mario, down, left, right)
        if self.mario.stage > -1 and self.flag.asset_id is not self.settings.auto_id and self.mario.my_warp is None:
            if down:
                if self.mario.stage > 0:
                    self.mario.crouching = True
            if left:
                if not self.mario.swim:
                    self.mario.move_left(shift)
                else:
                    self.mario.swim_left()
            elif right:
                if not self.mario.swim:
                    self.mario.move_right(shift)
                else:
                    self.mario.swim_right()

            if space:
                if not self.mario.swim:
                    self.mario.jump()
                else:
                    self.mario.swim_up()

            if fire:
                self.mario.fire(self.fireballs)

    def draw_screen(self):
        self.background.draw()
        self.mario.draw()
        if not self.mario.swim:
            self.enemies.draw(self.screen)
            self.floor.draw()
        else:
            self.floor.draw()
            self.enemies.draw(self.screen)
        self.items.draw(self.screen)
        self.blocks.draw(self.screen)
        self.flag.draw()
        self.warps.draw(self.screen)
        self.fireballs.draw(self.screen)
        self.scores.draw_text()

        if self.mario.my_warp is not None:
            if self.mario.my_warp.do_load is True:
                self.level_id = self.mario.my_warp.level_id
                self.screen.fill((0, 0, 0))
                pygame.display.flip()
                time.wait(100)
        elif self.mario.reset_timer == 0:
            self.level_id = self.next_id
            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            time.wait(100)
