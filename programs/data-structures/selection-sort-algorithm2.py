#!/usr/bin/env python3.7

def selection_sort_algorithm(seq):
    n=len(seq)
    for i in range(n):
        current_min=i
        pos=i
        for j in range(i+1,n):
            if seq[j]<seq[current_min]:
                current_min=j
            if seq[current_min]!=seq[i]:
                temp=seq[i]
                seq[i]=seq[current_min]
                seq[current_min]=temp
    return seq


#testing
print(selection_sort_algorithm([8,6,3,-4,2,11,9,0,-5]))
