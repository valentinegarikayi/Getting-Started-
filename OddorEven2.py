#!/usr/bin/env python
num = int(input('Give me the number to check: '))
check =int(input('Give me the number to divide: '))
if num % check ==0:
    print ('{} divides evenly into,{}'.format(check, num))
else:
    print ('{} doesnt divide evenly into,{}'.format(check, num))
