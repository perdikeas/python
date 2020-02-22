#N=600851475143
N=60
def prime_fact(a):
    rv=[]
    for i in range(2,a+1):
        if a%i==0:
            rv.append(i)
            a/=i
            while a%i==0:
                rv.append(i)
                a/=i
        i+=1
    return rv
print(prime_fact(N))
