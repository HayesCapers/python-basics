# this is a procedural approach to a text based
# the hero is fighting a goblin
# he has the option to:
# 1. fight
# 2. run
# 3.


def main():
	hero_health = 10
	hero_power = 5
	goblin_health = 6
	goblin_power = 2

	while goblin_health > 0 and hero_health > 0:
		print "You have %d health and %d power." % (hero_health, hero_power)
		print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
		print "What do you want to do?"
		print "1. fight goblin"
		print "2. do nothing"
		print "3. flee"
		print "> ",
		user_input = raw_input('> ')
		if user_input == '3':
			print 'Goobye coward.'
			break

main()        	