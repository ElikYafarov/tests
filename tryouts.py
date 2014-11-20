import random

list_of = []
greeting = '\nWelcome to auto-dash-length test.\n \'0\' - back to menu'


def length_test():
	choice_2 = None
	while choice_2 != '0':
		choice_2 = raw_input('\nType some words or sentence to check dashes auto length.\n\n')
		if len(choice_2) > 50:
			print 'Too long, sorry'
		else:
			choice_dash = '\t' + len(choice_2) * '-'
			print '%s\n\t%s\n%s' % (choice_dash, choice_2, choice_dash)
	start()

def list_test():
	choice = None
	while choice != '0':
		print '\n\t0 - exit'
		print '\t1 - add number'
		print '\t2 - show the list'
		print '\t3 - delete number'
		print '\t4 - sort numbers'
		print '\t5 - reverse numbers'
		print '\t6 - add random number'
		print '\t7 - show random number'
		print '\t8 - clear the list'
		print '\tq - back to main menu\n'
		choice = raw_input('Select number.\n\n>>')

		if choice == '1':
			try:
				number = int(raw_input('Type the number you want to add.\n'))
				list_of.append(number)
			except:
				print 'Numbers have to be used.'

		elif choice == '2':
			print list_of[:]

		elif choice == '3':
			number = int(raw_input('Type the number you want to delete.\n'))
			if number in list_of:
				list_of.remove(number)
				print "Succesfully deleted ", number, " from your list."
			else:
				error =  "\nThe number %d is not in the list.\n" % number
				dash = len(error) * '-'
				print '\n%s\nThe number %d is not in the list.\n%s\n' % (dash, number, dash)
		elif choice == '4':
			list_of.sort()
			print 'Succesfully sorted.'
		elif choice == '5':
			list_of.reverse()
			print 'Succesfully reverted.'
		elif choice == '6':
			list_of.append(random.choice(range(1000)))
			random_number = list_of[-1]
			print 'Succesfully added %s to the list!' % random_number # So great!
		elif choice == '7':
			try:
				print random.sample(list_of[:], 1) # So great!
			except:
				print 'Maybe there is no numbers in the list?'
		elif choice == '8':
			list_of = []
			print 'Succesfully removed all items!'
		elif choice == 'q':
			start()

def start():
	global greeting
	where = raw_input('\n1 for dashes test. 2 for list test.\n')
	if where == '1':
		print 'working.\n'
		print greeting
		length_test()
	elif where == '2':
		print 'working.\n'
		list_test()
	else:
		print 'No easter here..'
		start()

start()
