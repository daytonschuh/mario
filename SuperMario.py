import pygame, sys
from pygame.locals import *
from Settings import Settings

class SuperMario:
    def __init__(self):
        pygame.init()
        self.game_settings = Settings()
        self.window_surface = pygame.display.set_mode((self.game_settings.WIDTH,
                                              self.game_settings.HEIGHT), 0, 32)
        pygame.display.set_caption('Super Mario')

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
            self.window_surface.fill((0, 0, 0))
            self.check_events()


if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
