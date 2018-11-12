#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

def showTime(foo):
    start = time.time()
    end=time.time()
    print('run time is :%d' %(end - start))

@showTime
def foo():
    print('The function is runnig.')
    time.sleep(1)


foo()