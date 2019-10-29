import pygame
from pygame.sprite import Sprite
from Timer import Timer
from physics import *


coin1 = pygame.image.load('Resources/Images/Items/coin.png')
coin2 = pygame.image.load('Resources/Images/Items/coin2.png')
coin3 = pygame.image.load('Resources/Images/Items/coin3.png')
coin4 = pygame.image.load('Resources/Images/Items/coin4.png')
coin5 = pygame.image.load('Resources/Images/Items/coin5.png')
coin = [coin1, coin2, coin3, coin4, coin5]
mushroom = pygame.image.load('Resources/Images/Items/mushroom.png')
green_mushroom = pygame.image.load('Resources/Images/Items/green_mushroom.png')
star = pygame.image.load('Resources/Images/Items/star.png')
flower_a = pygame.image.load('Resources/Images/Items/flower_a.png')
flower_b = pygame.image.load('Resources/Images/Items/flower_b.png')
flower_c = pygame.image.load('Resources/Images/Items/flower_c.png')
flower_d = pygame.image.load('Resources/Images/Items/flower_d.png')
flower = [flower_a, flower_b, flower_c, flower_d]



class Mushroom(Sprite):
    def __init__(self, screen, settings, camera, x, y, scores, block_spawn=False, true_x=None):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.image = mushroom
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        if true_x is None:
            self.x = x * settings.block_size + self.camera.x_pos
        else:
            self.x = true_x
        self.rect.left = self.x - self.camera.x_pos + self.settings.block_size/2 - self.image.get_size()[0]/2
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size)
        self.block_spawn = block_spawn
        self.delta_x = 1
        self.delta_y = 0
        self.score = 1000
        self.scores = scores
        self.rise_timer = 48
        self.rise = -1
        if block_spawn:
            self.asset_id = self.settings.no_collision_id
        else:
            self.asset_id = self.settings.mushroom_id

    def land(self):
        self.delta_y = 0

    def bounce(self):
        add_velocity_up(12, self)

    def update(self, floor, blocks):
        if self.block_spawn:
            self.rect.left = self.x - self.camera.x_pos
            if self.rise_timer > 0:
                self.rect.bottom += self.rise
                self.rise_timer -= 1
            else:
                self.block_spawn = False
                self.asset_id = self.settings.mushroom_id
        else:
            self.rect.left = self.x - self.camera.x_pos
            self.rect.left += self.delta_x
            self.x += self.delta_x
            direction_x = get_direction(self.delta_x)
            if collide_group_x(blocks, self, direction_x):
                self.delta_x *= -1
                direction_x = 0
            if collide_check_x(floor, self, direction_x):
                self.delta_x *= -1

            apply_gravity(self.settings, self)
            self.rect.bottom += self.delta_y
            direction_y = get_direction(self.delta_y)
            if collide_group_y(blocks, self, direction_y):
                self.delta_y = 0
                if direction_y > 0:
                    self.land()
                direction_y = 0
            if collide_check_y(floor, self, direction_y):
                self.delta_y = 0
                if direction_y > 0:
                    self.land()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def eat_mushroom(self):
        self.kill()
        self.scores.scores += self.score


class FireFlower(Mushroom):
    def __init__(self, screen, settings, camera, x, y, scores, block_spawn=False, true_x=None):
        super().__init__(screen, settings, camera, x, y, scores, block_spawn, true_x)
        self.delta_x = 0
        self.score = 200
        self.image = flower_a
        self.frame = 0
        if block_spawn:
            self.asset_id = self.settings.no_collision_id
        else:
            self.asset_id = self.settings.flower_id

    def update(self, floor, blocks):
        super().update(floor, blocks)
        if self.asset_id == self.settings.mushroom_id:
            self.asset_id = self.settings.flower_id

        if self.frame % 4 == 0:
            self.image = flower[self.frame//4]

        self.frame += 1
        if self.frame >= 16:
            self.frame = 0

    def eat_flower(self):
        self.kill()
        self.scores.scores += self.score


class Star(Mushroom):
    def __init__(self, screen, settings, camera, x, y, scores, block_spawn=False, true_x=None):
        super().__init__(screen, settings, camera, x, y, scores, block_spawn, true_x)
        self.image = star
        self.score = 200
        self.delta_x = 2
        if block_spawn:
            self.asset_id = self.settings.no_collision_id
        else:
            self.asset_id = self.settings.star_id

    def land(self):
        super().land()
        self.bounce()

    def bounce(self):
        add_velocity_up(15, self)

    def update(self, floor, blocks):
        super().update(floor, blocks)
        if self.asset_id == self.settings.mushroom_id:
            self.asset_id = self.settings.star_id

    def eat_star(self):
        self.kill()
        self.scores.scores += self.score


class GreenMushroom(Mushroom):
    def __init__(self, screen, settings, camera, x, y, scores, block_spawn=False, true_x=None):
        super().__init__(screen, settings, camera, x, y, scores, block_spawn, true_x)
        self.image = green_mushroom
        self.score = 2000
        if block_spawn:
            self.asset_id = self.settings.no_collision_id
        else:
            self.asset_id = self.settings.green_mushroom_id

    def update(self, floor, blocks):
        super().update(floor, blocks)
        if self.asset_id == self.settings.mushroom_id:
            self.asset_id = self.settings.green_mushroom_id

    def eat_green_mushroom(self):
        self.kill()
        #Give player 1+ life
        self.scores.scores += self.score


class Coin(Sprite):
    def __init__(self, screen, settings, camera, x, y, scores, block_spawn=False, true_x=None):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.state = 0
        self.image = coin[self.state]
        self.rect = self.image.get_rect()
        self.scores = scores
        self.score = 500
        if true_x is None:
            self.x = x * settings.block_size + self.camera.x_pos
        else:
            self.x = true_x
        self.rect.left = self.x - self.camera.x_pos + self.settings.block_size/2 - self.image.get_size()[0]/2
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size) - self.settings.block_size/2 + self.image.get_size()[1]/2
        self.block_spawn = block_spawn
        self.delta_x = 0
        self.delta_y = 0
        if not self.block_spawn:
            self.asset_id = self.settings.coin_id
            self.timer = Timer(12)
        else:
            self.asset_id = self.settings.no_collision_id
            self.timer = Timer(1)

    def update(self, floor, blocks):
        self.timer.tick()
        if self.timer.check():
            self.state += 1
            self.state %= len(coin)
            self.image = coin[self.state]
        self.rect.left = self.x - self.camera.x_pos + self.settings.block_size / 2 - self.image.get_size()[0] / 2

        if self.block_spawn:
            add_velocity_up(10, self)
            self.block_spawn = False
        if self.delta_y is not 0:
            self.rect.bottom += self.delta_y
            apply_gravity(self.settings, self)
            if self.delta_y >= self.settings.gravity_max/2:
                self.eat_coin()

    def eat_coin(self):
        self.kill()
        self.scores.scores += self.score

    def spawn(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
