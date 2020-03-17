#!/usr/bin/env python3

def difference_between(x,y):
    return abs(y-x)

def difference_with_golden_ratio(x,y):
    if x*y==0:
        raise Exception('impossible values (x,y)=({},{})'.format(x,y))
    else:
        return difference_between( (x+y)/max(x,y),max(x,y)/min(x,y))

rv=1
total_steps = 55
for i in range(1, total_steps):
    if difference_with_golden_ratio(i,total_steps-i)< difference_with_golden_ratio(rv,total_steps-rv):
        rv=i

golden = (1 + 5 ** 0.5) / 2
steps_below_tier = max(rv, total_steps-rv)
steps_above_tier = min(rv, total_steps-rv)
print(('\n\n\tThe {} steps in the Epidaurus amphitheatre should be\n'+
'\tdivided by a tier as {} and {} ({} below the\n'
+'\ttier, {} above the tier) to be as close\n'+
'\tas possible to the Golden Ratio ({})\n\n').format(total_steps
, steps_below_tier
, steps_above_tier
, steps_below_tier
, steps_above_tier
, golden))
