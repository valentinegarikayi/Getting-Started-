#!/usr/bin/env python

#a=[input('Eneter an element: ')for i in range(5)]
a=[4,6,7,8,3,4,6,1]

b=[]
for i in a:
    if not i in b:
        b.append(i)

print (b)
#sorted version of b
print (sorted(b))

