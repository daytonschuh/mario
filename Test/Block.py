import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, game, image_file):
        super().__init__()
        self.screen = game.screen

        self.watch = pygame.time.Clock()
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.y = 545

        self.x = float(self.rect.x)

    def draw_block(self):
        self.screen.blit(self.image, self.rect)
