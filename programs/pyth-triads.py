#!/usr/bin/python

#finding all Pythagorean Triads whose values do not exceed a certain number
a=[]
#print('tell me a number')
#N=input()

N = 20
for i in range(2,N+1):
    for j in range(2,N+1):
        for k in range(2,N+2):
            if i**2==j**2+k**2:
                global a
                a.append((i,j,k))
print(a)

print('There were {} Pythagorean Triads until the number you chose'.format(int(len(a)/2)))
