from pygame import *
from physics import *

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
blooper_1 = pygame.image.load('Resources/Images/Enemies/Blooper/blooper_1.png')
blooper_2 = pygame.image.load('Resources/Images/Enemies/Blooper/blooper_2.png')
bowser_left_1 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_left_1.png')
bowser_left_2 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_left_2.png')
bowser_right_1 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_right_1.png')
bowser_right_2 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_right_2.png')
bowser_walk = [[bowser_left_1, bowser_left_2], [bowser_right_1,  bowser_right_2]]
bowser_shoot_left_1 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_shoot_left_1.png')
bowser_shoot_left_2 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_shoot_left_2.png')
bowser_shoot_right_1 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_shoot_right_1.png')
bowser_shoot_right_2 = pygame.image.load('Resources/Images/Enemies/Bowser/bowser_shoot_right_2.png')
bowser_shoot = [[bowser_shoot_left_1, bowser_shoot_left_2], [bowser_shoot_right_1, bowser_shoot_right_2]]
fireball_left_1 = pygame.image.load('Resources/Images/Enemies/Bowser/fireball_left_1.png')
fireball_left_2 = pygame.image.load('Resources/Images/Enemies/Bowser/fireball_left_3.png')
fireball_right_1 = pygame.image.load('Resources/Images/Enemies/Bowser/fireball_right_1.png')
fireball_right_2 = pygame.image.load('Resources/Images/Enemies/Bowser/fireball_right_3.png')
cc_left_1 = pygame.image.load('Resources/Images/Enemies/Cheep_Cheep/jump_left_1.png')
cc_left_2 = pygame.image.load('Resources/Images/Enemies/Cheep_Cheep/jump_left_2.png')
cc_right_1 = pygame.image.load('Resources/Images/Enemies/Cheep_Cheep/jump_right_1.png')
cc_right_2 = pygame.image.load('Resources/Images/Enemies/Cheep_Cheep/jump_right_2.png')
cc_move = [[cc_left_1, cc_left_2], [cc_right_1, cc_right_2]]
fire_bar = pygame.image.load('Resources/Images/Enemies/Fire_Bar/fire_bar.png')
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
stomp = pygame.mixer.Sound("Resources/Sounds/smb_stomp.wav")
kick = pygame.mixer.Sound("Resources/Sounds/smb_kick.wav")


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
        self.asset_id = self.settings.ground_enemy  # goomba is base asset id
        self.dead = False

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

        return self.rect

    def fire_hit(self):
        pass

    def bounce(self):
        add_velocity_up(15, self)


class Blooper(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.just_jumped = False
        self.image = blooper_1
        self.frames = [blooper_1, blooper_2]
        self.asset_id = self.settings.no_jump_phase_enemy  # enemy can only be killed by fireball
        self.rect = self.adjust_hitbox(settings, x, y)
        self.y = self.rect.bottom
        self.delta_y = 1
        self.delta_x = -5

    def hit(self):
        pass

    def fire_hit(self):
        self.image = pygame.transform.flip(goomba_walk_1, True, False)
        self.wait = 1000
        # animate death sequence
        self.state = 1
        self.bounce()
        pygame.mixer.Sound.play(kick)
        if self.wait > 0:
            self.wait -= 1
            self.rect.bottom += 1
        else:
            print("Enemy Down")

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            apply_gravity(self.settings, self, True)

            self.wait -= 1
            if self.wait <= 0:
                self.just_jumped = False

            if self.delta_y < 0:
                self.image = blooper_1

                if self.rect.left < mario.rect.left - 6:
                    self.rect.left -= self.delta_x
                    self.x -= self.delta_x
                elif self.rect.right > mario.rect.right + 6:
                    self.rect.left += self.delta_x
                    self.x += self.delta_x

            self.rect.bottom += self.delta_y
            self.y += self.delta_y

            if self.delta_y > 0:
                self.image = blooper_2

            if self.delta_y > 0 and self.rect.bottom >= mario.rect.top-10 and not self.just_jumped:
                self.delta_y = 0
                add_velocity_up(8, self)
                self.just_jumped = True
                self.wait = 100

            if self.rect.top < 48:
                self.rect.top = 48


class Bowser(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = bowser_left_1
        self.face = 0
        self.frames = bowser_walk[self.face][self.buffer]
        self.asset_id = self.settings.tough_enemy
        self.rect = self.adjust_hitbox(settings, x, y)
        self.hp = 10

    def hit(self):
        pass

    def fire_hit(self):
        self.hp -= 1
        if self.hp == 0:
            self.image = pygame.transform.flip(bowser_walk[self.face][self.buffer], True, False)
            self.state = 1
            self.active = False
            pygame.mixer.Sound.play(kick)
            self.asset_id = self.settings.no_collision_id

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate walking
                apply_gravity(self.settings, self)
                if self.buffer % 8 == 0:
                    self.image = bowser_walk[self.face][self.buffer // 32]
                self.buffer += 1
                if self.buffer >= 64:
                    self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

            # animate death
            if self.state == 1:
                # death animation
                self.buffer += 1
                if self.buffer > 16:
                    self.kill()
                    self.state = 0

                # death sound
                # settings.points += 100
        # choose some slightly random interval to shoot at mario
        # random.randint[] use value as a countdown
        # walk / jump towards mario
        # kill when mario picks up axe and bridge collapse


class CheepCheep(Enemy):
    def __init__(self, screen, settings, camera, x, y, swim=False):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = cc_left_1
        self.face = 0
        self.frames = cc_move[self.face][self.buffer]
        self.start_y = y
        self.start_x = x
        if swim:
            self.face = 0
            self.delta_x = -1
            self.asset_id = self.settings.no_jump_phase_enemy
        else:
            self.face = 1
            self.delta_x = 2
            self.asset_id = self.settings.fish_enemy
        self.rect = self.adjust_hitbox(settings, x, y)
        self.swim = swim

    def hit(self):
        self.state = 1
        self.delta_y = 0
        pygame.mixer.Sound.play(stomp)
        self.buffer = 0
        self.asset_id = self.settings.no_collision_id
        print("Enemy Down")
        pass

    def fire_hit(self):
        self.asset_id = self.settings.no_collision_id
        self.image = pygame.transform.flip(cc_left_1, True, False)
        self.wait = 1000
        # animate death sequence
        self.bounce()
        pygame.mixer.Sound.play(kick)
        if self.wait > 0:
            self.wait -= 1
            self.rect.bottom += 1
        else:
            print("Enemy Down")

    def bounce(self):
        self.delta_y = 0
        self.rect.top = self.settings.HEIGHT
        add_velocity_up(self.start_y*1.5 + 14, self)
        self.rect.left = self.start_x * self.settings.block_size + self.camera.x_pos
        self.x = self.rect.left

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            if self.state == 0:
                # animate walking
                if not self.swim:
                    apply_gravity(self.settings, self)
                    if self.rect.top > self.settings.HEIGHT:
                        self.bounce()
                if self.buffer % 8 == 0:
                    self.image = cc_move[self.face][self.buffer // 32]
                self.buffer += 1
                if self.buffer >= 64:
                    self.buffer = 0

                # check collisions
                self.rect.left += self.delta_x
                self.x += self.delta_x
                direction_x = get_direction(self.delta_x)

                self.rect.bottom += self.delta_y

            # animate death
            if self.state == 1:
                # death animation
                apply_gravity(self.settings, self)
                self.rect.top += self.delta_y
                self.buffer += 1
                if self.buffer > 16:
                    self.kill()
                    self.state = 0

                # death sound
                # settings.points += 100


class FireBar(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.original_image = fire_bar
        self.image = self.original_image
        self.angle = 0
        self.rect = self.adjust_hitbox(settings, x, y)

    def rotate(self):
        """Rotate the image of the sprite around its center."""
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(left=self.rect.left)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle += 1 % 360

    def hit(self):
        pass

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            self.rotate()


class Goomba(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = goomba_walk_1
        self.frames = [goomba_walk_1, goomba_walk_2]
        self.asset_id = self.settings.ground_enemy

    def hit(self):
        self.image = goomba_death
        self.state = 1
        pygame.mixer.Sound.play(stomp)
        self.buffer = 0
        self.asset_id = self.settings.no_collision_id
        print("Enemy Down")

    def fire_hit(self):
        self.state = 2
        self.active = False
        pygame.mixer.Sound.play(kick)
        self.asset_id = self.settings.no_collision_id

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            apply_gravity(self.settings, self)
            if self.state == 0:
                # animate walking
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

            if self.state == 2:
                self.image = pygame.transform.flip(goomba_walk_1, False, True)
                self.rect.bottom += self.delta_y

                # death sound
                # settings.points += 100


class KoopaParatroopa(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.asset_id = self.settings.ground_enemy
        self.face = 0
        self.image_a = koopa_jump_left_1
        self.frames = [koopa_jump_left_1, koopa_jump_left_2], [koopa_jump_right_1, koopa_jump_right_2]
        self.frames2 = [koopa_walk_left_1, koopa_walk_left_2], [koopa_walk_right_1, koopa_walk_right_2]
        self.rect = self.image.get_rect()
        self.rect = self.adjust_hitbox(settings, x, y)

    def hit(self):
        self.image = koopa_shell
        self.state = 1
        self.wait = 1000
        print("Enemy Down")

    def fire_hit(self):
        self.image = pygame.transform.flip(koopa_shell, True, False)
        self.wait = 1000
        # animate death sequence
        self.bounce()
        if self.wait > 0:
            self.wait -= 1
            self.rect.bottom += 10
        else:
            self.kill()
        print("Enemy Down")

    def land(self):
        super().land()
        self.bounce()

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


class KoopaTroopa(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.face = 0
        self.image_a = koopa_walk_left_1
        self.frames = [koopa_walk_left_1, koopa_walk_left_2], [koopa_walk_right_1, koopa_walk_right_2]
        self.rect = self.image.get_rect()
        self.rect = self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.ground_enemy

    def fire_hit(self):
        self.image = pygame.transform.flip(koopa_shell, False, True)
        self.active = False
        self.state = 3
        pygame.mixer.Sound.play(kick)
        self.asset_id = self.settings.no_collision_id
        print("Enemy Down")

    def hit(self):
        self.image = koopa_shell
        self.state = 1
        self.wait = 1000
        if self.asset_id == self.settings.ground_enemy:
            self.asset_id = self.settings.slide_enemy
        elif self.asset_id == self.settings.slide_enemy:
            self.kick()
        print("Enemy Down")

    def kick(self):
        self.state = 2
        self.wait = 10
        pygame.mixer.Sound.play(kick)
        # Hit is used when:
        # Mario jumps on a moving shell
        # Mario jumps on a non-shell koopa(paratroopa)
        # Kick is used when:
        # Mario touches a shell(and shell only) when its delta_x = 0
        # Direction parameter is so mario kicks it away from him, +1 is to the right, -1 if to the left
        # Check asset_id of 33 in Physics for more shell information

        # When mario kicks the shell it is possible he will get hit immediately
        # Potential Solutions
        # give it a asset_id of 33 for the first few frames of motion
        # To minimize the above risk the shell movespeed must be >= Mario's max run speed (6)

    def behavior(self, enemies, floor, blocks, mario):
        if self.active:
            apply_gravity(self.settings, self)
            if self.state == 0:
                # animate walking
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
                        and self.settings.ground_enemy == self.asset_id:
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
                    self.asset_id = self.settings.slide_enemy
                    self.state = 0

            # Koopa shell has been kicked
            if self.state == 2:
                apply_gravity(self.settings, self)
                if self.wait > 0:
                    self.wait -= 1
                    self.asset_id = self.settings.no_collision_id

                else:
                    self.asset_id = self.settings.slide_enemy
                    self.rect.left += 5
                    self.x += 5
                    direction_x = get_direction(self.delta_x)
                    if (collide_check_x(floor, self, direction_x) or collide_group_x(blocks, self, direction_x))\
                            and self.settings.slide_enemy == self.asset_id:
                        self.delta_x *= -1

            # Koopa is dying
            if self.state == 3:
                self.image = pygame.transform.flip(koopa_shell, False, True)
                self.rect.bottom += self.delta_y

        else:
            apply_gravity(self.settings, self)
            self.kill()


class LavaBubble(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = fireball_up_1
        self.frames = [fireball_up_1, fireball_up_2, fireball_up_3], [fireball_down_1, fireball_down_2, fireball_down_3]
        self.face = 0
        self.rect = self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.pure_phase_enemy

    def hit(self):
        pass

    def behavior(self, enemies, floor, blocks, mario):
        # animate
        if self.buffer % 8 == 0:
            self.image = self.frames[self.face][self.buffer // 16]
        self.buffer += 1
        if self.buffer >= 32:
            self.buffer = 0

        # moving up
        if 0 == self.state:
            self.rect.bottom -= 7
            self.face = 0
            if self.rect.bottom < self.settings.HEIGHT - 300:
                self.wait = 20
                self.state = 1
        # delay
        if 1 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 2
        # moving down
        if 2 == self.state:
            self.rect.bottom += 7
            self.face = 1
            if self.rect.bottom > self.settings.HEIGHT + 300:
                self.wait = 1
                self.state = 3
        # second delay
        if 3 == self.state:
            self.wait -= 1
            if 0 == self.wait:
                self.state = 0


class PiranhaPlant(Enemy):
    def __init__(self, screen, settings, camera, x, y):
        super().__init__(screen, settings, camera, x, y)
        self.active = False
        self.image = piranha_plant_open
        self.frames = [piranha_plant_open, piranha_plant_close]
        self.rect = self.image.get_rect()
        self.rect = self.adjust_hitbox(settings, x, y)
        self.asset_id = self.settings.no_jump_phase_enemy

    def fire_hit(self):
        self.image = pygame.transform.flip(koopa_shell, False, True)
        self.active = False
        self.state = 4
        pygame.mixer.Sound.play(kick)
        self.asset_id = self.settings.no_collision_id

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

        if 4 == self.state:
            self.image = pygame.transform.flip(piranha_plant_open, False, True)
            self.delta_y = 6
            self.rect.bottom += self.delta_y


""" ANYTHING BEYOND THIS POINT DOES NOT NEED TO BE IMPLEMENTED BEFORE THE DEADLINE """


class BulletBill(Enemy):
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


class BillBlaster(Enemy):
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


class BuzzyBeetle(Enemy):
    """def __init__(self, screen, settings, camera, x, y):
            super().__init__(screen, settings, camera, x, y)
            self.active = False
            self.image = goomba_walk_1
            self.frames = [goomba_walk_1, goomba_walk_2]
            self.asset_id = 30

    def behavior(self):
    # uh?"""
    pass


class HammerBro(Enemy):
    """def behavior(self, enemies, floor, blocks, mario):
        choices = [1000, 2000]
        # randomly throw stuff and jump
        random.randint(choices)
    # throws gravity affected 'bullets'
    pass"""


""" TODO: Maybe make a class for hammers thrown by the hammer bro """


class SpinyEgg(Enemy):
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
