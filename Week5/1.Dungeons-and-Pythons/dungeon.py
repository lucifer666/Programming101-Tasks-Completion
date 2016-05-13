from entity import *

SPAWN_HERO = "H"
START_POINT = "S"
OBSTACLE = "#"
ENEMY = "E"
TREASURE = "T"
UP = (-1, 0)




class Dungeon(object):

	def __init__(self, load_map):
		self.__dungeon_map = load_map

	def print_map(self):
		try:
			with open(self.__dungeon_map, 'r') as fread:
				read_map = fread.read()
				print (read_map)	
		except IOError:
			print ("Cannot open the map!")

	def spawn(self, hero):
		map_list = []
		try:
			with open(self.__dungeon_map, 'r+') as fread_fwrite:
				map_list = fread_fwrite.read().split('\n')
				if self.check_if_hero_exists(map_list) == True:
					print ("There is a Hero on the map already!")
					return False
				if self.check_if_start_point_exists(map_list) == False:
					print ("Game Over!")
					return False
				for row_number, current_row in enumerate(map_list):
					if START_POINT in current_row:
						updated_row = current_row.replace(START_POINT, SPAWN_HERO)
						map_list[row_number] = updated_row
						fread_fwrite.seek(0)
						fread_fwrite.truncate()
						fread_fwrite.write('\n'.join(map_list))
						break
				return True
		except IOError:
			print ("Cannot open the map!")

	def check_if_start_point_exists(self, map_list):
		map_str = '\n'.join(map_list)
		if START_POINT not in map_str and SPAWN_HERO not in map_str:
			return False
		return True

	def check_if_hero_exists(self, map_list):
		map_str = '\n'.join(map_list)
		if SPAWN_HERO in map_str: 
			return True
		return False

	def move_hero(self, direction):
		map_list = []
		try:
			with open(self.__dungeon_map, 'r+') as fread_fwrite:
				map_list = fread_fwrite.read().split('\n')
				for row_position in range(0, len(map_list)):
					for col_position in range(0, len(map_list[0])):
						if direction == "up":
							if map_list[row_position][col_position] == SPAWN_HERO:
								map_list[row_position+UP[0]][col_position+UP[1]]  
				
		except IOError:
			print ("Cannot open the map!")

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

d = Dungeon("level1.txt")
d.print_map()
d.spawn(h)
d.print_map()
d.spawn(h)
d.move_hero("up") 