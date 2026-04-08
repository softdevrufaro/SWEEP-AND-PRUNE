import pygame as pg 
from settings import * 
from sys import exit 
from tile import *
import operator
import math

# Initialize Pygame 
pg.init()

# setting up the screen 
screen = pg.display.set_mode((Window_width , Window_height))
pg.display.set_caption(window_caption)

#initializing the clock 
clock = pg.time.Clock()

# creating a list of rectangles 
rect_list = []

for i in range(1000):
	rect_list.append(tile(((i%20)*10 , (i//20)*10 ), (5 , 5 ), RED , i))

for i in range(1000):
	rect_list.append(tile((Window_width - (i%20)*10 , (i//20)*10 ), (5 , 5 ), BLUE , len(rect_list) + i))

# Function to sort the list according to the distance of each object from the point (0 , 0)
def sorttiles(tiles_list):
	if tiles_list:
		obj_dict = {} # The index will be the key and the value is the distance from origin
		for index , my_tile in enumerate(tiles_list):
			obj_dict[index] = math.sqrt((my_tile.rect.x)**2 + (my_tile.rect.y)**2)
		# Here we sort the dictionary according the value of the distance from origin
		sorted_objects = dict(sorted(obj_dict.items(), key=operator.itemgetter(1)))
		new_list = [] # this is the new list that will be sorted using the index keys in the dictionary
		for key in sorted_objects.keys():
			new_list.append(tiles_list[key])
		return new_list # here we return the new object list
	else:
		return []

# list containing the index of each colliding rect
collision_index_list = []
# The minimum difference between the distances of the objects from origin before checking for collisions
min_diff = 5
# Main game loop 
running = True 
while running: 
	# Handle events 
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				running = False
	# Paint the screen black in the background
	screen.fill(BLACK)
	# Checking for collisions in among the objects
	# First we sort the list of objects
	rect_list = sorttiles(rect_list)
	for index ,my_tile in enumerate(rect_list):
		i = index + 1 
		while i < len(rect_list):
			rect_2 = rect_list[i].rect 
			# Here we find the difference of the distance from origin between the two objects
			difference = (math.sqrt((rect_2.x**2) + (rect_2.y ** 2)))-(math.sqrt((my_tile.rect.x**2) + (my_tile.rect.y**2)))
			if difference < 0 : 
				difference = difference * -1
			if difference < min_diff:
				if my_tile.check_collisions(rect_list[i]):
					collision_index_list.append(index)
					collision_index_list.append(i)
				i+=1
			else:
				break
		pg.draw.rect(screen , my_tile.color , my_tile.rect)
		if my_tile.color == RED:
			my_tile.rect.x += 1
		elif my_tile.color == BLUE:
			my_tile.rect.x -= 1
	# Remove tiles in reverse order to avoid index shifting issues
	for index in sorted(collision_index_list, reverse=True):
		rect_list.pop(index)
	collision_index_list = []
	#Updating the display
	pg.display.flip()
	#Control Frame rate 
	clock.tick(FPS)

pg.quit()
exit()
