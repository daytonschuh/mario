import pygame, sys
from pygame.locals import *
from Settings import Settings
from Background import Background

class SuperMario:
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.screen = pygame.display.set_mode((self.game_settings.WIDTH, self.game_settings.HEIGHT), 0, 32)
        pygame.display.set_caption('Super Mario')

        self.bg = Background(self, 'Resources/Images/level_1_background.png')
        self.bg_floor = Background(self, 'Resources/Images/level_1_floor.png')

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup(event)

    def check_keydown(self, event):
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

    def run_game(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.check_events()
            self.bg.draw_bg()
            self.bg_floor.draw_bg()
            self.bg.update_bg()
            self.bg_floor.update_bg()

if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
