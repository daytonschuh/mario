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


class Coin(Sprite):
    def __init__(self, screen, settings, camera, x, y, block_spawn=False, true_x=None):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.state = 0
        self.image = coin[self.state]
        self.rect = self.image.get_rect()
        self.score = 100
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
            self.asset_id = self.settings.item_id
            self.timer = Timer(12)
        else:
            self.asset_id = self.settings.no_collision_id
            self.timer = Timer(1)

    def update(self):
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
                self.kill()


    def spawn(self):
        pass

    def draw(self):
        self.screen.blit(self.image, self.rect)
