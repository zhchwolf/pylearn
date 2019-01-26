#!/usr/bin/env python3

import numpy as np

a = np.array([-1.0,1.0,3.0])
b = a>0
print(b)
print(b.astype(np.int))

def step_function(x):
    if x>0:
        return 1
    else:
        return 0

def step_function_01(x):
    y= x>0
    return y.astype(np.int)

import matplotlib.pylab as plt
def step_function_02(x):
    return np.array(x>0, dtype=np.int)

x = np.arange(-5.0,5.0,0.1)
y = step_function_02(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()