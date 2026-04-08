# importing pygame 
import pygame as pg  

# Creating the tile class 
class tile: 
	def __init__(self , position , size , color , id):
		self.rect = pg.Rect(position[0] , position[1] , size[0] , size[1])
		self.color = color
		self.id  = id
		self.collision_flag = False

	# Checking for collisions between two tiles
	def check_collisions(self , tile):
		if self.rect.colliderect(tile.rect):
			print(f"Collision between tile {self.id} and {tile.id}")
			self.collision_flag = True
			tile.collision_flag = True
			return True
		else:
			return False