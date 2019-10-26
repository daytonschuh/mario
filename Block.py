from physics import *

b_block = pygame.image.load("Resources/Images/Blocks/b_block.png")
e_block = pygame.image.load("Resources/Images/Blocks/e_block.png")
q_block = pygame.image.load("Resources/Images/Blocks/q_block.png")
i_block = pygame.image.load("Resources/Images/Blocks/i_block.png")


class Block(Sprite):
    def __init__(self, screen, settings, camera, x, y, item=None):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.image = e_block
        self.rect = self.image.get_rect()
        self.rect.left = x * settings.block_size + self.camera.x_pos
        self.x = self.rect.left
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size)
        self.item = item
        self.active = False

    def update(self):
        self.rect.left = self.x - self.camera.x_pos

    def draw_block(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, entity):
        pass


class QuestionBlock(Block):
    def __init__(self, screen, settings, camera, x, y, item="Coin"):
        super().__init__(screen, settings, camera, x, y, item)
        self.active = False
        self.image = q_block
        self.y_pos = self.rect.bottom
        self.delta_y = 0

    def hit(self, entity):
        if self.image is not e_block:
            self.active = True
            add_velocity_up(self.settings.block_recoil, self)

    def update(self):
        super().update()
        if self.active:
            self.rect.bottom += self.delta_y
            apply_gravity(self.settings, self)

            if self.rect.bottom >= self.y_pos:
                self.rect.bottom = self.y_pos
                self.delta_y = 0
                self.active = False
                if self.item is not None:
                    self.image = e_block


class BrickBlock(QuestionBlock):
    def __init__(self, screen, settings, camera, x, y, item=None):
        super().__init__(screen, settings, camera, x, y, item)
        self.image = b_block
        self.y_pos = self.rect.bottom
        self.delta_y = 0

    def hit(self, entity):
        if not self.active:
            if self.item is not None:
                super().hit(entity)
            elif entity.state is 0:
                self.active = True
                add_velocity_up(self.settings.block_recoil, self)
            else:
                pass

    def update(self):
        super().update()


class InvisibleBlock(QuestionBlock):
    def __init__(self, screen, settings, camera, x, y, item="Coin"):
        super().__init__(screen, settings, camera, x, y, item)
        self.image = i_block

    def hit(self, entity):
        super().hit(entity)
        if self.image is not e_block:
            self.image = q_block
