#!/usr/bin/python

import random

a = []
while (True):
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    if (a*a == b*b + c*c):
        print('({}, {}, {})'.format(a,b,c))

        
    
