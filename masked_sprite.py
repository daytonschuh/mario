from pygame.sprite import *
from pygame import *


class MaskedSprite(Sprite):
    def __init__(self, screen, image, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.move(x, y)

    def move(self, x, y):
        self.rect.top = y
        self.rect.left = x

    def draw(self):
        self.screen.blit(self.image, self.rect)
        pygame.display.flip()
