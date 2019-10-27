import pygame
from pygame.sprite import Sprite
from Timer import Timer

coin1 = pygame.image.load('Resources/Images/Items/coin.png')
coin2 = pygame.image.load('Resources/Images/Items/coin2.png')
coin3 = pygame.image.load('Resources/Images/Items/coin3.png')
coin4 = pygame.image.load('Resources/Images/Items/coin4.png')
coin5 = pygame.image.load('Resources/Images/Items/coin5.png')
coin = [coin1, coin2, coin3, coin4, coin5]


class Coin(Sprite):
    def __init__(self, screen, settings, camera, x, y, block_spawn=False):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.state = 0
        self.image = coin[self.state]
        self.rect = self.image.get_rect()
        self.score = 100
        self.rect.left = x * settings.block_size + self.camera.x_pos + 12
        self.x = self.rect.left
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size) - 3
        self.timer = Timer(12)
        self.spawned = not block_spawn

    def update(self):
        if self.spawned:
            self.timer.tick()
            if self.timer.check():
                self.state += 1
                self.state %= len(coin)
                self.image = coin[self.state]
        else:
            pass
