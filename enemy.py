from pygame.sprite import Sprite
from pygame import *


class Enemy(Sprite):
    def __init__(self, screen, settings, camera, spawn_pos):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/jumpman/face_right.png')
        self.rect = self.image.get_rect()
        self.active = False
        self.camera = camera
        self.pos = spawn_pos

    def update(self):
        self.rect.left = self.pos - self.camera.x_pos
        if not self.active:
            if self.rect < self.settings.WIDTH:
                self.active = True
        if self.active:
            self.behavior()
            if self.rect.right < 0:
                self.active = False
                # self.kill()

    def behavior(self):
        pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)
