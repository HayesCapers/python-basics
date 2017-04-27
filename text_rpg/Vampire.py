from monsters import Monster
class Vampire(Monster):
	def __init__(self):
		super(Vampire, self).__init__()
		self.health = 6
		self.power = 2
		self.name = 'Vampire'
		self.xp_value = 10
		self.max_health = 6

	