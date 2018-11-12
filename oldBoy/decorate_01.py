#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
def logger(flag):
    def showTime(func):
        def inner(*x ,**y):
            start = time.time()
            func(*x,**y)
            end=time.time()
            print('run time is :%s' %(end - start))
            if flag == 'true':
                print('print log...')
        return inner
    return showTime

@logger('true')
def foo():
    print('The function1 is runnig.')
    time.sleep(1)

@logger('false')
def bar():
    print('The function2 is runnig.')
    time.sleep(2)

@logger('True')
def addFunc(*args,**kwargs):
    sum = 0
    for x in args:
        sum += x
    print(sum)

foo()
bar()
addFunc(1,2,3,4,5)