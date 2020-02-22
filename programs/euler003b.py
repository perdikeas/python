N=600851475143

def prime_fact(a):
    rv = None
    i = 2
    while (i <= N):
        if (a<i):
            break
        if a%i==0:
            rv = i
            a/=i
            while a%i==0:
                a/=i
        i += 1
    return rv

print(prime_fact(N))


