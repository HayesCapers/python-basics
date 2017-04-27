from random import randint

class Hero(object):
	def __init__(self, name = 'Ash'):
		self.name = name
		self.coins = 0
		self.current_pokemon = []
		self.pokeball_count = 10
		self.potion_count = 0
		# self.number_of_pokemon_alive = len(self.current_pokemon)
		

	def add_pokemon(self, pokemon):
		self.current_pokemon.append(pokemon)
		
	def pokemon_status(self):
		for i in self.current_pokemon:
			print '%s has %d hp.' % (i.name, i.hp)

	# def number_of_pokemon_alive(self):
	# 	for i in self.current_pokemon:
	# 		if not i.alive():
	# 			self.pokemon_alive -= 1

	def apply_potion(self, character):
		character.hp += 5
		print '%s\'s hp has increased to %d' % (character.name, character.hp)
	
	def buy(self, item):
		self.coins -= item.cost

	def capture(self, pokemon):
		odds_capture = 0
		self.pokeball_count -= 1
		if self.pokeball_count >= 0:
			if pokemon.hp == pokemon.max_hp:
				odds_capture = randint(0, 100)
			elif pokemon.hp <= (pokemon.hp / 2):
				odds_capture = randint(0, 30)
			if odds_capture < 25:
				print '%s captured %s!' % (self.name, pokemon.name)
				pokemon.name_select(pokemon)
				self.add_pokemon(pokemon)
			else:
				print '%s has escaped the Pokeball!' % pokemon.name
		else:
			print '%s has no Pokeballs left!!!' % self.name

	def apply(self, character):
		character.hp += 5
		print '%s\'s hp has increased to %d' % (character.name, character.hp)


	

	#this class method returns a boolean. True is the hero is alive, False if the hero is dead
	

	def switch_pokemon(self):
		while True:
			print '///////////////////////////'
			print '//These are your Pokemon//'
			print '/////////////////////////'


			for i in range(0,len(self.current_pokemon)):
				print '\n%d. %s: %dhp remaining' % (i+1, self.current_pokemon[i].name, self.current_pokemon[i].hp)
			print '\n7. Don\'t select new pokemon'
			input = int(raw_input('> '))
			if input == 7:
				break
			else:
				pokemon_to_use = self.current_pokemon[input - 1]
				self.current_pokemon.remove(pokemon_to_use)
				self.current_pokemon.insert(0, pokemon_to_use)
				print self.current_pokemon
				break


	











	# def check_level(self):
	# 	if self.xp > 3:
	# 		self.level = 2
	# 		self.level_up()
	# def level_up(self):
	# 	print "Thou hast leveled up %s! Thy hp is now %d and thy power is now %d" % (self.name, self.max_health, self.power)
	# 	self.max_health += 10
	# 	self.health = self.max_health
	# 	self.power += 5
	# def increase_health(self, amount):
	# 	self.health += amount
	# 	if self.health > self.max_health:
	# 		self.health = self.max_health
	# def is_alive(self):
	# 	if (self.health > 0):
	# 		return True
	# 	else:
	# 		return False

	# def attack(self, who):
	# 	who_to_attack.health -= self.power