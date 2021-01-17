#!/usr/bin/env python3
l=[1,2,3,3,4,6,6,9]

def compute_freq_of_each_elem(l):
    dict={}
    for i in l:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
    return dict


def solution(l, n):
    freqs = compute_freq_of_each_elem(l)
    return list(filter(lambda x: freqs[x]<=n, l))

print(solution(l,1))
