N=600851475143
#N=60
def prime_fact(a):
    rv = None
    i = 2
    steps = 0
    while i<=a:
        steps += 1
        if a%i==0:
            rv = i
            a/=i
            while a%i==0:
                steps += 1
                a/=i
        i+=1
    return rv
print(prime_fact(N))
