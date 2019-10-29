# store all game settings here
class Settings:
    def __init__(self):
        self.WIDTH = 1200
        self.HEIGHT = 672
        self.fps = 30
        self.bg_speed = 1 # speed of the background
        self.upscale = 3

        # Physics Variables
        self.gravity = 0.8
        self.gravity_max = 20
        # Mario Variables
        self.jump_speed = [12, 6, 3]
        self.run_speed = 6
        self.walk_speed = 3
        self.acceleration_x = 1
        self.decceleration_x = 0.2
        self.invincible_time = 600

        # Enemy Variables
        self.enemy_walk_speed = 1

        # Block Variables
        self.block_recoil = 3
        self.block_size = 48

        # Asset IDs
        self.static_id = -1
        self.block_id = 0
        self.invisible_block_id = 1
        self.platform_id = 2
        self.bounce_id = 3

        self.no_collision_id = 10
        self.item_id = 11

        self.star_id = 20
        self.mushroom_id = 21
        self.green_mushroom_id = 22
        self.flower_id = 23
        self.coin_id = 24

        self.goomba_id = 30
        self.koopa_troopa_id = 31
        self.koopa_paratroopa_id = 32
        self.koopa_shell_id = 33
        self.piranha_plant_id = 34
        self.lava_bubble_id = 35
        self.one_way_platform_id = 36
