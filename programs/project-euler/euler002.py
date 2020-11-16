#!/usr/bin/env python3.7

x=1
y=1
z=0
result=0

while z<4*(10**6):
    z=x+y
    if z%2==0:
        result+=z

    x=y
    y=z
    
print(result)
