from class_pokemon import Pokemon
class Plant(Pokemon):
	def __init__(self):
		self.health = 5


class Bulbasaur(Plant):
	def __init__(self,name = 'Bulbasaur'):
		self.hp = 25
		self.name = name
		self.type_name = 'Bulbasaur'
		self.xp = 0
		self.level = 1
		self.max_hp = 25
		self.max_power = 7
		