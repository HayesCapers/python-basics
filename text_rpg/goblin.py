class Goblin(object):
	def __init__(self):
		self.health = 6
		self.power = 2
		self.name = 'Goblin'
		self.xp_value = 5
		max_health = 6

	def take_damage(self, damage):
		self.health -= damage
	def is_alive(self):
		return self.health > 0