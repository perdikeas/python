result=0
a=1
b=1
N=10
for i in range(N-2):
    temp=a+b
    a=b
    b=temp
#    print(temp)
    if temp%2==0:
        result+=temp
print(result)
