#!/usr/bin/python3
def no_c(my_string):
    cpy = ''.join([x for x in my_string if x != 'C' and x != 'c'])
    return cpy
