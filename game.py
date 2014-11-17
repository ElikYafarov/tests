gold_key = False
tries_right = 0
dash = '-'*45

def char_name():
	global name
	name = raw_input("\nWhat's your name, stranger?\n>")
	if name.isalpha() and len(name) > 2:
		print '\nOkay, %s' % name
	elif len(name) < 2:
		print '\nName is too short.'
		char_name()
	else:
		print '\nNot suspected characters used.'
		char_name()

def char_age():
	global gold_key
	global name
	global age
	age = raw_input("\nHow old are you, " + name + '?\n>')
	if age.isdigit():
		print 'Okay, %s' % name
		age = int(age)
		if age > 120:
			print 'INSANITY, %s, INSANITY' % name
			print 'Okay...it\'s just a game..'
		elif age > 70:
			print 'you are pretty old fuck!!'
	else:
		print ('\nNeed to use integers, ' + name +'.')
		char_age()

def main_hall():
	global name
	global gold_key
	choice = raw_input('\nWhere will you go? left or right?\n')
	if choice == 'left':
		print '\nYou decided to go left..\n'
		lef_door()
	elif choice == 'right':
		print ('\nYou decided to go right, ' + name + '.\n')
		print dash + dash
		print ' You are entering great hall with red carpets and strange portraits on walls.'
		print 'In the end of the hall you noticed only one little door, with picture of eiffel sticked on it.'
		print 'Room is filled with pastel light, you can smell expesive perfume in the air.'
		print 'Young lady is sitting near the sealed window, reading something and drinking cofee..'
		print 'Without any attention to you she asked:'
		right_door()
	else:
		print '\nYou did something wrong, %s' % name
		print 'left or right, nothing too difficult.'
		main_hall()

def right_door():
	global tries_right
	global name
	global gold_key
	print dash
	if gold_key == True:
		print dash + dash
		print '\nYoung lady said:\n"Please, leave me alone.\n'
		print '\tYou have already cleared this room!'
		main_hall()
	question = raw_input("What is in the middle of Paris?\n\t")
	if question == 'r':
		print dash + dash
		print '\n\tYoung lady sitting there is wondering how smart you was.'
		print '\tShe gave you a little golden key'
		print '\tYou cleared this room. You can visit another one.\n\t *clap clap*'
		gold_key = True
		main_hall()
	elif question.isdigit():
		print dash
		print '\nAnswer should be in characters'
		right_door()
	elif tries_right > 20:
		print dash
		print 'Okay..the answer contains 1 letter'
		tries_right +=1
		print tries_right
	elif tries_right > 15:
		print dash
		print '\nWake me up when you\'re done here.. %d' % tries_right
		tries_right +=1
		right_door()
	elif tries_right > 10:
		print dash
		print '\nUhm..you\'re dumb'
		tries_right += 1
		right_door()
	elif tries_right > 5:
		print dash
		print '\nIt seems to me that you stuck.. Try to think different.\n'
		print '\tCounting your tries.. \'%d\'' % tries_right
		tries_right += 1
		right_door()
	elif len(question) > 2:
		print dash
		tries_right += 1
		print '\nHere is a tip: length of answer is not so long, as you think.'
		print '\tYou made %d of tries.\n' % tries_right
		right_door()
	else:
		print '\nUnknow error'
		tries_right += 1
		right_door()

def lef_door():
	global name
	global gold_key
	global age
	print dash
	if age > 40 and gold_key == False:
		print 'Hmm..even you are %s years old, you\'re wise and expirienced,' % age
		print 'but i can\'t let you in without a golden key..'
	elif gold_key == False or age < 30:
		print '\n\tOh, sorry buddy, but you don\'t have a golden key..'
		main_hall()
	elif gold_key == True:
		print 'Welcome, my friend!'
		print '\n\n\t\tWORK IN PROGRESS\n\n'
		print 'It means, that i\'m not finished here yet.'
	else:
		print 'Don\'t know how you get here, %s' % name
		lef_door()
	main_hall()

def game_start():
	print '\n\n\n'
	print dash + '\n'
	print '\tWelcome to nameless game!\n\nYou will travel trhough',
	print 'several chambers and will get some challanges.'
	print 'To quit, press \'CTRL+C\' any time'
	raw_input('Press enter to continue..')
	char_name()
	char_age()
	main_hall()

game_start()
