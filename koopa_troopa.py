from enemy import Enemy
from pygame.sprite import Sprite
from pygame import *
from camera import Camera


class KoopaTroopa(Enemy):
    def __init__(self, settings, camera, spawn_pos):
        super().__init__(settings, camera, spawn_pos)
        self.image = pygame.image.load('images/jumpman/face_left.png')
        self.rect = self.image.get_rect()
        self.active = False

    def update(self):
        self.rect.left = self.pos - self.camera.x_pos
        if not self.active:
            if self.rect < self.settings.WIDTH:
                self.active = True
        if self.active:
            self.behavior()
            if self.rect.right < 0:
                self.kill()

    def behavior(self):
        self.pos += 10
