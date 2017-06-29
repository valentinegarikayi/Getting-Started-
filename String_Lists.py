#!/usr/bin/env python
#this is the solution to:
#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# here I attempt reversing the string using double colon and it works
user=input('Please give me a string:')
back =user[::-1]
if back==user:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
