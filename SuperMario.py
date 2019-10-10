import pygame, sys
from pygame.locals import *
from Settings import Settings
from Background import Background
from Button import Button

class SuperMario:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.game_active = False
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.WIDTH, self.game_settings.HEIGHT), 0, 32)
        pygame.display.set_caption('Super Mario')

        # SET BUTTONS
        self.play_button = Button(self, "PLAY", self.game_settings.WIDTH/2 - 100, self.game_settings.HEIGHT/2)

        # SET SPRITES
        self.bg = Background(self, 'Resources/Images/level_1_background.png')
        self.bg_floor = Background(self, 'Resources/Images/level_1_floor.png')

        # SET SOUNDS
        self.lvl1_bg_music = pygame.mixer.Sound('Resources/Sounds/level_1_theme.wav')

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

    def check_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == pygame.K_d:
            self.bg.moving_right = True
            self.bg_floor.moving_right = True
        if event.key == pygame.K_a:
            self.bg.moving_left = True
            self.bg_floor.moving_left = True

    def check_keyup(self, event):
        if event.key == pygame.K_d:
            self.bg.moving_right = False
            self.bg_floor.moving_right = False
        elif event.key == pygame.K_a:
            self.bg.moving_left = False
            self.bg_floor.moving_left = False

    def check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active = True
            pygame.mouse.set_visible(False)

    def initialize(self):
        self.bg.draw_bg()
        self.bg_floor.draw_bg()
        self.lvl1_bg_music.play()

    def run_game(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.play_button.draw_button()

            if self.game_active == True:
                self.initialize()

            # update/check methods
            self.bg.update_bg()
            self.bg_floor.update_bg()

            self.check_events()

if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
