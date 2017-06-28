#!/usr/bin/env python
number = int(input("Please give me a number: "))
if number % 2 != 0:
    print ('The number you gave me is an odd number')
elif number % 4 ==0 and number % 2 ==0:
        print ('The number you gave me is even and a multiple of four git!')
else:
    print ('The number you gave me is an even number')
