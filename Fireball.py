from pygame.sprite import *
from physics import *
from Timer import Timer

fire_ball_a = pygame.image.load("Resources/Images/Items/fire_ball.png")
fire_ball_b = pygame.image.load("Resources/Images/Items/fire_ball_b.png")
fire_ball = [fire_ball_a, fire_ball_b]


class Fireball(Sprite):
    def __init__(self, screen, settings, camera, x, y, direction):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.camera = camera
        self.image = fire_ball[0]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.bottom = y
        self.x = self.rect.x
        self.asset_id = self.settings.fire_id
        self.timer = Timer(10)
        self.image_index = 1
        if direction == 0:
            self.direction = -1
        else:
            self.direction = 1
        self.delta_x = 9
        self.delta_y = self.settings.gravity_max/4

    def land(self):
        self.delta_y = 0
        add_velocity_up(10, self)

    def update(self, floor, enemies, blocks):
        self.timer.tick()
        if self.timer.check():
            self.image = fire_ball[self.image_index]
            self.image_index += 1
            if self.image_index > 1:
                self.image_index = 0
        self.x += self.delta_x * self.direction
        self.rect.left = self.x - self.camera.x_pos

        for enemy in enemies:
            if collide_rect(self, enemy):
                enemy.fire_hit()
                #enemy.kill()
                self.kill()

        if collide_group_x(blocks, self, self.direction):
            self.kill()
        if collide_check_x(floor, self, self.direction):
            self.kill()

        apply_gravity(self.settings, self)
        self.rect.bottom += self.delta_y
        direction_y = get_direction(self.delta_y)

        if collide_group_y(blocks, self, direction_y):
            direction_y = 0
        collide_check_y(floor, self, direction_y)

        if self.rect.right < 0 or self.rect.left > 1200:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)