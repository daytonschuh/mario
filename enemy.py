# potentially rewriting this entire thing
from pygame.sprite import Sprite
from pygame import *


class Enemy(Sprite):
	""" Base class for enemies. """
    def __init__(self, screen, settings, camera, spawn_pos):
        super().__init__()
		self.sprite_sheet = pygame.image.load('Resources/Images/enemy_sprite_sheet')
        self.screen = screen
        self.settings = settings
        self.active = False
        self.camera = camera
        self.pos = spawn_pos
		self.velocity = 10
		
		# Generate frames from sprite sheet.
        self.frames = []
		generate_frames()
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0

        self.name = name

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y

    def update(self):
        self.rect.left = self.pos - self.camera.x_pos
        if not self.active:
            if self.rect < self.settings.WIDTH:
                self.active = True
        if self.active:
            self.behavior()
            if self.rect.right < 0:
                self.active = False
                # self.kill()
		
	def generate_frames(self, x, y, direction, name, setup_frames):
        """ Create frames from the sprite sheet. """
		image = pygame.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image = pygame.transform.scale(image,
                                   (int(rect.width),
                                    int(rect.height))
        return image

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Blooper(Enemy):
	# basically follows Mario
	pass

class Bill_Blaster(Enemy):
	# stationary
	# shoots when mario crosses in the path
	pass

class Bullet_Bill(Enemy):
	# just flies straight
	# can be bounced on
	pass

class Buzzy_Beetle(Enemy):
	# uh?
	pass

class Cheep_Cheep(Enemy):
	# gravity affected jumping enemy
	# comes from off screen
    # track x to know when to jump
	pass

class Fire_Bar(Enemy):
	# unsure of behavior
    # pretty sure this just spins in circles
    # might want to add something like length to append to a group of fire balls on the bar?
    # or just hard code it
	pass

class Goomba(Enemy):
	# walks back and forth
	# jumping on it kills it
	pass

class Hammer_Bro(Enemy):
	# stationary
	# throws gravity affected 'bullets'
	pass

class Koopa_Paratroopa(Enemy):
	# jumps and moves
	# first bounce knocks it to a troopa, second turns to a shell, third kicks it
	pass

class Koopa_Troopa(Enemy):
	# walks back and forth
	# first bounce turns it to a shell, second kicks it
	pass

class Lava_Bubble(Enemy):
	# unsure of behavior
    # perhaps just like Piranha plant up and down with delay
	pass

class Piranha_Plant(Enemy):
	# up and down delay
	# behind pipe, in front of backdrop
	pass

class Spiny_Egg(Enemy):
	# drops until it hits the floor
	# short delay before becoming spiny
	pass

class Spiny(Enemy):
	# walks back and forth
	# cannot be jumped on
	pass

class Lakitu(Enemy):
	# flies above and follows mario
	# drops spiny eggs  that turn into spiny enemy
	pass
