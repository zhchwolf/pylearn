#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

n = 0
i = 0
for n in range(1001):
    if n%3 == 0 or n%5 == 0:
        print(n%3)
        i = i+n
print(i)

