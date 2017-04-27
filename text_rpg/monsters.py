class Monster(object):
	def __init__(self, health, power, name):
		self.health = health
		self.power = power
		self.name = name
		self.xp_value = 10
		self.max_health = 6

	def take_damage(self, damage):
		self.health -= damage
	def is_alive(self):
		return self.health > 0