class Camera:
    def __init__(self, settings, map_image):
        self.x_pos = settings.WIDTH / 2
        self.max_scroll = map_image.get_rect().right - (settings.WIDTH / 2)

    def center_camera(self, sprite):
        if sprite.x > self.x_pos and self.x_pos < self.max_scroll:
            self.x_pos = sprite.x
