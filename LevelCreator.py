from Level import Level


def world_1_1(screen, settings):
    new_level = \
        Level(screen, settings, 'Resources/Images/level_1_background.png', 'Resources/Images/level_1_floor.png', (500, 600), (120,120), 500)

#    place_enemy()
    new_level.place_block('q', 16, 4)
    new_level.place_block('b', 20, 4)
    new_level.place_block('q', 21, 4)
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