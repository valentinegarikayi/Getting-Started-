#!/usr/bin/env python

#this is the solution to
#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = []
for i in a:
    if i<5:
        x.append(i)

print x

#same answer in one line
x = [i for i in a if i<5]
print x
