import pygame.font

class Text:
    def __init__(self, game):
        self.screen = game.screen
        self.font_size = 15
        self.font = pygame.font.Font('Resources/Fonts/prstartk.ttf', self.font_size)

    def message(self, msg, color, locationx, locationy):
        text = self.font.render(str(msg), True, color)
        self.screen.blit(text, (locationx, locationy))
