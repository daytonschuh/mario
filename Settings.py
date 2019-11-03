# store all game settings here
class Settings:
    def __init__(self):
        self.WIDTH = 768
        self.HEIGHT = 672
        self.fps = 30
        self.bg_speed = 1  # speed of the background
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
        self.flag_fall = 3

        self.swim_up_speed = 6
        self.sink_speed = 0.2
        self.sink_max_speed = 3
        self.swim_max_speed = 3

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
        self.flag_id = 4
        self.auto_id = 5
        self.fire_id = 6

        self.no_collision_id = 10
        self.item_id = 11

        self.star_id = 20
        self.mushroom_id = 21
        self.green_mushroom_id = 22
        self.flower_id = 23
        self.coin_id = 24

        # Goombas, Koopas, Koopa Paratroopas, Non-Water Cheep-Cheeps
        self.ground_enemy = 30
        # Pirahna Plant, Water Cheep-Cheep, Blooper
        self.no_jump_phase_enemy = 31
        # Lava Bubble
        self.pure_phase_enemy = 32
        # Koopa, Koopa Paratroopa (SHELLS ONLY)
        self.slide_enemy = 33
        # Bowser
        self.tough_enemy = 34

        self.one_way_platform_id = 40
        self.down_platform_id = 40

        self.mario_id = 99
        self.star_power_id = 100

        # Level_ID
        self.W_1_1 = 0
        self.W_1_1_sub = 1
        self.W_1_2 = 2
        self.W_1_2_sub = 3
        self.W_1_2_sub_sub = 4
        self.W_1_2_exit = 5
        self.W_1_3 = 6
        self.W_1_4 = 7
        self.W_2_1 = 8
        self.W_2_1_sub = 9
        self.W_2_2 = 10
        self.W_2_2_sub = 11
        self.W_2_2_exit = 12
        self.W_2_3 = 13
        self.W_2_4 = 14
