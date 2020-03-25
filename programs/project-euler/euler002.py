#By considering the terms in the Fibonacci sequence whose values do not
#exceed four million
#find the sum of the even-valued terms.


a=1
b=1

fib=[]
fib.extend([a,b])
for i in range(2,4000000):

    i=fib[i-1]+fib[i-2]
    i++
fib.append(i)
fibeven=filter(lambda x:x%2==0,fib)
print(sum(fib))
