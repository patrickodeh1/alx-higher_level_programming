#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    n = len(sys.argv)
    for count in range(1, n):
        sum += int(sys.argv[count])
    print("{}".format(sum))
