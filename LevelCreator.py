from Level import Level


def world_1_1(screen, settings):
    world_1_level_1 = \
        Level(screen, settings, 'Resources/images/level_1_background.png', 'Resources/images/level_1_floor.png', (500, 600), (120,120), 500)
#    place_enemy()
#    place_block()
    return world_1_level_1
