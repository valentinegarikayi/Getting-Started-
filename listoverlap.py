#!/usr/bin/env python

#this is the solution to
#http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random# random module imported here...is it?

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#print the overlap of both lists
for i in a and b:#this reads list a and b
    if i in a and b:#this is a condition to check both numbers-why not use equal?
        print(i)
#generate random lists and do the same thing
