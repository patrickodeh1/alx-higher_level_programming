#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if sys.argv[2] == '+':
            sum_all = cal.add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} + {} = {}".format(sys.argv[1], sys.argv[3], sum_all))
        elif sys.argv[2] == '-':
            subtract = cal.sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} - {} = {}".format(sys.argv[1], sys.argv[3], subtract))
        elif sys.argv[2] == '*':
            multiply = cal.mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} * {} = {}".format(sys.argv[1], sys.argv[3], multiply))
        elif sys.argv[2] == '/':
            divide = cal.div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} / {} = {}".format(sys.argv[1], sys.argv[3], divide))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
