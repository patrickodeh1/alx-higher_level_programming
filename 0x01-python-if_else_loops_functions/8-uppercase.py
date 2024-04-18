#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            res += chr(ord(i) - 32)
        else:
            res += i
    print("{}".format(res))
