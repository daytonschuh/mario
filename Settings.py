# store all game settings here
class Settings:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 672
        self.fps = 30
        self.bg_speed = 1 # speed of the background
        self.block_size = 48
        self.upscale = 3

        # Physics Variables
        self.gravity = 0.8
        self.gravity_max = 20

        # Mario Variables
        self.jump_speed = [12, 6, 3]
        self.run_speed = 12
        self.walk_speed = 6
        self.acceleration_x = 1
