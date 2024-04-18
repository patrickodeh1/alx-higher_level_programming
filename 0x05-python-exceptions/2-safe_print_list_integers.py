#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    new = my_list[:x]
    val = []
    for i in new:
        if x <= len(my_list):
            try:
                print("{:d}".format(i), end='')
                val.append(i)
            except(TypeError, ValueError):
                pass
        else:
            raise IndexError
    print()
    return len(val)
