#!/usr/bin/env python

#this is the solution to#
#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html#

import random
print ('Welcome to the Cows and Bulls Game')#Welcome message
#a = [random.randint(1,4) for i in range(4)] #generates the random number
a = [1,2,3,4]
#accepts the random number-this is defined as a variable
numb = input('Please guess a 4 digit number: ') 

#converts the number into a string
b = [int(i) for i in numb] 
c = [] #this stores all the guesses

for i in zip(a,b):
	if i[0] == i[1]:
		print('1 Cow')
	else:
		print('1 Bull')

