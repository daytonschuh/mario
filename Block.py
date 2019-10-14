import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    def __init__(self, game, image_file):
        super().__init__()
        self.screen = game.screen

        self.watch = pygame.time.Clock()
        self.image = pygame.image.load(image_file)
        self.image.set_colorkey((25, 250, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = self.rect.width
        #self.rect.y = self.rect.height
        self.rect.y = 460

        self.x = float(self.rect.x)

    def draw_block(self):
        self.screen.blit(self.image, self.rect)
