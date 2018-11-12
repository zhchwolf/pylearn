#!/usr/bin/env python3

import random
import sys

'''tip01'''
__version_info__ = (1, 1, 1)
__version__ = '.'.join(map(str, __version_info__))
print(__version__)
'''
str   --encode--> bytes
bytes --decode--> str
type function:  encoding =[utf-8,gbk,...]
bytes(str1,encoding='utf-8')
str(bytes1,encoding='utf-8')
'''

f= open("d:\good_poem.txt",'r')
for i in f:
    print(i)

#print(random.seed())
L = [1,2,3]
L.extend([4,5,6])
L.append([7,8,9])
L.remove(L[6])
L.pop()
print(id(L[1]))
print(id(L[0]))
print(id(L))
kv = {'Sunday':1,'Monday':2,'Tuesday':3,'Wednesday':4,'Thursday':5,'Friday':6,'Saturday':7}
print(kv.keys())
print(kv.values())
print(kv.items())
print(dict(kv.items()))
print(list(kv.values()))

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

