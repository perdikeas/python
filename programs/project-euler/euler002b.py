#!/usr/bin/env python3.7
N=4000000

def prepareFib(N):
    fib = []
    for i in range(N):
        if (i<=1):
            fib.append(1)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib


fib = prepareFib(N)

print(sum(filter(lambda x:x%2==0, fib)))
