#!/usr/bin/python3
def length(words):
    count = 0
    for i in words:
        count += 1
    return count

def safe_print_list_integers(my_list=[], x=0):
    new = my_list[:x]
    val = []
    for i in new:
        if x <= length(new):
            try:
                print("{:d}".format(i), end='')
                val.append(i)
            except(TypeError, ValueError):
                pass
        else:
            raise IndexError
    print()
    return length(val)
