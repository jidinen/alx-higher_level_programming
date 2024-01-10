#!/usr/bin/python3
def weight_average(my_list=[]) -> float:
    """commnet"""
    if not my_list:
        return 0
    sum = 0
    total = 0
    average = 0
    for counter in my_list:
        element = counter[0]
        element2 = counter[1]
        result = element * element2
        sum = sum + result
        total = total + element2
    average = sum/total
    return average
