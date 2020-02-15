#!/usr/bin/python

i = 0

def fib(n):
    global i
    i += 1
    if (i%100 == 0):
        print('trying to calculate fib({})'.format(n))
    if (n<=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)


N = 30
try:
    print('the {}-th term of the Fibonacci sequence is {}'.format(N, fib(N)))
except RuntimeError:
    print('oops, it looks like we reached maximum recursion depth')
