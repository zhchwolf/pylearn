#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1.在字典中将键映射到多个值上面
from collections import defaultdict
import pandas

d = defaultdict(list)
print(d)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
d['b'].append(5)
d['b'].append(6)
print(d)
print(d.get("a"))
print(d.keys())
print([d.get(i) for i in d])

# 2.迅速转换字典键值对
data = {'a': 23, 'b': 45}
zip(data.values(), data.keys())
# data是我们的格式数据，使用zip后进行快速键值转换，然后可以使用max，min之类函数进行数据操作。

# 3.通过公共键对字典进行排序
from operator import itemgetter

data = [
    {'name': "bran", "uid": 101},
    {'name': "xisi", "uid": 102},
    {'name': "land", "uid": 103}
]
print(sorted(data, key=itemgetter("name")))
print(sorted(data, key=itemgetter("uid")))

# 4.对列表中的多个字典根据某一字段进行分组
# 注意注意，在进行分组前要首先对数据进行排序处理，排序字段根据实际要求来选择
rows = [
    {'name': "bran", "uid": 101, "class": 13},
    {'name': "xisi", "uid": 101, "class": 11},
    {'name': "land", "uid": 103, "class": 10}
]
some = [('a', [1, 2, 3]), ('b', [4, 5, 6])]
print(dict(some))

data_one = sorted(rows, key=itemgetter("class"))
print(data_one)
data_two = sorted(rows, key=lambda x: (x["uid"], x["class"]))
print(data_two)


# python实现折半查找和归并排序算法
def halfSearch(array, key, low, high):
    mid = int((low + high) / 2)
    if key == array[mid]:
        return array[mid]
    if low > high:
        return False
    if key < array[mid]:
        return halfSearch(array, key, low, mid - 1)
    if key > array[mid]:
        return halfSearch(array, key, mid + 1, high)

array = [4, 13, 27, 38, 49, 49, 55, 65, 76, 97]
res = halfSearch(array, 505, 0, len(array) - 1)
print(res)

def merge_sort(array):
    mid = int((len(array) + 1) / 2)
    if len(array) == 1:
        return array
    list_left = merge_sort(array[:mid])
    list_right = merge_sort(array[mid:])
    print(">>>list_left:", list_left)
    print(">>>list_right:", list_right)
    return merge(list_left, list_right)

def merge(list_left, list_right):
    final = []
    while list_left and list_right:
        if list_left[0] <= list_right[0]:
            final.append(list_left.pop(0))
        else:
            final.append(list_right.pop(0))
    return final + list_left + list_right

array = [49, 3543, 23, 45, 64, 984]
print(merge_sort(array))
