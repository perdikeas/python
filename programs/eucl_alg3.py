from random import randint
N=9
M=399
def gcd(a,b):
    a=max(_a,_b)
    b=min(_a,_b)
    def innerGcd(a,b):
        assert(b<=a)
        if (a*b!=0):
            return innerGcd(b,a%b)
        return a;
    return innerGcd(a, b)

a = [randint(0, 1000) for i in range(200)]
b = [randint(0, 1000) for i in range(200)]


ab = zip(a,b)
for x in ab:
    assert( gcd(x[0], x[1]) == gcd(x[1], x[0]) )
    assert( gcd(x[0], 1 ) == 1)
    assert( gcd(x[1], 1 ) == 1)


print(gcd(N,M))
                        
