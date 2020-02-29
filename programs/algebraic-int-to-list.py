#!/usr/bin/env python3
import math

def orderOfMagnitude(i):
    return int(math.log(i,10))

def algebraic_int_to_list(a):
    if (a==0):
        return [0]
    rv=[]
    for i in range(orderOfMagnitude(a),-1,-1):
        nextDigit=math.floor(a/(10**i))
        rv.append(nextDigit)
        a -= nextDigit*10**i
    return rv

for i in range(0, 100, 1):
    print('{} => {}'.format(i, algebraic_int_to_list(i)))
