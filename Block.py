import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, screen,  image, x, y):
        super().__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def draw_block(self):
        self.screen.blit(self.image, self.rect)
