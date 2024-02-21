# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:50:47 2024

@author: syed.hussain

def is_even(n):
    return n%2==0
    
num_1=[2,3,4,5,6,8,9,4,11]

even_num =list(filter(is_even,num_1))
print(even_num)

"""
num_1=[2,3,4,5,6,8,9,4,11]

even_num =list(filter(lambda n:n%2==0,num_1))
print(even_num)

def update(n):
    return n*2

double = list(map(update, even_num))
print(double)


double = list(map(lambda even_num: even_num *2, even_num))
print(double)



from functools import reduce
def add_all(a,b):
    return a+b

sum = reduce(add_all, double)
print(sum)



sum = reduce(lambda a,b:a+b, double)
print(sum)



