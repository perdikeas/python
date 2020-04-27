#!/usr/bin/env python3.7



def binary_search(ordered_list,value):

    top=len(ordered_list)-1
    bottom=0

    middle=int((top-bottom)/2)

    while top!=bottom:

        if ordered_list[middle]==value:
            return middle

        elif ordered_list[middle]<value:
            bottom=middle+1

        else:
            top=middle-1

        if top==value:
            return top

        else:
            return -1

print(binary_search(list(range(10)),9))
