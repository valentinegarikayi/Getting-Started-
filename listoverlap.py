#!/usr/bin/env python

#this is the solution to
#http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#print the overlap of both lists


for i in a and b: # this syntax seems legal but is redundant, you can just say 'for i in a'
    #this checks if i is in both lists but again is redundant, just say 'if i in b'
    if i in a and b:
        print(i)
        
#same thing in one line   
print set([i for i in a if i in b])

#generate random lists and do the same thing
a = [random.randint(1,10) for i in range(10)] #list comprehension
b = [random.randint(1,10) for i in range(10)]
