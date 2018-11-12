#!/usr/bin/env python3
# ---- coding:utf8 ----

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names1880 = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'births'])
name_sum = names1880.groupby('sex').births.sum()
print(name_sum)
years = range(1880,2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'names/yob%d.txt' %year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
names = pd.concat(pieces, ignore_index=True)
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births.tail())
total_births.plot('Total births by sex and year')
plt.show()