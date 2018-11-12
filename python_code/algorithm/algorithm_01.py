#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 后缀表达式求值
# 计算一个表达式时，编译器通常使用后缀表达式，这种表达式不需要括号.

operators = {
    '+': lambda op1,op2: int(op1) + int(op2),
    '-': lambda op1,op2: int(op1) - int(op2),
    '*': lambda op1,op2: int(op1) * int(op2),
    '/': lambda op1,op2: int(op1) / int(op2)
}

def evalPostfix(e):
    """
    :param e: 后缀表达式
    :return:  正常情况下栈内的第一个元素就是计算好之后的值
    """
    tokens = e.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        elif token in operators.keys():
            f = operators[token]
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f(op1,op2))
    return stack.pop()
result = evalPostfix('2 3 4 * +')
print(result)

# 背包问题
# 有一个背包能装10kg的物品，现在有6件物品分别为：
# 物品名称	重量
# 物品0	1kg
# 物品1	8kg
# 物品2	4kg
# 物品3	3kg
# 物品4	5kg
# 物品5	2kg
# 编写找出所有能将背包装满的解，如物品1+物品5。
def knapsack(t,w):
    """
    :param t: 背包总容量
    :param w:物品重量列表
    :return:
    """
    n = len(w)  # 可选的物品数量
    stack = []  # 创建一个栈
    k = 0  # 当前所选择的物品游标
    while stack or k < n:  # 栈不为空或者k<n
        while t > 0 and k < n:   # 还有剩余空间并且有物品可装
            if t >= w[k]:   # 剩余空间大于等于当前物品重量
                stack.append(k)  # 把物品装备背包
                t -= w[k]  # 背包空间减少
            k += 1  # 继续向后找
        if t == 0:  # 找到解
            print('物品编号：',stack)
        # 回退过程
        k = stack.pop() # 把最后一个物品拿出来
        t += w[k]  # 背包总容量加上w[k]
        k += 1   # 装入下一个物品

knapsack(10, [1, 8, 4, 3, 5, 2])

# 小东和三个朋友一起在楼上抛小球，他们站在楼房的不同层，假设小东站的楼层距离地面N米，球从他手里自由落下，每次落地后反跳回上次下落高度的一半，并以此类推知道全部落到地面不跳，求4个小球一共经过了多少米？(数字都为整数)
# 给定四个整数A,B,C,D，请返回所求结果。
# iuput: 100,90,80,70 return: 1020

def ballpath(high):
    total = 3*sum(high)
    return total

sumPath = ballpath([100, 90, 80, 70])
print(sumPath)

# 一条长l的笔直的街道上有n个路灯，若这条街的起点为0，终点为l，第i个路灯坐标为ai，每盏灯可以覆盖到的最远距离为d，为了照明需求，所有灯的灯光必须覆盖整条街，但是为了省电，要是这个d最小，请找到这个最小的d。
# 每组数据第一行两个整数n和l（n大于0小于等于1000，l小于等于1000000000大于0）。第二行有n个整数(均大于等于0小于等于l)，为每盏灯的坐标，多个路灯可以在同一点。
def mind(n, l, s):
    s = sorted(s)
    print(s)
    print(max([s[i+1]-s[i] for i in range(len(s)-1)])/2)
mind(7,15,[15,5,3,7,9,14,0])


