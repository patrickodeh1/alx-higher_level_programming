#!/usr/bin/python3
def magic_calculation(a, b):
    import magic_calculation_102 as magic
    if a < b:
        c = magic.add(a, b)
        for i in range(4, 6):
            c = magic.add(c, i)
        return c
    else:
        return magic.sub(a, b)
