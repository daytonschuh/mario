import pygame.font

class Text:
    def __init__(self, game):
        self.screen = game.screen
        self.font_size = 30
        self.font = pygame.font.SysFont(None, self.font_size)

    def message(self, msg, color, locationx, locationy):
        text = self.font.render(str(msg), True, color)
        self.screen.blit(text, (locationx, locationy))
