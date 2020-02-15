#!/usr/bin/python


N = 20

triads = []
for a in range(1, N+1):
    for b in range(1, a):
        for c in range(1, b):
            if (a**2 == b**2 + c**2):
                triads.append( (a,b,c) )

print('There are {} triads up to {}. These are:'.format(len(triads), N))

for triad in triads:
    print(triad)


                

        
    
