#!/usr/bin/python
a=[]
b=[]
for i in range(1000):
    if (i%3==0):
        a.append(i)
        b.append(0)
    elif (i%5==0):
        b.append(i)
        a.append(0)
print(sum(map(lambda x,y: x+y, a, b)))
