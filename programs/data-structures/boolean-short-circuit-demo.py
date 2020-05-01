#!/usr/bin/env python3.7

import random

def divides1000(n):
    return (n!=0) and (1000 % n == 0)


def keepOnlyDivisorsOf1000(alist):
    return filter(divides1000, alist)

'''
a = [random.randint(0, 250) for i in range(10**5)]

print(list(keepOnlyDivisorsOf1000(a)))
'''

def condition_a():
    print("evaluating condition a")
    return True

def condition_b():
    print("evaluating condition b")
    # raise Exception("foo")
    return True

def condition_c():
    print("evaluating condition c")
    return False

print(condition_a() and condition_b() and condition_c())
