#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum = 0
    size = 0
    for score, weight in my_list:
        sum += score * weight
        size += weight
    return sum / size
