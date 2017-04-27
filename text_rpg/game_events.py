import time
from random import randint
# class Menu(object):
# 	def main_menu(self, hero, battle_object):
# 		while True:
# 			print '----------------------------------------'
# 			print '-Welcome %s. What would you like to do?-' % hero.name
# 			print '----------------------------------------'
# 			time.sleep(1.5)
# 			print '1. Check pokemon status'
# 			print '2. Explore the tall grass'
# 			print '3. Visit Pokemart'
# 			print '4. Visit Pokemon Center'
# 			print '5. Visit Gym'
# 			print '6. Give up on the dream of becoming a pokemon Master.'
# 			input = int(raw_input('> '))

# 			if input == 1:
# 				hero.pokemon_status()
# 			# elif input == 2:
# 			elif input == 2:
# 				battle_object.wild_battle(hero, )


class Potion(object):
	cost = 5
	name = 'potion'
	
	

class Pokeball(object):
	cost = 5
	name = 'Pokeball'

	


# class Pokemart(object):
class Main_menu(object):
	def main(self, hero, wild_pokemon, battle_engine):
		while True:
			print '\n\n\n\n\n'
			print '----------------------------------------'
			print '-Welcome %s. What would you like to do?-' % hero.name
			print '----------------------------------------'
			time.sleep(1.5)
			print '1. Check pokemon status'
			print '2. Explore the tall grass'
			print '3. Visit Pokemart'
			print '4. Visit Pokemon Center'
			print '5. Visit Gym'
			print '6. Give up on the dream of becoming a pokemon Master.'
			input = int(raw_input('> '))

			if input == 1:
				hero.pokemon_status()
			# elif input == 2:
			elif input == 2:
				battle_engine.wild_battle(hero, wild_pokemon)
			elif input == 6:
				break


class Battle(object):
	def wild_battle(self, hero, enemy):
		pokemon = hero.current_pokemon[0]
		print '\n///////////////////////////////////////////////////'
		print '///////////////A Wild %s Appeared/////////////////' % enemy.name
		print '/////////////////////////////////////////////////'
		time.sleep(1.5)
		print '\n%s sends %s into battle.\n' % (hero.name, pokemon.name)
		while pokemon.alive() and enemy.alive():
			pokemon.print_status()
			print ""
			enemy.print_status()
			print '////////////////////////////////////////'
			print ''
			print 'What will you do?' 
			print '1. Attack %s' % enemy.name
			print '2. Switch pokemon'
			print '3. Use potion'
			print '4. Attempt to capture'
			print '5. FLEEEEE!!'
			input = int(raw_input('> ')) 
			if input == 1:
				pokemon.attack(enemy)
			elif input == 2:
				hero.switch_pokemon()
				pokemon = hero.current_pokemon[0]
			elif input == 4:
				hero.capture(enemy)
				print hero.current_pokemon
				break
			elif input == 5:
				print "%s got away safely..." % hero.name
				break
			else:
				print 'invalid input'
				pass
			enemy.attack(pokemon)
			if not pokemon.alive():
				hero.switch_pokemon()
			
					


		

			# elif input == 2:

