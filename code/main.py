import pygame, sys
from settings import *
from pytmx.util_pygame import load_pygame
from tile import Tile, CollisionTile
from player import Player
from pygame.math import Vector2 as vector

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.offset = vector()

	def custom_draw(self,player):

		# exercise
		# change the offset vector
		self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
		self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

		# blit all sprites
		for sprite in sorted(self.sprites(), key = lambda sprite: sprite.z):
			offset_rect = sprite.image.get_rect(center = sprite.rect.center)
			offset_rect.center -= self.offset
			self.display_surface.blit(sprite.image, offset_rect)
			
class Main:
	def __init__(self):
		pygame.init()
		self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
		pygame.display.set_caption("Contra")
		self.clock = pygame.time.Clock()

		# groups
		self.all_sprites = AllSprites()
		self.collision_sprites = pygame.sprite.Group()

		self.setup()

	def setup(self):
		tmx_map = load_pygame('../data/map.tmx')

		# collision tiles
		for x, y, surf in tmx_map.get_layer_by_name('Level').tiles():
			CollisionTile((x * 64,y * 64), surf, [self.all_sprites,self.collision_sprites])

		# tiles
		for layer in ['BG', 'BG Detail', 'FG Detail Bottom', 'FG Detail Top']:
			for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
				Tile((x * 64,y * 64), surf, self.all_sprites, LAYERS[layer])

		# objects
		for obj in tmx_map.get_layer_by_name('Entities'):
			if obj.name == 'Player':
				self.player = Player((obj.x,obj.y), self.all_sprites, '../graphics/player', self.collision_sprites)

	def run(self):
		while True:
			# event loop
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000
			self.display_surface.fill((249,131,103))

			self.all_sprites.update(dt)
			self.all_sprites.custom_draw(self.player)

			pygame.display.update()

if __name__ == '__main__':
	main = Main()
	main.run()