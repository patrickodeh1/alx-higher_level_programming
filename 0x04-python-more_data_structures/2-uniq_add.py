#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_elements = set()
    total = 0
    for i in my_list:
        if i not in uniq_elements:
            uniq_elements.add(i)
            total += i
    return total
