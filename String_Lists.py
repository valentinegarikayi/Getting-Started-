#!/usr/bin/env python
#this is the solution to:
#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# here I attempt reversing the string using double colon and it works
user=input('Please give me a string:')
back =user[::-1]
print(back)
# here I attempt reversing the string using reverse() and it doesnt work
user=input('Please give me a string:')
user.reverse()
print(user)
