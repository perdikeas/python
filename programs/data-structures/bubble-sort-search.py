#!/usr/bin/env python3.7


import random

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'



def bubble_sort(seq):

    n=len(seq)
    steps = 0
    try:
        for i in range(n-1):
            flip_occured=False    
            for j in range(n-i-1):
                steps += 1
                if seq[j]>seq[j+1]:
                    flip_occured=True
                    initial_seq_j=seq[j]
                    seq[j]=seq[j+1]
                    seq[j+1]=initial_seq_j
            if (not flip_occured):
                return
    finally:
        print('{} steps'.format(steps))


print(Color.RED+'Note, we sort the sequence in ascending order, that is from lowest to highest number'+Color.END)
print("\n\n\n\n\n")

a = [1,2,3,4,5]
bubble_sort(a)
print(a)
b = [1,2,3,5,4]
bubble_sort(b)
print(b)
c = [5,4,3,2,1]
bubble_sort(c)
print(c)
d = [random.randint(1, 10) for i in range(10**3)]
bubble_sort(d)
print(d)

