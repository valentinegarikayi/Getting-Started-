#!/usr/bin/env python

#this is the solution to#
#http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html#

import random
a= [random.randint(1,4)for i in range(4)]#generates the random number
numb=[int(input('Please guess what number I am'))]#accepts the random number
c=[int(i) for i in str(numb)]#converts the number into a string


b=[]
