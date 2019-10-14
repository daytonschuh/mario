import pygame, sys
from pygame.locals import *
from Settings import Settings
from Background import Background
from Button import Button
from Block import Block


"""
Yes i know this shit is messy but I was trying to test out some stuff. I was referencing the old alien code
and all the functions he used to detect collisions but none of that seems to work out here. I tested the code and
referenced pygame documentation but im stuck on something... I tried to test functions using sprite groups or just
singular sprites. I made the test to print out "COLLISION DETECTED" upon detecting a collision but it seems
that it is printing out constantly no matter the position of the block. I have changed the position of the block
to be in the sky and it is still colliding with something. I removed the static background just to eliminate a
variable in the testing. All the stuff commented out are things I have tried so far. Uncomment them and see what
I mean...
"""
class SuperMario:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_active = False
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.WIDTH, self.game_settings.HEIGHT), 0, 32)
        pygame.display.set_caption('Super Mario')

        # SET BUTTONS
        self.play_button = Button(self, "PLAY", self.game_settings.WIDTH/2 - 100, self.game_settings.HEIGHT/2) # 100 is the button offset (button width/2)
        self.exit_button = Button(self, "EXIT", self.game_settings.WIDTH/2 - 100, self.game_settings.HEIGHT/2 + 100)

        # SET SPRITES
        #self.bg = Background(self, 'Resources/Images/level_1_background.png')
        self.bg_floor = Background(self, 'Resources/Images/level_1_floor.png')

        # SET SOUNDS
        self.lvl1_bg_music = pygame.mixer.Sound('Resources/Sounds/level_1_theme.wav')

        # Block testing
        self.block = Block(self, 'Resources/Images/b_block.png')
        self.block_group = pygame.sprite.Group()
        self.bg_floor_group = pygame.sprite.Group()

        self.block_group.add(self.block)
        self.bg_floor_group.add(self.bg_floor)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
                self.check_exit_button(mouse_pos)

    def check_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_d:
            #self.bg.moving_right = True
            self.bg_floor.moving_right = True
        if event.key == pygame.K_a:
            #self.bg.moving_left = True
            self.bg_floor.moving_left = True

    def check_keyup(self, event):
        if event.key == pygame.K_d:
            #self.bg.moving_right = False
            self.bg_floor.moving_right = False
        elif event.key == pygame.K_a:
            #self.bg.moving_left = False
            self.bg_floor.moving_left = False

    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)

    def check_exit_button(self, mouse_pos):
        button_clicked = self.exit_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            pygame.quit()
            sys.exit()

    def initialize(self):
        #self.bg.draw_bg()
        self.bg_floor.draw_bg()
        self.block.draw_block()
        self.lvl1_bg_music.play()

    def run_game(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))

            if self.game_active == False:
                self.play_button.draw_button()
                self.exit_button.draw_button()

            if self.game_active == True:
                self.initialize()

            # update/check methods
            #self.bg.update_bg()
            self.bg_floor.update_bg()
            #self.check_collisions(self.block, self.bg_floor)
            self.check_collisions(self.bg_floor, self.block)
            #self.check_collide()

            self.check_events()

    def spawn_block(self):
        block = Block(self, 'Resources/Images/b_block.png')
        self.block_group.add(block)

    def check_collisions(self, sprite1, sprite2):
        #collision = pygame.sprite.collide_rect(sprite1, sprite2)
        collision = pygame.sprite.collide_rect(sprite2, sprite1)
        if collision:
            print("COLLISION DETECTED")
        #if pygame.sprite.spritecollideany(self.bg_floor, self.block):
        #    print("COLLISION DETECTED")

    def check_collide(self):
        pass
        #if pygame.sprite.spritecollideany(self.block_group, self.bg_floor_group):
        #    print("COLLISION DETECTED")
        #collision = pygame.sprite.groupcollide(self.bg_floor_group, self.block_group, False, False)
        #collision = pygame.sprite.groupcollide(self.block_group, self.bg_floor_group, False, False)
        #if collision:
        #    print("COLLISION DETECTED")


if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
