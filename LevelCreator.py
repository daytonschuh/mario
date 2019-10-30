from Level import Level


def world_1_1(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [8, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-1/level_1_background.png', 'Resources/Images/Backgrounds/World_1/1-1/level_1_floor.png', start_pos, [198, 2], 500, "1-1", settings.W_1_1, settings.W_1_2, settings.W_1_1)

    new_level.place_warp(settings.W_1_1_sub, 'down', 57.5, 4)

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


def world_1_1_sub(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 10]

    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-1/2-1_sub_background.png', 'Resources/Images/Backgrounds/World_2/2-1/2_1_sub_floor.png', start_pos, [-32, 1], 500, "2-1", settings.W_1_1_sub, None, settings.W_1_1)

    new_level.place_warp(settings.W_1_1, "right", 13, 1)

    new_level.mass_place_blocks('ub', 4, 12, 7, 1)
    new_level.place_item("Coin", 4, 4)
    new_level.place_item("Coin", 5, 4)
    new_level.place_item("Coin", 6, 4)
    new_level.place_item("Coin", 7, 4)
    new_level.place_item("Coin", 8, 4)
    new_level.place_item("Coin", 9, 4)
    new_level.place_item("Coin", 10, 4)
    new_level.place_item("Coin", 4, 6)
    new_level.place_item("Coin", 5, 6)
    new_level.place_item("Coin", 6, 6)
    new_level.place_item("Coin", 7, 6)
    new_level.place_item("Coin", 8, 6)
    new_level.place_item("Coin", 9, 6)
    new_level.place_item("Coin", 10, 6)
    new_level.place_item("Coin", 5, 8)
    new_level.place_item("Coin", 6, 8)
    new_level.place_item("Coin", 7, 8)
    new_level.place_item("Coin", 8, 8)
    new_level.place_item("Coin", 9, 8)

    return new_level


def world_1_2_sub(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [115, 10]

    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_floor.png', start_pos, [-32, 1], 500, "1-2", settings.W_1_2_sub, None, settings.W_1_2)

    new_level.place_enemy('goomba', 16, 2)
    new_level.place_enemy('goomba', 15, 2)
    new_level.place_warp(settings.W_1_2_sub_sub, "down", 103.5, 3)
    new_level.place_warp(settings.W_1_2_exit, "right", 166, 4)
    new_level.mass_place_blocks('ub', 6, 11, 83, 1)
    new_level.place_block('ub', 89, 11, "Power-Up")
    new_level.mass_place_blocks('ub', 89, 11, 49, 1)
    new_level.place_block('q', 10, 4, "Power-Up")
    new_level.place_block('q', 11, 4)
    new_level.place_block('q', 12, 4)
    new_level.place_block('q', 13, 4)
    new_level.place_block('q', 14, 4)
    new_level.place_block('ub', 29, 5, "10-Coin")
    new_level.place_enemy('goomba', 29, 2)
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
    new_level.place_enemy('koopa', 46, 2)
    new_level.place_enemy('koopa', 48, 2)
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
    new_level.place_enemy('koopa', 60, 2)
    new_level.place_enemy('goomba', 63, 2)
    new_level.place_enemy('goomba', 64, 2)
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
    new_level.place_enemy('goomba', 73, 9)
    new_level.place_block('ub', 73, 5, "Coin")
    new_level.place_block('ub', 73, 4)
    new_level.place_enemy('goomba', 76, 5)
    new_level.place_enemy('goomba', 77, 5)
    new_level.mass_place_blocks('ub', 76, 4, 4, 1)
    new_level.mass_place_blocks('ub', 76, 9, 4, 1)
    new_level.place_item('Coin', 84, 8)
    new_level.place_item('Coin', 85, 8)
    new_level.place_item('Coin', 86, 8)
    new_level.place_item('Coin', 87, 8)
    new_level.place_item('Coin', 88, 8)
    new_level.place_item('Coin', 89, 8)
    new_level.place_enemy('goomba', 98, 2)
    new_level.place_enemy('goomba', 100, 2)
    new_level.place_enemy('goomba', 102, 2)
    new_level.place_enemy('piranha_plant', 103.5, 3.9)
    new_level.place_enemy('piranha_plant', 109.5, 4.9)
    new_level.place_enemy('goomba', 114, 2)
    new_level.place_enemy('piranha_plant', 115.5, 2.9)
    new_level.mass_place_blocks('ub', 84, 5, 6, 1)
    new_level.mass_place_blocks('ub', 84, 6, 6, 1)
    new_level.mass_place_blocks('ub', 145, 5, 5, 1)
    new_level.place_enemy('goomba', 132, 5.5)
    new_level.place_enemy('goomba', 135.5, 7.5)
    new_level.place_block('plt',140, 0)
    new_level.place_block('plt',140, 5)
    new_level.place_block('plt',140, 10)
    new_level.place_block('ub', 150, 5, "Power-Up")
    new_level.place_enemy('koopa', 151, 2)
    new_level.place_block('plt', 155, 0)
    new_level.place_block('plt', 155, 5)
    new_level.place_block('plt', 155, 10)
    new_level.mass_place_blocks('ub', 160, 11, 10, 1)

    return new_level


def world_1_2_sub_sub(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 10]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part2_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part2_floor.png', start_pos, [-32, 1], 500, "1-2", settings.W_1_2_sub_sub, None, settings.W_1_2)

    new_level.place_warp(settings.W_1_2_sub, 'right', 13, 1)

    new_level.mass_place_blocks('ub', 3, 4, 9, 1)
    new_level.place_block('ub', 12, 4, "10-Coin")
    new_level.mass_place_blocks('ub', 3, 8, 10, 4)

    new_level.place_item("Coin", 3, 1)
    new_level.place_item("Coin", 4, 1)
    new_level.place_item("Coin", 4, 5)
    new_level.place_item("Coin", 5, 1)
    new_level.place_item("Coin", 5, 5)
    new_level.place_item("Coin", 6, 1)
    new_level.place_item("Coin", 6, 5)
    new_level.place_item("Coin", 7, 1)
    new_level.place_item("Coin", 7, 5)
    new_level.place_item("Coin", 8, 1)
    new_level.place_item("Coin", 8, 5)
    new_level.place_item("Coin", 9, 1)
    new_level.place_item("Coin", 9, 5)
    new_level.place_item("Coin", 10, 1)
    new_level.place_item("Coin", 10, 5)
    new_level.place_item("Coin", 11, 1)
    new_level.place_item("Coin", 11, 5)

    return new_level

def world_1_2(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-2/2-2_background.png', 'Resources/Images/Backgrounds/World_2/2-2/2-2_floor.png', start_pos, [-32, 1], 500, "1-2", settings.W_1_2, None, settings.W_1_2)
    new_level.place_warp(settings.W_1_2_sub, 'right', 10, 1)

    return new_level


def world_1_2_exit(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [4.5, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part3_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_part3_floor.png', start_pos, [22, 2], 500, "1-2", settings.W_1_2_exit, settings.W_1_3, settings.W_1_2)
    new_level.place_enemy("piranha_plant", 3.5, 3)
    return new_level


def world_1_3(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 2]

    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-3/level_1_3_background.png', 'Resources/Images/Backgrounds/World_1/1-3/level_1_3_floor.png', start_pos, [152,2], 500, "1-3", settings.W_1_3, settings.W_1_4, settings.W_1_3)

    new_level.place_enemy('koopa', 29, 9)
    new_level.mass_place_blocks('invis_plt', 18, 1, 4, 1)
    new_level.mass_place_blocks('invis_plt', 24, 4, 8, 1)
    new_level.mass_place_blocks('invis_plt', 26, 8, 5, 1)
    new_level.place_item('Coin', 27, 9)
    new_level.place_item('Coin', 28, 9)
    new_level.place_item('Coin', 29, 9)
    new_level.mass_place_blocks('invis_plt', 32, 1, 3, 1)
    new_level.place_item('Coin', 33, 2)
    new_level.mass_place_blocks('invis_plt', 35, 5, 5, 1)
    new_level.mass_place_blocks('invis_plt', 40, 9, 7, 1)
    new_level.place_item('Coin', 37, 11)
    new_level.place_item('Coin', 38, 11)
    new_level.mass_place_blocks('invis_plt', 50, 0, 4, 1)
    new_level.mass_place_blocks('invis_plt', 59, 0, 5, 1)
    new_level.place_enemy('goomba', 42, 10)
    new_level.place_enemy('goomba', 44, 10)
    new_level.place_item('Coin', 50, 7)
    new_level.place_item('Coin', 51, 7)
    new_level.place_block('q', 59, 3, "Power-Up")
    new_level.place_block('vert_plt', 55, 8)
    new_level.mass_place_blocks('invis_plt', 60, 8, 4, 1)
    new_level.mass_place_blocks('invis_plt', 65, 0, 5, 1)
    new_level.mass_place_blocks('invis_plt', 70, 4, 3, 1)
    new_level.mass_place_blocks('invis_plt', 76, 7, 6, 1)
    new_level.place_item('Coin', 60, 9)
    new_level.place_item('Coin', 61, 9)
    new_level.place_item('Coin', 62, 9)
    new_level.place_item('Coin', 63, 9)
    new_level.place_enemy('koopa_paratroopa', 78, 9)
    new_level.place_enemy('goomba', 82, 9)
    new_level.place_block('horiz_plt', 83, 6)
    new_level.place_item('Coin', 85, 8)
    new_level.place_item('Coin', 86, 8)
    new_level.place_block('invert_horiz_plt', 95, 4)
    new_level.mass_place_blocks('invis_plt', 98, 2, 4, 1)
    new_level.place_item('Coin', 93, 9)
    new_level.place_item('Coin', 94, 9)
    new_level.place_item('Coin', 97, 9)
    new_level.place_item('Coin', 98, 9)
    new_level.mass_place_blocks('invis_plt', 104, 6, 8, 1)
    new_level.mass_place_blocks('invis_plt', 113, 0, 3, 1)
    new_level.place_enemy('koopa', 111, 9)
    new_level.place_enemy('koopa_paratroopa', 117, 9)
    new_level.place_item('Coin', 113, 1)
    new_level.place_item('Coin', 114, 1)
    new_level.place_item('Coin', 115, 1)
    new_level.mass_place_blocks('invis_plt', 116, 4, 4, 1)
    new_level.place_item('Coin', 120, 8)
    new_level.place_item('Coin', 121, 8)
    new_level.mass_place_blocks('invis_plt', 122, 4, 4, 1)
    new_level.place_block('horiz_plt', 127, 7,)
    new_level.place_enemy('koopa', 137, 5)

    return new_level

def world_1_4(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-4/level_1_4_background.png', 'Resources/Images/Backgrounds/World_1/1-4/level_1_4_floor.png', [3,2], (120,120), 500, "1-4")
    new_level.place_block('q', 29.5, 7, "Power-Up")
    new_level.place_block('i', 106.5, 4, "Coin")
    new_level.place_block('i', 109.5, 4, "Coin")
    new_level.place_block('i', 112.5, 4, "Coin")
    new_level.place_block('i', 107.5, 8, "Coin")
    new_level.place_block('i', 110.5, 8, "Coin")
    new_level.place_block('i', 113.5, 8, "Coin")
    return new_level

def world_2_1(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [10, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_background.png', 'Resources/Images/Backgrounds/World_2/2-1/level_2_1_floor.png', start_pos, (200, 2), 500, "2-1", settings.W_2_1, settings.W_2_2, settings.W_2_1)

    new_level.place_block('e', 189, 4)

    new_level.place_warp(settings.W_2_1_sub, "down", 103.5, 4)

    new_level.place_enemy("goomba", 24, 6)
    new_level.place_enemy("koopa", 32, 1)
    new_level.place_enemy("koopa", 33, 1)
    new_level.place_enemy("goomba", 42, 1)
    new_level.place_enemy("goomba", 43.5, 1)
    new_level.place_enemy("piranha_plant", 46.5, 5)
    new_level.place_enemy("koopa", 55, 5)
    new_level.place_enemy("goomba", 59, 1)
    new_level.place_enemy("goomba", 60.5, 1)
    new_level.place_enemy("koopa", 66, 1)
    new_level.place_enemy("goomba", 68, 1)
    new_level.place_enemy("goomba", 69.5, 1)
    new_level.place_enemy("goomba", 71, 1)
    new_level.place_enemy("piranha_plant", 74.5, 5)
    new_level.place_enemy("goomba", 87, 1)
    new_level.place_enemy("goomba", 88.5, 1)
    new_level.place_enemy("goomba", 90, 1)
    new_level.place_enemy("goomba", 102.5, 5)
    new_level.place_enemy("piranha_plant", 103.5, 5)
    new_level.place_enemy("goomba", 114.5, 3)
    new_level.place_enemy("piranha_plant", 115.5, 3)
    new_level.place_enemy("goomba", 120, 1)
    new_level.place_enemy("piranha_plant", 122.5, 5)
    new_level.place_enemy("piranha_plant", 130.5, 5)
    new_level.place_enemy("koopa", 137, 1)
    new_level.place_enemy("koopa_paratroopa", 152, 1)
    new_level.place_enemy("goomba", 163, 1)
    new_level.place_enemy("goomba", 164.5, 1)
    new_level.place_enemy("koopa_paratroopa", 170, 1)
    new_level.place_enemy("koopa_paratroopa", 172, 1)
    new_level.place_enemy("piranha_plant", 176.5, 4)
    new_level.place_enemy("koopa", 185, 1)

    new_level.place_block('b', 15, 4)
    new_level.place_block('b', 16, 4, "Power-Up")
    new_level.place_block('b', 17, 4)
    new_level.place_block('i', 28, 4)
    new_level.place_block('i', 28, 8, "1-Up")
    new_level.mass_place_blocks('b', 29, 8, 3, 1)
    new_level.place_block('q', 53, 4, "Power-Up")
    new_level.mass_place_blocks('q', 53, 8, 5, 1)
    new_level.mass_place_blocks('q', 54, 4, 4, 1)
    new_level.place_block('b', 68, 4)
    new_level.place_block('b', 69, 8, "Star")
    new_level.mass_place_blocks('b', 70, 8, 3, 1)
    new_level.mass_place_blocks('q', 79, 4, 4, 1)
    new_level.mass_place_blocks('b', 81, 8, 2, 1)
    new_level.place_block('b', 83, 8, "Coin")
    new_level.mass_place_blocks('b', 84, 8, 2, 1)
    new_level.mass_place_blocks('q', 85, 4, 3, 1)
    new_level.mass_place_blocks('b', 92, 8, 4, 1)
    new_level.place_block('b', 125, 8, "Power-Up")
    new_level.mass_place_blocks('b', 126, 8, 3, 1)
    new_level.place_block('b', 161, 4, "Coin")
    new_level.mass_place_blocks('b', 164, 8, 5, 1)
    new_level.place_block('q', 170, 4)
    new_level.place_block('b', 172, 8, "Power-Up")
    new_level.mass_place_blocks('b', 185, 4, 2, 1)
    new_level.place_block('i', 186, 8, "Coin")

    return new_level


def world_2_1_sub(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 10]

    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-1/2-1_sub_background.png', 'Resources/Images/Backgrounds/World_2/2-1/2_1_sub_floor.png', start_pos, [-32, 1], 500, "2-1", settings.W_2_1_sub, None, settings.W_2_1)

    new_level.place_warp(settings.W_2_1, "right", 13, 1)

    new_level.mass_place_blocks('ub', 4, 12, 7, 1)
    new_level.place_item("Coin", 4, 4)
    new_level.place_item("Coin", 5, 4)
    new_level.place_item("Coin", 6, 4)
    new_level.place_item("Coin", 7, 4)
    new_level.place_item("Coin", 8, 4)
    new_level.place_item("Coin", 9, 4)
    new_level.place_item("Coin", 10, 4)
    new_level.place_item("Coin", 4, 6)
    new_level.place_item("Coin", 5, 6)
    new_level.place_item("Coin", 6, 6)
    new_level.place_item("Coin", 7, 6)
    new_level.place_item("Coin", 8, 6)
    new_level.place_item("Coin", 9, 6)
    new_level.place_item("Coin", 10, 6)
    new_level.place_item("Coin", 5, 8)
    new_level.place_item("Coin", 6, 8)
    new_level.place_item("Coin", 7, 8)
    new_level.place_item("Coin", 8, 8)
    new_level.place_item("Coin", 9, 8)

    return new_level

def world_2_2(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-2/2-2_background.png', 'Resources/Images/Backgrounds/World_2/2-2/2-2_floor.png', start_pos, [-32, 1], 500, "2-2", settings.W_2_2, None, settings.W_2_2)
    new_level.place_warp(settings.W_2_2_sub, 'right', 10, 1)
    return new_level

def world_2_2_water(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [3, 10]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-2/2-2_water_bg.png', 'Resources/Images/Backgrounds/World_2/2-2/2-2_water_floor.png', start_pos, [-32, 1], 500, "2-2",  settings.W_2_2_sub, None, settings.W_2_2, True)
    new_level.place_warp(settings.W_2_2_exit, 'right', 189.9, 5)
    return new_level

def world_2_2_exit(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [4.5, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-2/2-2_exit_background.png', 'Resources/Images/Backgrounds/World_2/2-2/2-2_exit_floor.png', start_pos, [22, 2], 500, "2-2", settings.W_2_2_exit, settings.W_2_3, settings.W_2_2)

    new_level.place_enemy("piranha_plant", 3.5, 2)
    return new_level

def world_2_3(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [4.5, 1]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-3/2-3_background.png', 'Resources/Images/Backgrounds/World_2/2-3/2-3_floor.png', start_pos, [22, 2], 500, "2-3", settings.W_2_3, settings.W_2_4, settings.W_2_3)
    return new_level

def world_2_4(screen, settings, start_pos=None):
    if start_pos is None:
        start_pos = [6, 4]
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_2/2-4/2-4_background.png', 'Resources/Images/Backgrounds/World_2/2-4/2-4_floor.png', start_pos, [-32, 1], 500, "2-4", settings.W_2_4, settings.W_1_1, settings.W_2_4)
    return new_level
