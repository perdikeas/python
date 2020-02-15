N=18
M=63
def gcd(_a,_b):
    a=max(_a,_b)
    b=min(_a,_b)
    while (a*b!=0):
        c=a%b
        a=b
        b=c

    return (b if a==0 else a)

print(gcd(N,M))
