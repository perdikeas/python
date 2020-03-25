#!/usr/bin/env python3
def intToList(a):
    b = str(a)
    return [b[i] for i in range(len(b))]



def isPalindrome1(l):
    l1=l.copy()
    l1.reverse()
    return l==l1

def isPalindrome2(l):
    for i in range(len(l)-1,-1,-1):
        if l[i]!=l[len(l)-1-i]:
            return False
    return True

def isPalindrome3(l):
    for i in range(len(l)):
        if l[len(l)-i-1]!=l[i]:
            return False
    return True

def isIntPalindrome(palindromeDetector, i):
    return palindromeDetector(intToList(i))

palindromeDetectors = [isPalindrome1, isPalindrome2, isPalindrome3]

overallResult = None
for palindromeDetector in palindromeDetectors:
    rv=[]
    for i in range(1000):
        for j in range(i,1000):
            if isIntPalindrome(palindromeDetector, i*j)==True:
                rv.append(i*j)
    result = max(rv)
    if overallResult == None:
        overallResult = result
    else:
        if result != overallResult:
            raise Exception('shit happened. I was expecting result to be {}, yet it was {}'.format(overallResult, result))

print(overallResult)
