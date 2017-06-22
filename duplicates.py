#!/usr/bin/env python

#a=[input('Eneter an element: ')for i in range(5)]
a=[4,6,7,8,3,4,6,1]

b=[]
for i in a:
    if not i in b:# I need an explanation of what this does...my question is because it seems b is nil and we are testing
        b.append(i)

print (b)
#sorted version of b
print (sorted(b))
