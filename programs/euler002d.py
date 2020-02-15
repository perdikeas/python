a=10
def prepareFibonacci(a):
    fib=[]
    for i in range(a):
        if i<=1:
            fib.append(1)
        else:
            fib.append(fib[-1]+fib[-2])
    return(fib)
fib=prepareFibonacci(a)
print(sum(filter(lambda x:x%2==0,fib)))
