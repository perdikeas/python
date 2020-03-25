#!/usr/bin/env python3

import math

def intToList(x):
    rv=[]
    a=str(x)
    for i in range(len(a)):
        rv.append(a[i])
    return rv

def isPalindrome2(l):
    rv = True
    l_len = len(l)
    for i in range(0, math.floor(l_len/2)):
        if l[i]!=l[l_len-1-i]:
            rv=False
    return rv

def isPalindrome(l):
    l_len = len(l)
    for i in range(l_len-1, -1, -1):
        if l[i]!=l[l_len-1-i]:
            return False
    return True

def isPalindrome3(l):
    lReverse = l.copy()
    lReverse.reverse()
    return l == lReverse

def isIntPalindrome(i):
    return isPalindrome(intToList(i))


print (isIntPalindrome([]))
print (isIntPalindrome([3]))
print (isIntPalindrome([4,4]))
print (isIntPalindrome([4,5,4]))

if True:
    for i in range(0, 1000, 1):
        print(i, intToList(i), isIntPalindrome(i))

rv=[]
computations = 0
for i in range(0, 1000):
    for j in range(i1, 1000):
        computations += 1
        if (isIntPalindrome(i*j)==True):
            if i*j not in rv:
                rv.append(i*j)

print( "answer after trying {} pairs is {}".format(computations, max(rv)))
