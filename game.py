def char_name():
	global name
	name = raw_input("What's your name, stranger?\n>")
	if name.isalpha() and len(name) > 2:
		print 'Okay, %s' % name
	elif len(name) < 2:
		print 'Name is too short.'
		char_name()
	else:
		print 'Not suspected characters used.'
		char_name()

def char_age():
	global name
	age = raw_input("How old are you, " + name + '?\n>')
	if age.isdigit():
		return age
		print 'Okay, %s' % name
	else:
		print ('Need to use integers, ' + name +'.')
		char_age()

def main_hall():
	global name
	choice = raw_input('Where will you go? left or right?')
	if choice == 'left':
		print 'You decided to go left..\n'
		lef_door()
	elif choice == 'right':
		print ('You decided to go right, ' + name + '.')
		right_door()
	else:
		print 'You did something wrong, %s' % name

def right_door():
	global name
	answer = False
	question = raw_input("What is in the middle of Paris?")
	if question == 'r':
		print 'Yor\'re good to go!'
		answer = True
	elif question.isdigit():
		print 'Answer should be in characters'
		right_door()
	elif len(question) > 2:
		print 'Here is a tip: length of answer is not so long, as you think.'
		right_door()
	else:
		print 'Unknow error'
		right_door()


def lef_door():
	global name
	print 'oops, it\'s not done yet..sorry %s' % name
	main_hall()



print '-'*45
print '\tWelcome to my \'game\''
char_name()
char_age()
main_hall()