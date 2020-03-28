#!/usr/bin/env python
#Find a positive integer that is divisible by both 11 and 12
counter =0
while True:
    if counter>=10:
        break
    counter = counter+1
    Ten_integers=int(input('Please enter an integer:'))
    if Ten_integers%2==0:
