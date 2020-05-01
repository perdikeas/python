#!/usr/bin/env python3.7

def selection_sort_algorithm(seq):
    n=len(seq)

    for i in range(n-1):
        current_min=i
        for j in range(i+1,n):
            if seq[j]<seq[current_min]:
                current_min=j

        if current_min!=i:
           temp=seq[i]
           seq[i]=seq[current_min]
           seq[current_min]=temp

    return seq

print(selection_sort_algorithm([5,4,3,2,1]))
