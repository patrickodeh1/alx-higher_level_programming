#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new1 = my_list_1[:list_length]
    new2 = my_list_2[:list_length]
    new_list = []

    for a in range(list_length):
        try:
            mul = new1[a] / new2[a]
        except ZeroDivisionError:
            print("division by 0")
            mul = 0
        except TypeError:
            print("wrong type")
            mul = 0
        except IndexError:
            print("out of range")
            mul = 0
        finally:
            new_list.append(mul)

    return new_list
