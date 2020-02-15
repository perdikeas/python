N=54
M=6
def gcd(_a,_b):
    a=max(_a,_b)
    b=min(_a,_b)
    while a*b!=0:
        c=a%b
        a=b
        b=c
    return max(a,b)
print(gcd(N,M))
