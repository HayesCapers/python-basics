# print "Hello, World!"
# print two things on the same line
# print ("Hello, world", "Again")

# print """ this 
# will ignore line breaks
# until python finds 
# another three double quotes"""
#  print "new thing"

# python
# Arithmatic
# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2
# % returns the remainder after dividing
# print the_meaning_of_life % 2
# % returns the remainder after dividing

# Data Types ( Variable types )
# - Strings - English type stuff for peeople(in yellow)
# - Numbers - something with digits and stuff that goes with digits (. -)
# 	- Floats - Integers -
# - Booleans - True or False. 1 or 0. yes or no. on or off.
# - lists - list of variables in one variables
# - dictionary - variables of variables 
# - objects - deal w. this later

#Strings
# first_name = "Hayes"
# last_name = "Capers"
# print "Hello {} {}".format(first_name, last_name)

# Placeholders
# print "Hello %s %s" % (first_name, last_name)

#  _Floats_
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# print make_me_an_integer

# _Boolealns_
# the_Truth = True 
# the_Lie = False

# _Raw_input_
#  first_name = raw_input("First Name: ")
#  print first_name
# last_name = raw_input("Last Name: ")

# _Conditionals_
# 1 = mean you want to assign something
# 2 == means you want to compare somethin on the left with something on the right

if(first_name == last_name):
	print "Your first name is the same as your last name?"

age = raw_input("How old are you? ")
age_as_int = int(age)
# print type(age)
if(age >= 21):
	print "You can buy beer."