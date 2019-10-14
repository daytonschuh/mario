import pygame.font

class Button:
    def __init__(self, game, msg, xcor, ycor):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (245, 66, 114)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font('Resources/Fonts/commando.ttf', 40)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery
        self.rect.x = xcor
        self.rect.y = ycor

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
