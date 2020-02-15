def gcd(a,b):
    print('entering gcd({}, {})'.format(a,b))
    if (a<b):
        return gcd(b,a)
    else:
        if (a*b==0):
            return max(a,b)
        else:
            return gcd(b, a%b)


print(gcd(15,100))
