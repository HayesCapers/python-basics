import os

phonebook_data = {
	"Melissa": "404-235-5428",
	"Joe": "404-235-2125",
	"Mike": "770-134-2229",
	"Igor": "770-233-3461"
}


# name = raw_input('>')
# print phonebook_data["name"]
# phonebook_data = [
#     {
#         "name": "Melissa",
#         "number": "404-235-5428"
#     },
#     {
#         "name": "Joe",
#         "number": "404-235-2125"
#     },
#     {
#         "name": "Mike",
#         "number": "770-134-2229"
#     },
#     {
#         "name": "Igor",
#         "number": "770-233-3461"
#     }
# ]

def look_up(userInput):
	for i in phonebook_data:
		if i == userInput:
			print phonebook_data[i]
		
#MAIN LOOP
while 1:
	print """Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)?
	"""

	user_input = raw_input("Enter Number: ")
	# if (user_input == '1'):
	try:
		convert_user = int(user_input)
	except ValueError:
		os.system("clear")
		print "You must enter a number!\n"
	else:
		if (convert_user == 1):
			search_name = raw_input("Enter name: ")
			look_up(search_name)
		elif (convert_user == 2):
			new_user_name = raw_input("Enter Name: ")
			new_user_number = raw_input("Enter Number: ")
			phonebook_data[new_user_name] = new_user_number
		elif (convert_user == 3):
			del_entry = raw_input('Enter Name: ')
			del phonebook_data[del_entry]
		elif (convert_user == 4):
			phonebook = list(phonebook_data)
			print str(phonebook)
		elif(convert_user == 5):
			break











