#!/usr/bin/env python
#this is the solution to
#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# This program asks for a user to provide a number and then it print the divisors of the number

a = [int(input ('Please give me a number in range 1 to 100: '))]
b=[]
for i in a:
    if i % 1 ==0:
        b.append(i)
    if i % 2 ==0:
        b.append(i/2)
    if i % (i/2)==0:
        b.append(2)
    if i % 1 ==0:
        b.append(1)
print(b)
# I think there should be more concise code to append? Is there?
