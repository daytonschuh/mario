from Level import Level


def world_1_1(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-1/level_1_background.png', 'Resources/Images/Backgrounds/World_1/1-1/level_1_floor.png', (500, 600), (120,120), 500)

    new_level.place_enemy('goomba', 22, 1)
    new_level.place_enemy('goomba', 43, 1)
    new_level.place_enemy('goomba', 44.5, 1)

    new_level.place_block('q', 16, 4)
    new_level.place_block('b', 20, 4)
    new_level.place_block('q', 21, 4, "Mushroom")
    new_level.place_block('b', 22, 4)
    new_level.place_block('q', 22, 8)
    new_level.place_block('q', 23, 4)
    new_level.place_block('b', 24, 4)
    new_level.place_block('i', 65, 5, "1-Up")
    new_level.place_block('b', 77, 4)
    new_level.place_block('q', 78, 4)
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
        Level(screen, settings, 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_background.png', 'Resources/Images/Backgrounds/World_1/1-2/level_1_2_floor.png', (500, 600), (120,120), 500)

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
