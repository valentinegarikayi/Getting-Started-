#!/usr/bin/env python

import datetime
name = input('What is your name: ')
age = int (input ('What is your age: '))
d = datetime.datetime.today() # datetime is the module, with a function of the same name being called
century = d.year + (100-age)
message = ('Your name is {}. You are {} years old and you will turn 100 years in {}.'.format(name,age,century))
numb = int(input('Please give me any number: '))
print (message)
