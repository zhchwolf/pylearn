# coding:utf-8

import numpy as np

def num_diff(f,x):
    h= 10e-4
    print(h)
    return (f(x+h) - f(x)) / h

t = np.array([2.0,44.0,0.0,55.0])

def function_1(x):
    return 0.01*x**2 + 0.1*x

y = function_1(t)
a = num_diff(y,3.0)
print(a)

