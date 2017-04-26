# Write code to do the following:

# 1.Print Elizabeth's phone number.
# 2.Add a entry to the dictionary: Kareem's number is 938-489-1234.
# 3.Delete Alice's phone entry.
# 4.Change Bob's phone number to '968-345-2345'.
# 5.Print all the phone entries.

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print (phonebook_dict['Aldice'])
phonebook_dict['Kareem'] = '968-345-3245'
phonebook_dict.pop('Alice')
phonebook_dict['Bob'] = '968-345-2345'
print phonebook_dict.values()



# 1.Write a python expression that gets the email address of Ramit.
# 2.Write a python expression that gets the first of Ramit's interests.
# 3.Write a python expression that gets the email address of Jasmine.
# 4.Write a python expression that gets the second of Jan's two interests.

# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     {
#       'name': 'Jasmine',
#       'email': 'jasmine@yahoo.com',
#       'interests': ['photography', 'tennis']
#     },
#     {
#       'name': 'Jan',
#       'email': 'jan@hotmail.com',
#       'interests': ['movies', 'tv']
#     }
#   ]
# }

# print ramit['email']
# print ramit['interests'][0]
# print ramit['friends'][0]['email']
# print ramit['friends'][1]['interests'][1]


# Write a letter_histogram function that takes a word as its input, 
# and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the word. 
# For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}

# word_input = list(raw_input('Type a word: '))
# empty_dict = {}

# for i in word_input:
# 	if i in empty_dict:
# 		empty_dict[i] += 1
# 	else:
# 		empty_dict[i] = 1

# print empty_dict

# empty_dict_para = {}


# def para_hist(paragraph):
# 	paragraph_list = paragraph.split(" ")
# 	for i in paragraph_list:
# 		if i in empty_dict_para:
# 			empty_dict_para[i] += 1
# 		else:
# 			empty_dict_para[i] = 1
# 	return empty_dict_para

# print para_hist("To be or not to be that is the question")

empty_dict = {}
# import operator

def letter_histogram(word):
	word_list = list(word)
	for i in word_list:
		if i in empty_dict:
			empty_dict[i] += 1
		else:
			empty_dict[i] = 1
	return empty_dict


full_dict = letter_histogram('helloworld')
# print full_dict














# while (full_dict.keys() > 3):
# 	for i in full_dict:
# 		if (full_dict.value([i]) <= full_dict.value([i+1])):
# 			full_dict.pop([i])
# 		else:
# 			full_dict.pop([i + 1])

#Doesnt Work
# def histogram_sort(dictionary):
# 	dict_list = list(dicitonary)
# 	for i in dict_list:
# 		if (i[1] >= (i[1] + 1)):
# 			dict_list.pop[i+1]
# 		else:
# 			dict_list.pop[i]

# print histogram_sort(full_dict)











# top_three = dict(sorted(empty_dict.iteritems(), key = operator.itemgetter(1), reverse = True) [:3])
# print top_three
# print sorted(top_three, reverse = True)












