#!/usr/bin/python

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = [i for i in range(1, 9)]


rv = []


for x in a:
    for y in b:
        rv.append( (x,y) )

print(rv)
