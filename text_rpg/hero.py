class Hero(object):
	def __init__(self, name = 'Incognitio'):
		self.name = name
		self.health = 10
		self.power = 5

	def cheer_hero(self):
		print 'Fight hard, %s' % self.name

	#this class method returns a boolean. True is the hero is alive, False if the hero is dead
	def is_alive(self):
		if (self.health > 0):
			return True
		else:
			return False
