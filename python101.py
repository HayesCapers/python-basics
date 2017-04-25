# # print "Hello, World!"
# # print two things on the same line
# # print ("Hello, world", "Again")

# # print """ this 
# # will ignore line breaks
# # until python finds 
# # another three double quotes"""
# #  print "new thing"

# # python
# # Arithmatic
# # the_meaning_of_life = 40 + 2
# # print the_meaning_of_life
# # print the_meaning_of_life / 2
# # % returns the remainder after dividing
# # print the_meaning_of_life % 2
# # % returns the remainder after dividing

# # Data Types ( Variable types )
# # - Strings - English type stuff for peeople(in yellow)
# # - Numbers - something with digits and stuff that goes with digits (. -)
# # 	- Floats - Integers -
# # - Booleans - True or False. 1 or 0. yes or no. on or off.
# # - lists - list of variables in one variables
# # - dictionary - variables of variables 
# # - objects - deal w. this later

# #Strings
# # first_name = "Hayes"
# # last_name = "Capers"
# # print "Hello {} {}".format(first_name, last_name)

# # Placeholders
# # print "Hello %s %s" % (first_name, last_name)

# #  _Floats_
# # pi_the_magic_float = 3.14
# # print pi_the_magic_float
# # print type(pi_the_magic_float)
# # make_me_an_integer = int(pi_the_magic_float)
# # print make_me_an_integer

# # _Boolealns_
# # the_Truth = True 
# # the_Lie = False

# # _Raw_input_
# #  first_name = raw_input("First Name: ")
# #  print first_name
# # last_name = raw_input("Last Name: ")

# # _Conditionals_
# # 1 = mean you want to assign something
# # 2 == means you want to compare somethin on the left with something on the right

# # if(first_name == last_name):
# # 	print "Your first name is the same as your last name?"

# # age = raw_input("How old are you? ")
# # age_as_int = int(age)
# # # print type(age)
# # if(age_as_int >= 21):
# # 	print "You can buy beer."
# # else:
# # 	print "You CANNOT buy beer."

# # import random
# # random_number = random.randint(1, 10) #This include 1 AND 10
# # # print random_number

# # #_Loop___ keep doing something till i tell you to stop

# # not_guessed = True
# # while not_guessed: #== True
# # 	guess_a_number = raw_input("Guess a number between 1 and 10. ")
# # 	if (int(guess_a_number) == random_number):
# # 		print "You guessed the number!"
# # 		not_guessed = False


# #--------------LISTS----------------#

# students = [
# 	"Marissa",
# 	"Merliee",
# 	"Daniel",
# 	"Chris",
# 	"Chad", 
# 	"Shane",
# 	"Stephen",
# 	"Drew"
# ]

# #print students
# print(students[1])
# print(students[7])
# # print(students[8])
# print(students[-1])

# atlanta_teams = [
# 	"Falcons",
# 	"Braves",
# 	"Hawks",
# 	"Thrashers",
# ]

# print (atlanta_teams[0])
# #To add an element to the END of a list, you can use ".append()"
# atlanta_teams.append("Atl United")
# print atlanta_teams
# #To delete an index, you can use ".remove()"
# atlanta_teams.remove("Thrashers")
# print atlanta_teams
# #We can insert into any indicies with ".insert()"
# atlanta_teams.insert(0, "Toms Brady's Team")
# print atlanta_teams

# teams_as_a_string = "Falcons, Braves, Hawks, Thrashers"
# teams_as_a_list = teams_as_a_string.split(",")
# print teams_as_a_list
# atlanta_teams.sort()
# #.sort will CHANGE the array
# print atlanta_teams
# #sorted() will NOT change the array
# copy_of_atlanta_teams = sorted(atlanta_teams)
# print (copy_of_atlanta_teams)

# copy_of_atlanta_teams.reverse()
# print copy_of_atlanta_teams

# length_of_atlanta_teams = len(copy_of_atlanta_teams)
# print (length_of_atlanta_teams)
# print (copy_of_atlanta_teams[-1])


# #The other type of loop is the "for" loop
# # like a While loop but it increments the variable by 1 each thime through the loop
# #*** for [what you want to call the thing you are on] in [variable looping through]***
# for i in range(1, 10): #optional range(start, stop, step) "step" is the amount the loop will increment by each time through
# 	print i

# for student in students:
# 	if (student == "Chris"):
# 		print "Welcome, Chris."
# 	else:
# 		print "Youe are not chris"

# student_length = len(students)
# for i in range(0, student_length):
# 	print(students[i])

# 	# IF you want a portion of a list, you can use the "[x:y]" format
# 	# this will creat a copy of the array, does not nutate or change the origianl
# 	#it will start at the xth element, and stop at the yth
# print(students)
# second_and_third = students[1:3]
# print second_and_third
# print(students)
# all_but_the_first = students[1:]
# print all_but_the_first


##---------FUNCTIONS---------
 #A function is a piece of code that can be called from the main body of the program
 # the upshot is that if you have complicated code or code that is repeated often,
 # a function is your answer
 # repeating yourself is BAD
 # a function in python is not a function, it is a definition. 
 # to declare a function in python, you use "def"
 # function always have ()

# def say_hello():
# 	print ("Hello")

# say_hello()

#important examples

# def say_hello_with_name(name): #"name" is a local variable. It only exists while the function is running
# 	print ("Hello, " + name)

# # say_hello_with_name() #this will fail
# # say_hello_with_name("Hayes", "Capers") #this wil also fail
# say_hello_with_name("Hayes")

# def say_hello_with_default(name, in_class = "Yes"): #"in_class" is a default variable. so if no variable is passed in position it will return default
# 	print ("Hello, " + name)
# 	print "Is student in class? " + in_class

# say_hello_with_default("Hayes")

# def make_uppercase(string):
# 	return string.upper()

# normalized_string = make_uppercase("Im a wild and crazy guy")
# print normalized_string

##---------TUPLES---------

# lists are changeable... what if you want somethng that can't change?
# 	- A tuple is the same as a list in all ways, except:
# 		1. it cannot be changed
# 		2. it uses () instead of []

# tuple_test = (1, 5, 8)
# print tuple_test[1]
# tuple_test[1] = 6 # DOESN"T WORK!!!!! either use a list or dont change it!


##--------DICTIONARIES--------
# dictionaries are very simple objects.
# operate with a "key value pair"

# name = "Hayes"
# gender = "male"
# height = "tall"

# person = {
# 	"name": "Hayes"
# 	"gender": "male"
# 	"height": "tall"
# }

# print person("name")

# zombie = {}
# zombie["weapon"] = "axe"
# zombie['health'] = 100
# zombie['startX'] = 10
# zombie['satrtY'] = 20
# zombie['speed'] = 10

# print zombie

# for key,value in zombie.items():
# 	print "Zombie has a key of %s with a value of %s" % (key, value)
# 	print zombie[key]

# if (zombie[speed] <= 5):
# 	zombie[position] = zombie[startX] + 5
# elif (zombie[speed] > 10):
# 	zombie[position] = zombie['startX'] + 10
# else:
# 	zombie[position] = zombie['startX'] + 15


# zombies = []
# zombies.apped({
# 	'speed': 10,
# 	'weapon': 'fist',
# 	'name': 'Hank',
# 	})
# zombies.append({
# 	'speed': 5,
# 	'weapon': 'baseball bat',
# 	'name'; 'Bruiser'
# 	})

# print zombies[1]['victims'] = [
# 'Jane',
# 'Mike',
# 'Jones Family':{
# 	'father': 'Jim'
# 	}
# ]

# print (zombies[1]["victims"][1])



#//////////OOP//////////
#/OBJECT ORIENTED PROG/
#//////////OOP////////
# functions
# 	initial overhead is veery high. 
# Portable
# Reusable
# Organized

# ***Classes***
# classes = blueprint
# 	attributes = data
# 		- can be overwritten
# 		- methods
# objet = thing made from the blueprint
# 	- now has attributes of class 
			
# ***ENCAPSULATION***
#--look up on Wiki

#Example:

class Person(object):
	def __init__(self,name,gender,cell,number_of_arms = 2):
		self.name = name 
		self.gender = gender
		self.phone = {
			'cell': cell,
			'home': 'noone has a home phone'
		}
		self.species = "human" #no need to pass when creating obj because every person is a human
		self.number_of_arms = number_of_arms

	def greet(self, other_person):
		print "Hello %s, I am %s!" % (other_person, self.name)
	def print_contact_info(self):
		if (self.phone != ''):
			print "%s contact info is %s" % (self.name, self.phone['cell'])

hayes = Person("Hayes", "male", '404-641-0550')
print hayes.name
print hayes.gender
#to change species
hayes.species = "robot"
hayes.greet("Jerry")
hayes.print_contact_info()






































































