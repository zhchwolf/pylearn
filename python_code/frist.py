#!/usr/bin/env python
# -*- coding: utf-8 -*-

# calculate the area and circumference of a circle from its radius
# Step 1: prompt for a radius
# Step 2: apply the area formula
# Step 3: print out the results

import math
radiusString = input('Enter radius of circle:')
radiusInt = int(radiusString)
circumference = 2*math.pi*radiusInt
print (circumference)
area = math.pi*radiusInt ** 2
print (area)
