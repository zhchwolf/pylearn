#!/usr/bin/python

b = 1
def fun(b):
    b = 2
fun(b)
print (b)

def foo(x):
    print ("executing foo(%s)"%(x))
 
class A(object):
    def foo(self,x):
        print ("executing foo(%s,%s)"%(self,x))
 
    @classmethod
    def class_foo(cls,x):
        print ("executing class_foo(%s,%s)"%(cls,x))
 
    @staticmethod
    def static_foo(x):
        print ("executing static_foo(%s)"%x)


def is_unique_char(string):
    str_len = len(string)

    if str_len > 256:
        return True
    for pos in range(str_len):
        for index in range(pos-1,str_len):
            if string[pos] == string[index]:
                return False
    return True

s='student'
b=is_unique_char(s)
print (b)

def is_unique_char2(string):
    if len(string)>256:
        return True
    record = [False]*256
    for ch in string:
        ch_val = ord(ch)
        if record[ch_val]:
            return False
        record[ch_val] = True
    return True

s2='qwersdfpui,xcnv'
b2=is_unique_char2(s2)
print (b2)

def is_unique_char3(string):
    if len(string) > 256:
        return True
    record = 0

    for ch in string:
        print (record)
        ch_val = ord(ch)
        
        if (record & (1 << ch_val)) > 0:
            return False
        
        record |= (1 << ch_val)
    
    return True

s3='qwersdfpuii,xcnv'
b3=is_unique_char2(s3)
print (b3)

def is_unique_char4(string):
    if len(string) > 256:
        return True

# def fib():
#     prev,curr = 0,1
#     

import dis
x = [1,2,3]
dis.dis('for _ in x: pass')

from itertools import count
counter = count(start=13)
print (next(counter))
#从一个有限序列中生成无限序列：
from itertools import cycle
colors = cycle(['red','white','blue'])
print (next(colors))
#从无限的序列中生成有限序列：
from itertools import islice
colors2 = cycle(['red','white','blue'])
limited = islice(colors2,0,4)
for x in limited:
    print(x)

#自定义一个迭代器，以斐波那契数列为例：
class Fib:
    def __init__(self):
        self.prev=0
        self.curr=1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value
f=Fib()
print(list(islice(f,0,10)))

#生成器来实现斐波那契数列的例子是：
def fib2():
    prev,curr = 0,1
    while True:
        yield curr
        prev,curr = curr,curr+prev

f2= fib2()
print(list(islice(f2,0,10)))
