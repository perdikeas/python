N=50



def erato(N):
    def sievePreparation(N):
        sieve = []
        for i in range(N+1):
            sieve.append(True)
        sieve[0]=False
        sieve[1]=False
        return sieve

    def sieveToList(sieve):
        rv=[]
        for i in range(len(sieve)):
            if sieve[i]==True:
                rv.append(i)
        return rv

    sieve = sievePreparation(N)
    p=2
    while p<=N:
        if sieve[p]==True:
            for i in range(2*p,N+1,p):
                sieve[i]=False
        p+=1
    return sieveToList(sieve)

print(erato)

print(erato(N))
