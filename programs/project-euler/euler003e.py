#!/usr/bin/env python3.7
import math
N=600851475143

def non_trivial_divisors(x):
    rv=[]
    for i in range(2,math.ceil(math.sqrt(x))):
        if x%i==0:
            rv.append(i)
    return rv

def is_prime(x):
    if len(non_trivial_divisors(x))==0:
        return True
    return False

def largest_prime_factor(x):
    divs=non_trivial_divisors(x)
    current_largest=None
    for i in range(2,math.ceil(math.sqrt(x))):
        if i in divs and is_prime(i):
            current_largest=i
    return current_largest

print(largest_prime_factor(N))
