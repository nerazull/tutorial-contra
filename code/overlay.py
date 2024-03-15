import pygame

class Overlay:
	def __init__(self, player):
		self.player = player
		self.display_surface = pygame.display.get_surface()
		self.health_surf = pygame.image.load('../graphics/health.png').convert_alpha()

	def display(self):
		# exercise:
		# blit the health surface as many times as the player has health
		for h in range(self.player.health):
			x_pos = 10 + h * (self.health_surf.get_width() + 4)
			y_pos = 10
			self.display_surface.blit(self.health_surf,(x_pos,y_pos))
			

