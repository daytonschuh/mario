# a class to handle the background
import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, screen, settings, camera, image_name):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.image = pygame.image.load(image_name)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
#        self.x = float(self.rect.x)
        self.x = (self.settings.WIDTH / 2)

    def update(self):
        self.rect.left = self.x - self.camera.x_pos

    def draw(self):
        self.screen.blit(self.image, self.rect)
