from hero import Hero
from goblin import Goblin
from Vampire import Vampire
from random import randint

hero_name = raw_input('What is your name? > ')
the_hero = Hero(hero_name)
# the_goblin = Goblin()
monsters = []
# monsters.append(Goblin())
# monsters.append(Vampire())
monster_selector = [Goblin(), Vampire()]

print 'Welcome brave %s, you have encountered a goblin' % the_hero.name
print 'How many enemies are you willing to fight?'
number_of_enemies = int(raw_input('> '))
for i in range(0, number_of_enemies):
	monsters.append(monster_selector[randint(0,1)])
print monsters
for monster in monsters:
	while monster.health > 0 and the_hero.is_alive():
		print "%s has %d health and %d power." % (the_hero.name, the_hero.health, the_hero.power)
		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
		print "What do you want to do?"
		print "1. fight goblin"
		print "2. do nothing"
		print "3. flee"
		print "4. Drink liquor."
		print "> ",
		user_input = raw_input()

		if user_input == '1':
			monster.take_damage(the_hero.power)
			print "%s does %d damage to the %s" % (the_hero.name, the_hero.power, monster.name)
			if monster.health <= 0:
				print "you have defeated the %s!" % monster.name
				the_hero.xp += monster.xp_value
				the_hero.check_level()
		elif user_input == '2':
			pass
		elif user_input == '3':
			print 'Goobye coward.'
			break
		elif user_input == '4':
			the_hero.increase_health(20)
		else:
			print 'Ivalid input %s' % user_input

		if (monster.health > 0):
			the_hero.health -= monster.power
			print 'The goblin hit you for %d damage' % monster.power
			if the_hero.health <= 0:
				print "You are dead."

		if the_hero.is_alive() and the_hero.health < 5: 
			print 'You have gone into a rage. Your power has increased!'
			the_hero.power += 3