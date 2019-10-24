import pygame
from Text import *
from Timer import *

class Scoring:
    def __init__(self, screen, score, world, coins, time):
        self.screen = screen
        self.clock = Timer(60)
        self.score_text = Text(self)
        self.score_num_text = Text(self)
        self.world_text = Text(self)
        self.world_num_text = Text(self)
        self.coins_text = Text(self)
        self.timer_text = Text(self)
        self.timer_num_text = Text(self)
        self.scores = score
        self.world = world
        self.coins = coins
        self.timer = time

    def draw_text(self):
        self.score_num_text.message(str(self.scores), (255, 255, 255), 100, 30)
        self.score_text.message('MARIO', (255, 255, 255), 100, 10)
        self.world_text.message('WORLD', (255, 255, 255), 675, 10)
        self.world_num_text.message(str(self.world), (255, 255, 255), 675, 30)
        self.coins_text.message('COIN*' + str(self.coins), (255, 255, 255), 350, 20)
        self.timer_text.message('TIME', (255, 255, 255), 900, 10)
        self.timer_num_text.message(str(self.timer), (255, 255, 255), 900, 30)

    def update_text(self):
        self.run_clock()

    def add_coin(self):
        self.coins += 1

    def add_score(self, score):
        self.scores += score

    def check_time(self):
        if self.timer == 0:
            self.timer.out_of_time = True

    def run_clock(self):
        self.clock.tick()
        if self.clock.check():
            self.timer -= 1
