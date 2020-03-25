#What is the largest prime factor of the number  ?
#N=600851475143
N=600851475143
def divisors(a):
    divlist=[]
    for i in range(1,a+1):
        if (a%i==0):
            divlist.append(i)

    return divlist

factors=[]
for i in range(N):
    if ( i in divisors(N))==True:
        factors.append(i)
    else:
        pass

def isPrime(x):
    return len(divisors(x))==2




print(max([i for i in divisors(N) if isPrime(i)==True]))
