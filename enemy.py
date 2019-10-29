from pygame.sprite import Sprite
from pygame import *
from physics import *
from itertools import combinations

goomba_walk_1 = pygame.image.load('Resources/Images/Enemies/Goomba/walk_1.png')
goomba_walk_2 = pygame.image.load('Resources/Images/Enemies/Goomba/walk_2.png')
goomba_death = pygame.image.load('Resources/Images/Enemies/Goomba/death.png')
koopa_walk_left_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_left_1.png')
koopa_walk_left_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_left_2.png')
koopa_walk_right_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_right_1.png')
koopa_walk_right_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/walk_right_2.png')
koopa_hiding = pygame.image.load('Resources/Images/Enemies/Green_Koopa/transition.png')
koopa_shell = pygame.image.load('Resources/Images/Enemies/Green_Koopa/death.png')
koopa_jump_left_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/jump_left_1.png')
koopa_jump_left_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/jump_left_2.png')
koopa_jump_right_1 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/jump_right_1.png')
koopa_jump_right_2 = pygame.image.load('Resources/Images/Enemies/Green_Koopa/jump_right_2.png')
piranha_plant_open = pygame.image.load('Resources/Images/Enemies/Piranha_Plant/nom_1.png')
piranha_plant_close = pygame.image.load('Resources/Images/Enemies/Piranha_Plant/nom_2.png')
fireball_up_1 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/up_1.png')
fireball_up_2 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/up_2.png')
fireball_up_3 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/up_3.png')
fireball_down_1 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/down_1.png')
fireball_down_2 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/down_2.png')
fireball_down_3 = pygame.image.load('Resources/Images/Enemies/Lava_Bubble/down_3.png')


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

    def adjust_hitbox(self, settings, x, y):
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


""" TODO: Maybe make a class for hammers thrown by the hammer bro """


class Koopa_Paratroopa(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.asset_id = self.settings.koopa_paratroopa_id
        self.face = 0
        self.image_a = koopa_jump_left_1
        self.frames = [koopa_jump_left_1, koopa_jump_left_2], [koopa_jump_right_1, koopa_jump_right_2]
        self.frames2 = [koopa_walk_left_1, koopa_walk_left_2], [koopa_walk_right_1, koopa_walk_right_2]
        self.rect = self.image.get_rect()
        self.adjust_hitbox(settings, x, y)

    def hit(self):
        self.image = koopa_shell
        self.state = 1
        self.wait = 1000
        if self.settings.koopa_paratroopa_id == self.asset_id:
            self.asset_id = self.settings.koopa_troopa_id
        if self.settings.koopa_troopa_id == self.asset_id:
            self.asset_id = self.settings.koopa_shell_id
        if self.settings.koopa_shell_id == self.asset_id:
            # depending on collision, hit it that way
            pass
        print("Enemy Down")

    def land(self):
        super().land()
        self.bounce()

    def bounce(self):
        add_velocity_up(15, self)

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate movement
                apply_gravity(self.settings, self)
                if self.asset_id == self.settings.koopa_paratroopa_id:
                    if self.buffer % 8 == 0:
                        self.image = self.frames[self.face][self.buffer // 16]
                    self.buffer += 1
                    if self.buffer >= 32:
                        self.buffer = 0

                else:
                    if self.buffer % 8 == 0:
                        self.image = self.frames2[self.face][self.buffer // 16]
                    self.buffer += 1
                    if self.buffer >= 32:
                        self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

                if direction_x > 0:
                    self.face = 1
                elif direction_x < 0:
                    self.face = 0

                # Turns the koopa around if he hits an enemy or wall
                if (collide_check_x(floor, self, direction_x) or collide_group_x(blocks, self, direction_x)) \
                        and self.settings.koopa_troopa_id == self.asset_id:
                    self.delta_x *= -1

                self.rect.bottom += self.delta_y
                direction_y = get_direction(self.delta_y)
                if collide_check_y(floor, self, direction_y) or collide_group_y(blocks, self, direction_y):
                    self.delta_y = 0
                    if direction_y > 0:
                        self.land()

            # Koopa currently in his shell
            if self.state == 1:
                # Wait until it's safe to come out!
                self.wait -= 1
                if self.wait == 0:
                    self.asset_id = self.settings.koopa_troopa_id
                    self.state = 0


class Koopa_Troopa(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.face = 0
        self.image_a = koopa_walk_left_1
        self.frames = [koopa_walk_left_1, koopa_walk_left_2], [koopa_walk_right_1, koopa_walk_right_2]
        self.rect = self.image.get_rect()
        self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.koopa_troopa_id

    def hit(self):
        self.image = koopa_shell
        self.state = 1
        self.wait = 1000
        self.asset_id = self.settings.koopa_shell_id
        print("Enemy Down")

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate walking
                apply_gravity(self.settings, self)
                if self.buffer % 8 == 0:
                    self.image = self.frames[self.face][self.buffer // 8]
                self.buffer += 1
                if self.buffer >= 16:
                    self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

                if direction_x > 0:
                    self.face = 1
                elif direction_x < 0:
                    self.face = 0

                # Turns the koopa around if he hits an enemy or wall
                if (collide_check_x(floor, self, direction_x) or collide_group_x(blocks, self, direction_x))\
                        and self.settings.koopa_troopa_id == self.asset_id:
                    self.delta_x *= -1

                self.rect.bottom += self.delta_y
                direction_y = get_direction(self.delta_y)
                if collide_check_y(floor, self, direction_y) or collide_group_y(blocks, self, direction_y):
                    self.delta_y = False

                # Koopa currently in his shell
                if self.state == 1:
                    # Wait until it's safe to come out!
                    self.wait -= 1
                    if self.wait == 0:
                        self.asset_id = self.settings.koopa_troopa_id
                        self.state = 0


class Lava_Bubble(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = fireball_up_1
        self.frames = [fireball_up_1, fireball_up_2, fireball_up_3],[fireball_down_1, fireball_down_2, fireball_down_3]
        self.face = 0
        self.rect = self.image.get_rect()
        self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.lava_bubble_id

    def hit(self):
        # can't be killed
        pass

    def behavior(self, enemies, floor, blocks, mario):
        """ TODO: change fireball direction based on up / down """
        ###########################################################
        direction_y = get_direction(self.delta_y)
        if direction_y > 0:
            self.face = 1
        elif direction_y < 0:
            self.face = 0
        ###########################################################

        # animate
        if self.buffer % 8 == 0:
            self.image = self.frames[self.face][self.buffer // 16]
        self.buffer += 1
        if self.buffer >= 32:
            self.buffer = 0

        # moving up
        if 0 == self.state:
            self.rect.bottom -= 1
            if self.rect.bottom < self.settings.HEIGHT - 100:
                self.wait = 20
                self.state = 1
        # delay
        if 1 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 2
        # moving down
        if 2 == self.state:
            self.rect.bottom += 1
            if self.rect.bottom > self.settings.HEIGHT - 50:
                self.wait = 250
                self.state = 3
        # second delay
        if 3 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 0


class Piranha_Plant(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = piranha_plant_open
        self.frames = [piranha_plant_open, piranha_plant_close]
        self.rect = self.image.get_rect()
        self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.piranha_plant_id

    def hit(self):
        # can be killed with fireball
        pass

    def behavior(self, enemies, floor, blocks, mario):
        # animate
        if self.buffer % 8 == 0:
            self.image = self.frames[self.buffer // 16]
        self.buffer += 1
        if self.buffer >= 32:
            self.buffer = 0

        # moving up
        if 0 == self.state:
            self.rect.bottom -= 1
            if self.rect.bottom < self.settings.HEIGHT - 100:
                self.wait = 200
                self.state = 1
        # delay
        if 1 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 2
        # moving down
        if 2 == self.state:
            self.rect.bottom += 1
            if self.rect.bottom > self.settings.HEIGHT - 50:
                self.wait = 350
                self.state = 3
        # second delay
        if 3 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 0
    # up and down delay
    # behind pipe, in front of backdrop?
    pass



""" ANYTHING BEYOND THIS POINT DOES NOT NEED TO BE IMPLEMENTED BEFORE THE DEADLINE """

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
