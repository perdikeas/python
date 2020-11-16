#!/usr/bin/env python3.7

def int_to_list(x):
    str_x=str(x)
    return[str_x[i] for i in range(len(str_x))]

def is_list_palindrome(list):
    for i in range(len(list)):
        if  not list[i]==list[len(list)-1-i]:
            return False
    return True

def is_int_palindrome(int):
    list=int_to_list(int)
    if is_list_palindrome(list):
        return True
    else:
        return False

current_largest_palindrome=0
for i in range(1000):
    for j in range(i,1000):
        if is_int_palindrome(i*j) and i*j>current_largest_palindrome:
            current_largest_palindrome=i*j

print("The largest palindrome number made up of the sum of 3 digit numbers is: {}".format(current_largest_palindrome))
