
sum=0
N = 10
a = 1
b = 1

for i in range(2, N):
    c=a+b
    a = b
    b = c
    if (c % 2 == 0):
        sum+=c

print('the result is: {}'.format(sum))
