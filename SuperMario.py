import pygame, sys
from pygame.locals import *
from Text import *
from Scoring import *
from Settings import *
from Button import *
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

        # SET GAME HEADER
        self.game_score = 0
        self.game_time = 0
        self.game_coin = 0
        # SET LEVEL
        self.level = world_1_2_sub_sub(self.screen, self.settings)
        self.level_id = self.level.level_id

        # SET EVENTS
        self.left, self.right, self.space, self.shift, self.down, self.fire = [False] * 6

        # SET SOUNDS
        #self.lvl1_bg_music = pygame.mixer.Sound('Resources/Sounds/level_1_theme.wav')

    def check_level(self):
        if self.level_id == self.level.level_id:
            return
        else:
            self.level.scores.set_stats(self.game_score, self.game_time)
            old_id = self.level_id
            start_pos = None
            if self.level.level_id is not None:
                self.level_id = self.level.level_id

            if self.level_id == self.settings.W_1_1:
                if old_id == self.settings.W_1_1_sub:
                    start_pos = [163.5, 2]
                self.level = world_1_1(self.screen, self.settings, start_pos)
                self.level.scores.scores = self.game_score
                self.level.scores.timer = self.game_time
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_1_1_sub:
                self.level = world_1_1_sub(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.timer = self.game_time
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_1_2:
                self.level = world_1_2(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_1_2_sub:
                if old_id == self.settings.W_1_2_sub_sub:
                    start_pos = [115.5, 3]
                self.level = world_1_2_sub(self.screen, self.settings, start_pos)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_1_2_sub_sub:
                self.level = world_1_2_sub_sub(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin
                self.level.scores.timer = self.game_time
            elif self.level_id == self.settings.W_1_2_exit:
                self.level = world_1_2_exit(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin
                self.level.scores.timer = self.game_time

            elif self.level_id == self.settings.W_1_3:
                self.level = world_1_3(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_1_4:
                self.level = world_1_4(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_1:
                if old_id == self.settings.W_2_1_sub:
                    start_pos = [115.5, 3]
                self.level = world_2_1(self.screen, self.settings, start_pos)
                self.level.scores.scores = self.game_score
                self.level.scores.timer = self.game_time
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_1_sub:
                self.level = world_2_1_sub(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.timer = self.game_time
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_2:
                self.level = world_2_2(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_2_sub:
                self.level = world_2_2_water(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.timer = self.game_time
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_2_exit:
                self.level = world_2_2_exit(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_3:
                self.level = world_2_3(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            elif self.level_id == self.settings.W_2_4:
                self.level = world_2_4(self.screen, self.settings)
                self.level.scores.scores = self.game_score
                self.level.scores.coins = self.game_coin

            print("Level " + self.level.world + " loaded")
            
            
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
        if event.key == pygame.K_SPACE:
            self.space = True
        if event.key == pygame.K_LSHIFT:
            self.shift = True
        if event.key == pygame.K_s:
            self.down = True
        if event.key == pygame.K_f:
            self.fire = True

    def check_keyup(self, event):
        if event.key == pygame.K_d:
            self.right = False
        if event.key == pygame.K_a:
            self.left = False
        if event.key == pygame.K_SPACE:
            self.space = False
        if event.key == pygame.K_LSHIFT:
            self.shift = False
        if event.key == pygame.K_s:
            self.down = False
        if event.key == pygame.K_f:
            self.fire = False

    def do_event(self):
        self.level.update_mario(self.left, self.right, self.space, self.shift, self.down, self.fire)

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

    def reset_stats(self):
        self.level.mario.x = 500
        self.level.camera.x_pos = self.settings.WIDTH/2

    def run_game(self):
        while True:
            self.game_time = self.level.scores.timer
            self.game_score = self.level.scores.scores
            self.game_coin = self.level.scores.coins

            self.clock.tick(60)

            if self.level.scores.timer <= 0:
                self.game_active = False
                self.reset_stats()
                pygame.mouse.set_visible(True)
                self.level.scores.timer = 240

            self.screen.fill((0, 0, 0))

            self.check_events()

            if self.game_active is False:
                self.play_button.draw_button()
                self.exit_button.draw_button()

            if self.game_active is True:
                self.do_event()
                self.draw_screen()
                self.check_level()

            pygame.display.flip()


if __name__ == '__main__':
    game = SuperMario()
    game.run_game()
