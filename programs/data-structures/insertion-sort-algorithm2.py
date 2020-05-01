#!/usr/bin/env python3.7

def insertion_sort_algorithm(seq):
    n=len(seq)
    for i in range(1,n):
        value=seq[i]
        pos=i
        while value<seq[pos-1] and pos>0:
            temp=seq[pos]
            seq[pos]=seq[pos-1]
            seq[pos-1]=temp
            pos-=1
        seq[pos]=value
    return seq

print(insertion_sort_algorithm([5,4,3,2,1]))
