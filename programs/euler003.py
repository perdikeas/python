#!/usr/bin/env python3
N=600851475143

def prime_fact(a):
    rv = None
    for i in range(2, N+1):
        if (a<i):
            break
        if a%i==0:
            rv = i
            a/=i
            while a%i==0:
                a/=i
    return rv

print(prime_fact(N))


