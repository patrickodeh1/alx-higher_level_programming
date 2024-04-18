#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = sum(x * y for x, y in my_list)
    total = sum(y for _, y in my_list)
    return num / total
