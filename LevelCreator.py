from Level import Level


def world_1_1(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [8, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-1/level_1_background.png', 'Resources/Images/Backgrounds/World_1/1-1/level_1_floor.png', start_pos, [198, 2], 500, "1-1")

    new_level.place_warp("1-2_A", 'down', 28.5, 2)

    new_level.place_enemy('goomba', 22, 1)
    new_level.place_enemy('lava_bubble', 20, 1)
    new_level.place_enemy('goomba', 32, 1)
    new_level.place_enemy('goomba', 43, 1)
    new_level.place_enemy('goomba', 44.5, 1)
    new_level.place_enemy('goomba', 80, 9)
    new_level.place_enemy('goomba', 82, 9)
    new_level.place_enemy('goomba', 97, 1)
    new_level.place_enemy('goomba', 98.5, 1)
    new_level.place_enemy('koopa', 107, 1)
    new_level.place_enemy('goomba', 114, 1)
    new_level.place_enemy('goomba', 115.5, 1)
    new_level.place_enemy('goomba', 124, 1)
    new_level.place_enemy('goomba', 125.5, 1)
    new_level.place_enemy('goomba', 128, 1)
    new_level.place_enemy('goomba', 129.5, 1)
    new_level.place_enemy('goomba', 174, 1)
    new_level.place_enemy('goomba', 175.5, 1)

    new_level.place_block('q', 16, 4)
    new_level.place_block('b', 20, 4)
    new_level.place_block('q', 21, 4, "Power-Up")
    new_level.place_block('b', 22, 4)
    new_level.place_block('q', 22, 8)
    new_level.place_block('q', 23, 4)
    new_level.place_block('b', 24, 4)
    new_level.place_block('i', 65, 5, "1-Up")
    new_level.place_block('b', 77, 4)
    new_level.place_block('q', 78, 4, "Power-Up")
    new_level.place_block('b', 79, 4)
    new_level.mass_place_blocks('b', 80, 8, 8, 1)
    new_level.mass_place_blocks('b', 91, 8, 3, 1)
    new_level.place_block('q', 94, 8)
    new_level.place_block('b', 94, 4, "10-Coin")
    new_level.place_block('b', 100, 4)
    new_level.place_block('b', 101, 4, "Star")
    new_level.place_block('q', 106, 4)
    new_level.place_block('q', 109, 4)
    new_level.place_block('q', 109, 8, "Power-Up")
    new_level.place_block('q', 112, 4)
    new_level.place_block('b', 118, 4)
    new_level.mass_place_blocks('b', 121, 8, 3, 1)
    new_level.place_block('b', 128, 8)
    new_level.mass_place_blocks('b', 129, 4, 2, 1)
    new_level.mass_place_blocks('q', 129, 8, 2, 1)
    new_level.place_block('b', 131, 8)
    new_level.mass_place_blocks('b', 168, 4, 2, 1)
    new_level.place_block('q', 170, 4)
    new_level.place_block('b', 171, 4)

    return new_level


def world_1_2(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_floor.png', [3, 12], (120,120), 500, "1-2_A")
    new_level.mass_place_blocks('ub', 6, 11, 83, 1)
    new_level.place_block('ub', 89, 11, "Power-Up")
    new_level.mass_place_blocks('ub', 89, 11, 49, 1)
    new_level.place_block('q', 10, 4, "Power-Up")
    new_level.place_block('q', 11, 4)
    new_level.place_block('q', 12, 4)
    new_level.place_block('q', 13, 4)
    new_level.place_block('q', 14, 4)
    new_level.place_block('ub', 29, 5, "10-Coin")
    new_level.mass_place_blocks('ub', 39, 4, 3, 1)
    new_level.place_item('Coin', 40, 5)
    new_level.place_item('Coin', 45, 5)
    new_level.place_item('Coin', 41, 8)
    new_level.place_item('Coin', 42, 8)
    new_level.place_item('Coin', 43, 8)
    new_level.place_item('Coin', 44, 8)
    new_level.mass_place_blocks('ub', 39, 5, 1, 2)
    new_level.mass_place_blocks('ub', 41, 5, 1, 2)
    new_level.mass_place_blocks('ub', 42, 6, 2, 1)
    new_level.mass_place_blocks('ub', 44, 4, 1, 3)
    new_level.mass_place_blocks('ub', 45, 4, 2, 1)
    new_level.place_block('ub', 46, 5)
    new_level.place_block('ub', 46, 6, "Star")
    new_level.mass_place_blocks('ub', 52, 4, 1, 5)
    new_level.mass_place_blocks('ub', 53, 4, 1, 5)
    new_level.mass_place_blocks('ub', 54, 2, 1, 3)
    new_level.mass_place_blocks('ub', 55, 2, 1, 3)
    new_level.mass_place_blocks('ub', 54, 9, 1, 2)
    new_level.mass_place_blocks('ub', 55, 9, 1, 2)
    new_level.mass_place_blocks('ub', 58, 4, 6, 1)
    new_level.place_item('Coin', 58, 5)
    new_level.place_item('Coin', 59, 5)
    new_level.place_item('Coin', 60, 5)
    new_level.place_item('Coin', 61, 5)
    new_level.mass_place_blocks('ub', 62, 5, 1, 6)
    new_level.mass_place_blocks('ub', 63, 5, 1, 6)
    new_level.mass_place_blocks('ub', 58, 9, 4, 1)
    new_level.mass_place_blocks('ub', 58, 10, 4, 1)
    new_level.mass_place_blocks('ub', 66, 9, 4, 1)
    new_level.mass_place_blocks('ub', 66, 10, 4, 1)
    new_level.mass_place_blocks('ub', 67, 4, 1, 5)
    new_level.mass_place_blocks('ub', 68, 4, 2, 1)
    new_level.place_item('Coin', 68, 5)
    new_level.place_block('ub', 69, 5, "Power-Up")
    new_level.mass_place_blocks('ub', 72, 4, 1, 5)
    new_level.mass_place_blocks('ub', 73, 6, 1, 3)
    new_level.place_block('ub', 73, 5, "Coin")
    new_level.place_block('ub', 73, 4)
    new_level.mass_place_blocks('ub', 76, 4, 4, 1)
    new_level.mass_place_blocks('ub', 76, 9, 4, 1)
    new_level.place_item('Coin', 84, 8)
    new_level.place_item('Coin', 85, 8)
    new_level.place_item('Coin', 86, 8)
    new_level.place_item('Coin', 87, 8)
    new_level.place_item('Coin', 88, 8)
    new_level.place_item('Coin', 89, 8)
    new_level.mass_place_blocks('ub', 84, 5, 6, 1)
    new_level.mass_place_blocks('ub', 84, 6, 6, 1)
    new_level.mass_place_blocks('ub', 145, 5, 5, 1)
    new_level.place_block('plt',140, 0)
    new_level.place_block('plt',140, 5)
    new_level.place_block('plt',140, 10)
    new_level.place_block('ub', 150, 5, "Power-Up")
    new_level.place_block('plt', 155, 0)
    new_level.place_block('plt', 155, 5)
    new_level.place_block('plt', 155, 10)
    new_level.mass_place_blocks('ub', 160, 11, 10, 1)

    return new_level

def world_1_2_part2(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part2_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part2_floor.png', (500, 600), (120,120), 500)

    return new_level

def world_1_2_part3(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part3_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part3_floor.png', (500, 600), (120,120), 500)

    return new_level

def world_1_3(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-3/level_1_3_background.png', 'Resources/Images/Backgrounds/World_1/1-3/level_1_3_floor.png', (500, 600), (120,120), 500)

    return new_level

def world_1_4(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-4/level_1_4_background.png', 'Resources/Images/Backgrounds/World_1/1-4/level_1_4_floor.png', (500, 600), (120,120), 500)

    return new_level

def world_2_1(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_background.png', 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_floor.png', (500, 600), (120,120), 500)

    return new_level

def world_2_1_part2(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_part2_background.png', 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_part2_floor.png', (500, 600), (120,120), 500)

    return new_level
