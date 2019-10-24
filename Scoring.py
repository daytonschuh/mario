import pygame
from Text import *

class Scoring:
    def __init__(self, screen, score, world, coins, time):
        self.screen = screen
        self.score_text = Text(self)
        self.world_text = Text(self)
        self.coins_text = Text(self)
        self.timer_text = Text(self)
        self.scores = score
        self.world = world
        self.coins = coins
        self.timer = time

    def draw_text(self):
        self.score_text.message('SCORE ' + str(self.scores), (255, 255, 255), 425, 20)
        self.world_text.message('WORLD ' + str(self.world), (255, 255, 255), 300, 20)
        self.coins_text.message('COINS ' + str(self.coins), (255, 255, 255), 200, 20)
        self.timer_text.message('TIME ' + str(self.timer), (255, 255, 255), 100, 20)

    def update_text(self):
        pass
