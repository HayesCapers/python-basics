from class_pokemon import Pokemon
class Fire(Pokemon):
	def __init__(self):
		self.resistance = 3



class Charmander(Fire):
	def __init__(self,name = 'Charmander'):
		self.hp = 16
		self.name = name
		self.type_name = 'Charmander'
		self.xp = 0
		self.level = 1
		self.max_hp = 16
		self.max_power = 10