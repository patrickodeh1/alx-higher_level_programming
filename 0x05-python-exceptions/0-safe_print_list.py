#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new = my_list[:x]
    num = 0
    for i in new:
        num = i
        try:
            print("{}".format(i), end='')
        except (ValueError):
            pass
    print()
    return num
