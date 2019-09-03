#!/usr/bin/env python3

import numpy as np
import matplotlib.pylab as plt

a = np.array([-1.0, 1.0, 3.0])
b = a > 0
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


def step_function_02(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function_02(x)
plt.plot(x, y)
plt.ylim(-0.1,1.1)
plt.show()


def sigmoid(x):
    return 1/(1 + np.exp(-x))


x1 = np.array([-1.0,1.0,2.0])
print(sigmoid(x1))

t = np.array([1.0, 2.0, 3.0])
print(1.0/(1.0 + t))

t = np.array([1.0, 2.0, 3.0])
1.0 + t
print(t)
t = 1.0 / t
print(t)

x2 = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x2)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()


def relu(x):
    return np.maximum(0,x)


x3 = np.array([1,2])
print(x3.shape)
w = np.array([[1,3,5],[2,4,6]])
print(w.shape)
y = np.dot(x3,w)
print(y)


def identify_function(x):
    return x


def softmax(a):
    exp_a =np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


def softmax_c(a):
    c = max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([0.3, 2.9, 4.0])
print(softmax(a))
print(sum(softmax(a)))

