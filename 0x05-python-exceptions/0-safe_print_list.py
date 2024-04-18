#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new = my_list[:x]
    for i in new:
        try:
            print("{}".format(i), end='')
        except:
            pass
    print()
    return len(new)
