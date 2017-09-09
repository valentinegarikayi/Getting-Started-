#!/usr/bin/env python

#this is the solution to#
#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html#

import random
print ('Welcome to the Cows and Bulls Game')#Welcome message
a = [random.randint(1,4) for i in range(4)] #generates the random number
#accepts the random number-this is defined as a variable
numb = input('Please guess a 4 digit number: ')
#converts the number into a list
b = [int(i) for i in numb]
c = [] #this stores all the guesses
count=0
if a != b:
	for i in zip(a,b):
		if i[0] == i[1]:
			c.append('Cow')
		else:
			c.append('Bull')
	print(c)
	count = count + 1
	print('You have guessed',count, 'times')
else:
	print('You guessed correctly and the game is over')
