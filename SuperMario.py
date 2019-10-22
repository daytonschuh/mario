import pygame, sys
from pygame.locals import *
from Settings import Settings
from Button import Button
from LevelCreator import *

class SuperMario:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.game_active = False
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT), 0, 32)
        pygame.display.set_caption('Super Mario')

        # SET BUTTONS
        self.play_button = Button(self, "PLAY", self.settings.WIDTH/2 - 100, self.settings.HEIGHT/2) # 100 is the button offset (button width/2)
        self.exit_button = Button(self, "EXIT", self.settings.WIDTH/2 - 100, self.settings.HEIGHT/2 + 100)

        # SET LEVEL
        self.level = world_1_1(self.screen, self.settings)

        # SET EVENTS
        self.left, self.right = False, False

        # SET SOUNDS
        #self.lvl1_bg_music = pygame.mixer.Sound('Resources/Sounds/level_1_theme.wav')

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
            self.left = False
            self.right = True
        if event.key == pygame.K_a:
            self.right = False
            self.left = True

    def check_keyup(self, event):
        if event.key == pygame.K_d:
            self.right = False
        elif event.key == pygame.K_a:
            self.left = False

    def do_event(self):
        if self.left is True:
            self.level.mario.move_left()

        elif self.right is True:
            self.level.mario.move_right()

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
        pass
#        self.bg.draw_bg()
#        self.bg_floor.draw_bg()
#        self.lvl1_bg_music.play()

    def draw_screen(self):
        self.level.update()
        self.level.draw_screen()

    def run_game(self):
        self.clock.tick(30)
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))

            self.check_events()

            if self.game_active is False:
                self.play_button.draw_button()
                self.exit_button.draw_button()

            if self.game_active is True:
                self.do_event()
                self.draw_screen()

if __name__ == '__main__':
    game = SuperMario()
    game.run_game()