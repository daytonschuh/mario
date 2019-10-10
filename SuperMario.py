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
            self.key_presses()

    # method to deal with key presses
    def key_presses(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_ESCAPE]: # press ESC to quit
            pygame.quit()
            sys.exit()

    def run_game(self):
        while True:
            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.check_events()
            self.bg.draw_bg()
            self.bg_floor.draw_bg()


if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
