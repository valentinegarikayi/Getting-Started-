#!/usr/bin/env python

#this is the solution to#
#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html#

import random
print ('Welcome to the Cows and Bulls Game')
count=0
finish = False
a = [random.randint(1,4) for i in range(4)]
#a = [1,2,3,4]
while finish == False:
	
	numb = input('Please guess a 4 digit number: ')
	b = [int(i) for i in numb]
	c = [] #this stores all the guesses
	for i in zip(a,b):
		if i[0] == i[1]:
			c.append('Cow')
		else:
			c.append('Bull')
	print(c)	
	count += 1
	if 'Bull' not in c:
		finish=True	

print('You guessed', count, 'times and the game is over')
