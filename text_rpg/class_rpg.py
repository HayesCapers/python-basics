from hero import Hero
from plant import Bulbasaur
from water import Squirtle
from fire import Charmander
from random import randint
                             
game_on = True                                                                            
user_first_time_in_game = True
pokemon_select = True
main_menu = True
current_pokemon = []

while game_on == True:
	while user_first_time_in_game == True:
		print """\nHello there! Welcome to the world of POKEMON! My name is OAK!
		People call me the POKEMON PROF! \n\nFirst, what is your name?""" 
		hero_name = raw_input('> ')
		the_hero = Hero(hero_name)

		print "\nRight! So your name is %s!\n\n" % the_hero.name
		print """%s! Your very own POKEMON legend is about to unfold! A world of
		dreams and adventures with POKEMON awaits! Let's go!""" % the_hero.name
		user_first_time_in_game = False


	while pokemon_select == True:
		print """\n\n\n...Now that I know evrything about you, It is time to pick your first pokemon.
		Here, %s! There are 3 POKEMON here! Haha! They are inside the
		POKE BALLS. When I was young, I was a serious POKEMON trainer.
		In my old age, I have only 3 left, but you can have one! Choose!
		1. Squirtle
		2. Charmander
		3. Bulbasaur
		""" % the_hero.name
		user_input = raw_input('>')

		if user_input == '1':
			print "So! You want Squirtle? (y/n)" 
			user_input = raw_input('> ')
			if user_input == 'y':
				print "Would you like to name Suirtle? (y/n)"
				user_input = raw_input('> ')
				if user_input == 'y':
					first_pokemon_name = raw_input('Enter name: ')
					first_pokemon = Squirtle(first_pokemon_name)
				else:
					first_pokemon = Squirtle()	
				current_pokemon.append(first_pokemon)
				pokemon_select = False
			elif user_input == 'n':
				pass
			else:
				print "Invalid input"
				pass	
		elif user_input == '2':
			print "So! You want Charmander? (y/n)" 
			user_input = raw_input('> ')
			if user_input == 'y':
				print "Would you like to name Charmander? (y/n)"
				user_input = raw_input('> ')
				if user_input == 'y':
					first_pokemon_name = raw_input('Enter name: ')
					first_pokemon = Charmander(first_pokemon_name)
				else:
					first_pokemon = Charmander()	
				current_pokemon.append(first_pokemon)
				pokemon_select = False
			elif user_input == 'n':
				pass
			else:
				print "Invalid input"
				pass	
		elif user_input == '3':
			print "So! You want Squirtle? (y/n)" 
			user_input = raw_input('> ')
			if user_input == 'y':
				print "Would you like to name Bulbasaur? (y/n)"
				user_input = raw_input('> ')
				if user_input == 'y':
					first_pokemon_name = raw_input('Enter name: ')
					first_pokemon = Bulbasaur(first_pokemon_name)
				else:
					first_pokemon = Bulbasaur()	
				current_pokemon.append(first_pokemon)
				pokemon_select = False
			elif user_input == 'n':
				pass
			else:
				print "Invalid input"
				pass
		else:
			print "Invalid input"
			pass	

	print "Congratulations! You now have your first pokemon. Say hello to your %s named %s." % (first_pokemon.type_name, first_pokemon.name)
	break

# while main_menu == True:
	


























# print 'How many enemies are you willing to fight?'
# number_of_enemies = int(raw_input('> '))
# for i in range(0, number_of_enemies):
# 	monsters.append(monster_selector[randint(0,1)])
# 	# monsters.append(monster_selector)


# for monster in monsters:
# 	monster.health = monster.max_health
# 	while monster.health > 0 and the_hero.is_alive():
# 		print "%s has %d health and %d power." % (the_hero.name, the_hero.health, the_hero.power)
# 		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
# 		print "What do you want to do?"
# 		print "1. fight goblin"
# 		print "2. do nothing"
# 		print "3. flee"
# 		print "4. Drink liquor."
# 		print "> ",
# 		user_input = raw_input()

# 		if user_input == '1':
# 			monster.take_damage(the_hero.power)
# 			print "%s does %d damage to the %s" % (the_hero.name, the_hero.power, monster.name)
# 			if monster.health <= 0:
# 				print "you have defeated the %s!" % monster.name
# 				the_hero.xp += monster.xp_value
# 				the_hero.check_level()
# 		elif user_input == '2':
# 			pass
# 		elif user_input == '3':
# 			print 'Goobye coward.'
# 			break
# 		elif user_input == '4':
# 			the_hero.increase_health(20)
# 		else:
# 			print 'Ivalid input %s' % user_input

# 		if (monster.health > 0):
# 			the_hero.health -= monster.power
# 			print 'The goblin hit you for %d damage' % monster.power
# 			if the_hero.health <= 0:
# 				print "You are dead."

# 		if the_hero.is_alive() and the_hero.health < 5: 
# 			print 'You have gone into a rage. Your power has increased!'
# 			the_hero.power += 3