N=9
M=399
def gcd(_a,_b):
    a=max(_a,_b)
    b=min(_a,_b)
    if (a*b!=0):
        return gcd(b,a%b)
    return max(a,b)
print(gcd(N,M))
