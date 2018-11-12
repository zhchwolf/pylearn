#!/usr/bin/env python3
# -*- coding:utf8 -*-

def getvalue( init_value, square_value):
    looplist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in looplist:
        chang_value = init_value + str(i)
        if float(chang_value) * float(chang_value) > square_value:
            chang_value = init_value + str(i-1)

            break
    return chang_value

v = getvalue('1.', 2)
print(v)

def get_radication(precision=1):
    init_value = '1.'
    for n in range(1, precision):
        init_value = getvalue(init_value, 2)
    return init_value

res = get_radication(15)
print(res)

