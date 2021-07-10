#!/usr/bin/env python3

l = [1,2,2,3,1,4,-1,7]

stats = {}

def incr_freq(x):
    global stats
    if x not in stats:
        stats[x]=0
    stats[x]+=1

def compute_freq(l):
    global stats
    for x in l:
        incr_freq(x)


def solution(l, thres):
    global stats
    compute_freq(l)
    allowed_key_value_tuples = filter(lambda x: x[1]<thres, stats.items())
    allowed_keys = [x[0] for x in allowed_key_value_tuples]
    return filter(lambda x : x in allowed_keys, l)

print(list(solution(l, 2)))
