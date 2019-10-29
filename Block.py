from physics import *

b_block = pygame.image.load("Resources/Images/Blocks/b_block.png")
e_block = pygame.image.load("Resources/Images/Blocks/e_block.png")
q_block = pygame.image.load("Resources/Images/Blocks/q_block.png")
i_block = pygame.image.load("Resources/Images/Blocks/i_block.png")
d_block = pygame.image.load("Resources/Images/Blocks/d_block.png")
ub_block = pygame.image.load("Resources/Images/Blocks/u_block.png")
ud_block = pygame.image.load("Resources/Images/Blocks/ud_block.png")
flag_pole = pygame.image.load("Resources/Images/Blocks/flag_pole.png")
flag = pygame.image.load("Resources/Images/Blocks/flag.png")


class Block(Sprite):
    def __init__(self, screen, settings, camera, x, y, level, item=None):
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
        self.asset_id = settings.static_id
        self.level = level
        self.origin = [x, y]

    def update(self):
        self.rect.left = self.x - self.camera.x_pos

    def draw_block(self):
        self.screen.blit(self.image, self.rect)

    def hit(self, entity):
        pass


class QuestionBlock(Block):
    def __init__(self, screen, settings, camera, x, y, level, item="Coin"):
        super().__init__(screen, settings, camera, x, y, level, item)
        self.active = False
        self.image = q_block
        self.y_pos = self.rect.bottom
        self.delta_y = 0
        self.asset_id = self.settings.block_id

    def hit(self, entity):
        if self.asset_id is not self.settings.static_id and entity.asset_id is 99:
            self.active = True
            add_velocity_up(self.settings.block_recoil, self)
            if self.item is not None:
                self.level.place_item(self.item, self.origin[0], self.origin[1], True, self.x)

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
                    self.asset_id = self.settings.static_id


class BrickBlock(QuestionBlock):
    def __init__(self, screen, settings, camera, x, y, level, item=None):
        super().__init__(screen, settings, camera, x, y, level, item)
        self.image = b_block
        self.destroy = False
        self.d_timer = 20

    def hit(self, entity):
        if not self.active:
            if self.item is not None:
                super().hit(entity)
            elif entity.stage is 0 and self.delta_y is 0:
                self.active = True
                add_velocity_up(self.settings.block_recoil, self)
            else:
                self.destroy = True
                self.image = d_block

    def update(self):
        super().update()
        if self.destroy:
            self.d_timer -= 1
            if self.d_timer < 18:
                self.asset_id = self.settings.no_collision_id
            if self.d_timer is 0:
                self.kill()


class InvisibleBlock(QuestionBlock):
    def __init__(self, screen, settings, camera, x, y, level, item="Coin"):
        super().__init__(screen, settings, camera, x, y, level, item)
        self.image = i_block
        self.asset_id = settings.invisible_block_id

    def hit(self, entity):
        super().hit(entity)
        if self.asset_id is self.settings.invisible_block_id:
            self.image = q_block
            self.asset_id = self.settings.block_id


class UndergroundBrickBlock(BrickBlock):
    def __init__(self, screen, settings, camera, x, y, level, item=None):
        super().__init__(screen, settings, camera, x, y, level, item)
        self.image = ub_block
        self.destroy = False
        self.d_timer = 20

    def hit(self, entity):
        if not self.active:
            if self.item is not None:
                super().hit(entity)
            elif entity.stage is 0 and self.delta_y is 0:
                self.active = True
                add_velocity_up(self.settings.block_recoil, self)
            else:
                self.destroy = True
                self.image = ud_block


class FlagPole(Sprite):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.image = flag_pole
        self.rect = self.image.get_rect()
        self.rect.left = x * settings.block_size + self.camera.x_pos + 12
        self.x = self.rect.left
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size)
        self.flag_image = flag
        self.flag_rect = self.flag_image.get_rect()
        self.flag_rect.right = self.rect.centerx
        self.flag_rect.top = self.rect.top + 24
        self.flag_x = self.flag_rect.left
        self.asset_id = self.settings.flag_id
        self.grabbed = False

    def grab(self):
        self.grabbed = True

    def update(self):
        self.rect.left = self.x - self.camera.x_pos
        self.flag_rect.left = self.flag_x - self.camera.x_pos
        if self.grabbed:
            if self.flag_rect.bottom < self.rect.bottom:
                self.flag_rect.y += 3
            else:
                self.grabbed = False
                self.asset_id = self.settings.auto_id

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.flag_image, self.flag_rect)