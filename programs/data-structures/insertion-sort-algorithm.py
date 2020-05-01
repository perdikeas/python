#!/usr/bin/env python3.7

def insertion_sort_algorithm(seq):
    n=len(seq)
    for i in range(1,n):
        value=seq[i]
        pos=i

        while pos>0 and value<seq[pos-1]:
            seq[pos]=seq[pos-1]
            pos-=1

        seq[pos]=value
        
    return seq
print(insertion_sort_algorithm([5,4,3,2,1]))
