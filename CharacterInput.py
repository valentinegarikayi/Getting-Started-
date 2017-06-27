#!/usr/bin/env python
import datetime
name = input('What is your name: ')
age = int (input ('What is your age: '))
d= datetime.datetime.today()# why does it repeat datetime? Is a function called by a variable?
century = d.year + (100-age)
message = ('Your name is '+ name,'you are',age,'years old and you will turn 100 years in',century)
numb= int(input('Please give me any number: '))
print (message*numb)
