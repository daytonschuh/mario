# a class to handle the background
import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, game, image_name):
        super().__init__()
        self.screen = game.screen
        self.settings = game.game_settings
        self.screen_rect = game.screen.get_rect()
        self.background = pygame.image.load(image_name)

        self.rect = self.background.get_rect()

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update_bg(self):
        if self.moving_right:
            self.x -= self.settings.bg_speed
        if self.moving_left:
            self.x += self.settings.bg_speed

        self.rect.x = self.x

    def draw_bg(self):
        self.screen.blit(self.background, self.rect)
