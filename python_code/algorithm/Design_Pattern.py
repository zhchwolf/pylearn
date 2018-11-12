#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 1. Factory Pattern for calculation
'''
class Operation():
    def getresult(self):
        pass

class OperationAdd(Operation):
    def getresult(self):
        return  self.op1 + self.op2

class OperationSub(Operation):
    def getresult(self):
        return  self.op1 - self.op2

class OperationMul(Operation):
    def getresult(self):
        return self.op1 * self.op2

class OperationDiv(Operation):
    def getresult(self):
        try:
            return  self.op1 / self.op2
        except:
            print("error:divided by zero!")
            return 0

class OperationUndef(Operation):
    def getresult(self):
        print("Undefine operation.")
        return 0

class OperationFactory:
    operation = {}
    operation['+'] = OperationAdd()
    operation['-'] = OperationSub()
    operation['*'] = OperationMul()
    operation['/'] = OperationDiv()
    def createoperation(self,ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op
if __name__ == "__main__":
    op = input("operation:")
    opa = float(input("a:"))
    opb = float(input("b:"))
    factory = OperationFactory()
    cal = factory.createoperation(op)
    cal.op1 = opa
    cal.op2 = opb
    print(cal.getresult())
'''
# 2. 策略模式
'''
class CashSuper:
    def acceptcash(self,money):
        return 0

class CashNormal(CashSuper):
    def acceptcash(self,money):
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self,ds):
        self.discount=ds
    def acceptcash(self,money):
        return money * self.discount

class CashReturn(CashSuper):
    total = 0
    ret = 0
    def __init__(self,t,r):
        self.total = t
        self.ret = r
    def acceptcash(self,money):
        if (money >= self.total):
            return money - self.ret
        else:
            return money

class CashContext:
    def __init__(self,csuper):
        self.cs = csuper
    def getresult(self,money):
        return self.cs.acceptcash(money)

if __name__ == "__main__":
    money =float(input("money:"))
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300,100))
    ctype = int(input("type:[1] for normal,[2] for 80% discount,[3] for 300-100."))
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print("Undefine type. Use normal mode.")
        cc = strategy[1]
    print("You will pay:%d" % (cc.getresult(money)))
'''
# 3.装饰模式

class Person:
    def __init__(self,tname):
        self.name = tname
    def show(self):
        print("Dressed %s" % (self.name))
class Finery(Person):
    componet = None
    def __init__(self):
        pass
    def decorator(self,ct):
        self.componet = ct
    def show(self):
        if (self.componet != None):
            self.componet.show()
class Tshirt(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Big T-shirt")
        self.componet.show()
class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Big Trouser")
        self.componet.show()
if __name__ == "__main__":
    p = Person("somebody")
    bt = BigTrouser()
    ts = Tshirt()
    bt.decorator(p)
    ts.decorator(bt)
    ts.show()

def fib(n):
    count = 0
    if n==1 or n==0:
        count = 1
    else:
        count = fib(n-2)+fib(n-1)
    return count

import time
start = time.time()
print ([fib(n) for n in range(40) ])
end = time.time()
print("cost:{}".format(end-start))

def fib2(n,cache = None):
    if cache is None:
        cache = {}
    if n in cache:
        return  cache[n]
    if n == 0 or n == 1:
        return 1
    else:
        cache[n] = fib2(n-2,cache) + fib2(n-1,cache)
    return cache[n]

# start1 = time.time()
# print(fib2(n) for n in range(20))
# end2 = time.time()
# print('cost:{}'.format(end2-start1))

# 爬楼梯
def climb (n,steps):
    count = 0
    if n<=1:
        count = 1
    else:
        for step in steps:
            count += climb(n-step,steps)
    return count
print(climb(5,[1,2]))

# 牛逼闪闪的装饰器
# 创建一个装饰器

def decorator(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@decorator
def decfib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return decfib(n-2)+decfib(n-1)

print(decfib(n) for n in range(10))

@decorator
def declimb(n,steps):
    count = 0
    if n<=1:
        count = 1
    else:
        for step in steps:
            count += climb(n-step,steps)
    return count

print(declimb(5,(1,2)))

