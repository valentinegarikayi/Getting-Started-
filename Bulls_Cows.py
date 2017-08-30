#!/usr/bin/env python

#this is the solution to#
#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html#

import random
print ('Welcome to the Cows and Bulls Game')#Welcome message
a= [random.randint(1,4)for i in range(4)]#generates the random number
numb=int(input('Please guess what number I am: '))#accepts the random number-this is defined as a variable
#DF please explain why it couldnt traverse is as a list
b=[int(i) for i in str(numb)]#converts the number into a string
c=[]#this stores all the guesses
for x in a:
    if x in a and b:
        print('1 Cow')
    else:
        print('1 Bull')
