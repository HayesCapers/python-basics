import time
from random import randint
class Pokemon(object):
	def __init__(self, name):
		self.name = name
		self.hp = 5
		self.power = 0
		self.max_power = 6

	def name_select(self, pokemon):
		print "Would you like to name %s? (y/n)" % pokemon.name
		user_input = raw_input('> ')
		if user_input == 'y':
			pokemon_new_name = raw_input('Enter name: ')
			pokemon.name = pokemon_new_name
		elif user_input == 'n':
				pass

	def print_status(self):
		print "%s has %d hp remaining." % (self.name, self.hp)
		time.sleep(1.5)

	def alive(self):
		return self.hp > 0

	def attack(self, enemy):
		if not self.alive():
			return
		print '%s attacks %s' % (self.name, enemy.name)
		enemy.recieve_damage(randint(0, self.max_power))
		time.sleep(1.5)


	def recieve_damage(self, hit_points):
		self.hp -= hit_points
		print '%s recieved %d damage.' % (self.name, hit_points)
		if self.hp <= 0:
			print '%s has been knocked out.' % self.name 



	


	
