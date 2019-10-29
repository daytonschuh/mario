from pygame.sprite import Sprite
from pygame import *
from physics import *
from itertools import combinations

goomba_walk_1 = pygame.image.load('Resources/Images/Enemies/Goomba/walk_1.png')
goomba_walk_2 = pygame.image.load('Resources/Images/Enemies/Goomba/walk_2.png')
goomba_death = pygame.image.load('Resources/Images/Enemies/Goomba/death.png')
koopa_walk_left_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_left_1.png')
koopa_walk_left_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_left_2.png')
koopa_wl_cycle = [koopa_walk_left_1, koopa_walk_left_2]
koopa_walk_right_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_right_1.png')
koopa_walk_right_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_right_2.png')
koopa_wr_cycle = [koopa_walk_right_1, koopa_walk_right_2]
koopa_hiding = pygame.image.load('Resources/Images/Enemies/Green_Koopa/transition.png')
koopa_shell = pygame.image.load('Resources/Images/Enemies/Green_Koopa/death.png')

class Enemy(Sprite):
    """ Base class for enemies. """

    def __init__(self, screen, settings, camera, x, y):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.active = False
        self.camera = camera
        self.state = 0
        self.airborne = False
        self.face = 1
        self.delta_x = -self.settings.enemy_walk_speed
        self.delta_y = 0
        self.wait = 100
        self.image = goomba_walk_1
        self.rect = self.image.get_rect()
        self.rect.left = x * settings.block_size + self.camera.x_pos
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size)
        self.x = self.rect.left
        self.buffer = 0
        self.asset_id = self.settings.goomba_id  # goomba is base asset id

    def land(self):
        self.airborne = False
        self.delta_y = 0

    def behavior(self, enemies, floor, blocks, mario):
        pass

    def update(self, enemies, floor, blocks, mario):
        self.rect.left = self.x - self.camera.x_pos
        if not self.active:
            if self.rect.left < self.settings.WIDTH:
                self.active = True
        if self.active:
            self.behavior(enemies, floor, blocks, mario)
            if self.rect.right < 0:
                self.active = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Blooper(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = goomba_walk_1
        self.frames = [goomba_walk_1, goomba_walk_2]
        self.asset_id = 31 # enemy can only be killed by fireball

    def behavior(self):def behavior(self):
        if self.active:
            if self.y - 10 < mario.rect.centery:
                if self.x < mario.rect.centerx:
                    self.x += 10
                else:
                    self.x -= 10
                self.y += 20

            else:
                self.y -= 5"""
    pass


class Bill_Blaster(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = goomba_walk_1
        self.frames = [goomba_walk_1, goomba_walk_2]
        self.asset_id = 0 # treat like a block

    def behavior(self):
        # shoots when mario crosses in the path
        if mario.rect.right == self.y:
            shoot"""
    pass


class Bowser(Enemy):
    """def __init__(self, screen, settings, camera, x, y)
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = bowser_walk
        self.frames = bowser_walk[self.face]
        self.asset_id = 31 or 32

    def behavior(self):
        # choose some slightly random interval to shoot at mario
        # random.randint[] use value as a countdown
        # walk / jump towards mario
        # kill when mario picks up axe and bridge collapse"""
    pass


class Bullet_Bill(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 30

    def behavior(self):
        # just flies straight
        if shot left:
            self.image = facing left
            self.x -= self.velocity
        if shot right:
            self.image = facing right
            self.x += self.velocity
        # can be bounced on"""
    pass


class Buzzy_Beetle(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 30

    def behavior(self):
    # uh?"""
    pass


class Cheep_Cheep(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = goomba_walk_1
        self.frames = [goomba_walk_1, goomba_walk_2]
        self.asset_id = 30

    def behavior(self):
    # gravity affected jumping enemy
    # comes from off screen
    # track x to know when to jump"""
    pass


class Fire_Bar(Enemy):
    """def behavior(self):
    # unsure of behavior
    # pretty sure this just spins in circles"""
    pass


class Goomba(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = goomba_walk_1
        self.frames = [goomba_walk_1, goomba_walk_2]

    def hit(self):
        self.image = goomba_death
        self.state = 1
        self.buffer = 0
        self.asset_id = self.settings.no_collision_id
        print("Enemy Down")

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate walking
                apply_gravity(self.settings, self)
                if self.buffer % 8 == 0:
                    self.image = self.frames[self.buffer // 8]
                self.buffer += 1
                if self.buffer >= 16:
                    self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

                reverse = False
                if collide_check_x(floor, self, direction_x):
                    direction_x = 0
                    reverse = True
                if collide_group_x(blocks, self, direction_x):
                    reverse = True
                if reverse:
                    self.delta_x *= -1

                self.rect.bottom += self.delta_y
                direction_y = get_direction(self.delta_y)
                if collide_check_y(floor, self, direction_y) or collide_group_y(blocks, self, direction_y):
                    self.delta_y = False

            # animate death
            if self.state == 1:
                # death animation
                self.buffer += 1
                if self.buffer > 16:
                    self.kill()
                    self.state = 0

                # death sound
                # settings.points += 100

    # jumping on it kills it


class Hammer_Bro(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 31

    def behavior(self):
        choices = [1000, 2000]
        # randomly throw stuff and jump
        random.randint(choices)
    # throws gravity affected 'bullets'"""
    pass


class Koopa_Paratroopa(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 30

    def behavior(self):
        if 0 == self.state:
            # jumps and moves
            if koopa_paratroopa collides with wall:
                self.velocity *= -1

            if not self.airborne:
                self.image = jump[self.face]
                self.airborne = True
                add_velocity_up(self.settings.jump_speed[6], self)

            if mario.rect.bottom collides with koopa_troopa.rect.top:
                self.state = 1
                self.image = koopa_paratroopa_no_wings

        if 1 == self.state:
            if koopa_paratroopa collides with wall:
                self.velocity *= -1

            if mario.rect.bottom collides with koopa_troopa.rect.top:
                self.state = 2
                self.velocity = 0
                self.image = koopa_paratroopa_in_shell

        if 2 == self.state:
            if mario.rect collides with self.rect.right:
                self.velocity = -12
            else if mario.rect colldes with self.rect.left:
                self.velocity = 12
            if koopa troopa shell hits wall:
                self.velocity *= -1
    # first bounce knocks it to a troopa, second turns to a shell, third kicks it"""
    pass


class Koopa_Troopa(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image_a = koopa_walk_left_1
        self.frames = [koopa_walk_left_1, koopa_walk_left_2]
        self.rect = self.image.get_rect()
        self.rect.left = x * settings.block_size + self.camera.x_pos
        self.rect.bottom = self.settings.HEIGHT - ((0.5 + y) * settings.block_size)
        self.x = self.rect.left

        bottom = self.rect.bottom
        left = self.rect.left

        size_a = self.image.get_size()

        self.image = koopa_walk_left_1
        size_b = self.image.get_size()

        c_x = size_b[0] - size_a[0]
        c_y = size_b[1] - size_a[1]

        self.rect.inflate_ip(c_x, c_y)

        self.rect.bottom = bottom
        self.rect.left = left

    def hit(self):
        self.image = koopa_shell
        self.state = 1
        self.wait = 1000
        self.asset_id = self.settings.no_collision_id
        print("Enemy Down")

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate walking
                apply_gravity(self.settings, self)
                if self.buffer % 8 == 0:
                    self.image = self.frames[self.buffer // 8]
                self.buffer += 1
                if self.buffer >= 16:
                    self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

                reverse = False
                if collide_check_x(floor, self, direction_x):
                    reverse = True
                if collide_group_x(blocks, self, direction_x):
                    reverse = True
                if reverse:
                    self.delta_x *= -1

                self.rect.bottom += self.delta_y
                direction_y = get_direction(self.delta_y)
                if collide_check_y(floor, self, direction_y) or collide_group_y(blocks, self, direction_y):
                    self.delta_y = False

            # animate death
            if self.state == 1:
                # death animation
                self.wait -= 1
                if self.wait == 0:
                    self.asset_id = self.settings.goomba_id
                    self.state = 0


class Lava_Bubble(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
           super().__init__(screen, settings, camera, x, y)
           self.active = False
           self.image = goomba_walk_1
           self.frames = [goomba_walk_1, goomba_walk_2]
           self.asset_id = 32

    def behavior(self):
        if not self.airborne:
            self.image = jump[self.face]
            self.airborne = True
            add_velocity_up(self.settings.jump_speed[6], self)

        if self.airborne:
            self.image = lava_bubble_falling
            self.y += 10
            if 0 == self.y:
                self.airborne = False
    # perhaps just like Piranha plant up and down with delay"""
    pass


class Piranha_Plant(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 31

    def behavior(self):
        # moving up
        if 0 == self.state:
            self.y -= 10
            if self.y > self.pos[1]+30:
                self.state = 1
        # delay
        if 1 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 2
        # moving down
        if 2 == self.state:
            self.y += 10
            if self.y == self.pos[1]:
                self.wait = 100
                self.state = 3
        # second delay
        if 3 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 0
    # up and down delay
    # behind pipe, in front of backdrop"""
    pass


class Spiny_Egg(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 32

    def behavior(self):
    # drops until it hits the floor
        self.y -= self.velocity

        if not self.airborne:
            self.image = jump[self.face]
            self.airborne = True
            add_velocity_up(self.settings.jump_speed[6], self)
    # short delay before becoming spiny
    def change_to_spiny(self):"""
    pass


class Spiny(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 31

    def behavior(self):
        if mario.x > self.x:
            self.image = facing right
            self.x += self.velocity

        if mario.x < self.x:
            self.image = facing left
            self.x += self.velocity

        if spiny collides with wall:
            self.velocity *= -1
    # cannot be jumped on
        if mario collides with self:
            mario.kill()"""
    pass


class Lakitu(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 31

    def behavior(self):
        self.velocity = 8
        if mario.rect.centerx > self.x:
            self.x += self.velocity
    # flies above and follows mario
    # drops spiny eggs  that turn into spiny enemy"""
    pass
