#!/usr/bin/python
N=100
M=80
def divisors(a):
    divlist=[]
    for i in range(1,a+1):
        if (a%i==0):
            divlist.append(i)
    return divlist


def commonElements(la, lb):
    return [i for i in la if i in lb]


def commonElements2(la, lb):
    rv = []
    for x in la:
        if x in lb:
            rv.append(x)
    return rv


def cartesian(a, b):
    rv = []
    for x in a:
        for y in b:
            rv.append( (x,y) )
    return rv

def commonElements3(a, b):
    ab = cartesian(a, b)
    ab2 = filter(lambda x: x[0]==x[1], ab)
    ab3 = [i[0] for i in ab2]
    ab3_dad = map(lambda x:x[0] , ab2)
    return ab3_dad




def gcd(x,y):
     cdlist=commonElements3(divisors(x), divisors(y))

     return max(cdlist)

print(gcd(N,M))
