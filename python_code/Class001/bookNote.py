#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python 基础教程 （第二版）

# 数据和表达式
print (1/2)
print (1.0/2.0)
print (10//2.0)
print (1%2)
print ((-3)**2)
a1 = 12352345634552345656345 * 23432452342 + 23
print (a1)

#16进制和8进制 0x 和 0
# 变量
_rule = "rule information" 
#最好以_开头,能够说明变量的含义

# 类名首字母大写
# 私有实例变量以"__"
# 方法首字母小写，后面每个单词的首字母大写。
class Student:
    """docstring for Class Student"""
    __name = ""
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.__name
if __name__ == '__main__':
    student = Student("borphi")  #对象名小写
    print (student.getName())

# 函数中的命名规则
import random

def compareNum(num1, num2):
    if (num1 > num2):
        return 1
    elif(num1 == num2):
        return 0
    else:
        return -1
num1 = random.randrange(1,9,2)
num2 = random.randrange(1,9,2)
print ("num1 =", num1)
print ("num2 =", num2)
print (compareNum(num1,num2))


#字符串（‘’，“”）
#列表和元组（序列，列表list，元组tuple）
#字典
#条件和循环
#抽象（函数，参数魔法，作用域，递归）
#类（多态，封装，继承）
#异常
#魔法方法，属性和迭代器
'''
1.神马是函数？
函数可以尽量的解决程序员编程中的一种的算法的重复使用的问题
2.调用函数。
（1）可以直接使用help（abs）函数来了解abs的用法。所以要学会使用help（）函数
'''
'''print(abs(100))
print(abs(-20))
print(abs(12.34))
#由以上可知abs（）函数便是取绝对值得函数abs（）
#由于该函数只能有一个参数，当你多加入参数的时候，就会出错,如下：
 print(abs(-89,-27))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
'''
'''
（2）cmp（）函数。
cmp（x，y）用以比较x和y的大小 ，当x=y的时候，返回值为0.
                            ，当x>y的时候，返回值为正值（通常为1）.
                            ，当x<y的时候，返回值为负值（通常为-1）.
（3）int（）函数。
int（x）：用以将其它数据类型，转换为整型。
'''
#sum（）函数接受一个list作为参数，并返回list所有元素之和。请计算1*1+2*2+3*3+4*4+。。。。+100*100
'''
#这便是一个函数，用以计算你输入数的前n项和。
num=int(input("please input a number:"))
n=0
for i in range(num):
      n+=num
      num-=1
print(n)
'''
'''
（4）str（）函数就是把其它类型转换为str（）类型。
a=str(123)
print(a)
print(type(a))
'''
'''4.编写函数
在，python中定义一个函数要使用到def（）语句，依次写出函数名，括号，括号中的参数和冒号；然后再缩进块中编写函数体
，函数的返回值用return语句返回。
我们以一个函数为例
def my_abs(x):
    if(x>0):
        return x
    else:
        return -x
num=int(input("please input your number:"))
print(my_abs(num))
#这便就是一个自定义函数的使用过程。注意：函数体内再执行的时候，一旦执行到return语句，函数就执行完毕，并将结果返回。
因此函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后，也会返回结果，只是结果为None
'''
'''4.返回多值。
函数可以返回多个值吗？答案是肯定的。
比如在游戏中，需要从一个点移动到另一个点，给出坐标，位移和角度，就可以计算出的目标。
#MATH包提供了sin（）和cos（）函数，我们先用import引用它：
'''
'''import math
def move(x,y,step,angle):
    nx=x+step+math.cos(angle)
    ny=y-step+math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)'''
'''
一元二次方程的定义是：ax^2+bx+c=0,试编写一个函数，返回一元二次方程的两个解。
注意:python中math函数包括了sqrt（）函数用以计算平方根。
'''
#这就是，用python来实现的一元二次方程的解法。

import math
def way(a,b,c):
    if(b**2-4*a*c<0):
        print("无可行解")
    elif(b**2-4*a*c==0):
        print("有两个相同的根")
        print("x1=x2=%d"%((-b)/(2*a)))
    else:
        print("有两个不同的实数根")
        print("x1=%d,x2=%d"%(((-b)+b**2-4*a*c)/(2*a)),((-b)-b**2-4*a*c)/(2*a))
print(way(1,2,1))

#问题出现，如何进行有两个根的方程计算结果，   print("x1=%d,x2=%d"%(((-b)+b**2-4*a*c)/(2*a)),((-b)-b**2-4*a*c)/(2*a))
# 这行代码很明显有一些问题。故明早修改。
'''
5,递归函数。
在函数内部可以调用其它函数，如果一个函数可以在内部调用自身本身，这个函数就是递归函数。
举个例子：
n!=1*2*3*.....*n
若用个函数表示则为fact（n）=n*（n-1）*.....*1,且只有当n=1时需要特殊处理。
'''
def fact(n):
    if(n<1):
        print("not allow")
    elif(n==1):
        print("fact=%d"%(1))
    else:
        m=1
        k=n
        for i in range(k):
            m*=n
            n-=1
        return m
print("fact:",fact(10))

#注意：无法实现阶乘？在进行下一步的调试。注意有汉诺塔的作业需要看一下子，并最好能够做出来。

'''
6,定义默认参数
例如，python中的int（）函数就是自带两个参数，我们既可以传一个参数，也可以传两个参数。
print(int("123"))
def power(x,n):
    print("x**n=%d"%(x**n))
print(power(3,2))
#可以直接计算x的n次方。也可指定n的具体取值，这样便可以实现计算x的幂级数了。
'''
'''作业：请定义一个greet（）函数，它包含一个默认参数，如果没有传入，打印“hello xxx”
'''
def greet(say="Hello null"):
    print(say)
print()
print("Hello pappi!")
'''
7,定义可变参数。
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：
def fn(*args):
print(args)
可变参数的名字前面有个*号，我们可以传0个，1个或多个参数，给可变参数。可变参数也不是很神秘，python解释器会把传入的一组参数组装成一个
tuple传递给可变参数，因此在函数内部，直接把arg看成一个tuple就好了。
定义可变参数的目的也是为了简化运算，假设我们要计算人一个数的平均值，我们就可以定义一个可变参数。
'''
'''作业，做一个求平均值的函数。（无论有多少个元素）
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    if a == 0:
        raise TypeError('a不能为0')
    if not isinstance(a,(int,float)) or  not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('Bad operand type')
    delta = math.pow(b,2) - 4*a*c
    if delta < 0:
        return '无实根'
    x1= (math.sqrt(delta)-b)/(2*a)
    x2=-(math.sqrt(delta)+b)/(2*a)
    return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))'''
'''import math
def way(a,b,c):
    if(a==0):
        print("这就不是一个一元二次方程")
    if(b**2-4*a*c<0):
        print("无可行解")
    elif(b**2-4*a*c==0):
        print("有两个相同的根")
        print("x1=x2=%d"%((-b)/(2*a)))
    else:
        print("有两个不同的实数根")
        x1=(math.sqrt((b**2-4*a*c))-b)/(2*a)
        x2=(math.sqrt(-(b**2-4*a*c))-b)/(2*a)
print(way(14,23,1))'''
#上面总是有问题，所以需要修改
'''学习python遇到的第一个问题：汉诺塔问题的实现。首先是不知道什么是汉诺塔问题，然后是不知道怎么实现。于是百度了下，结果如下：

汉诺塔：汉诺塔（又称河内塔）问题是源于印度一个古老传说的益智玩具。
大梵天创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上按照大小顺序摞着64片黄金圆盘。
大梵天命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。
并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘'''
#4.字典（dic）
#我们要找到名字对应的分数这件事是很困难的，所以我们引入了字典这一概念，我们把名字叫做”键（key），对应的成绩叫做值（value）。由于dict也是集合，len（）函数可
#以计算任意集合的大小。
#建立字典。
'''d={
    "wangshuai":95,
    "wangchuan":89,
    "wangyun":90
}
#花括号｛｝表示这是一个字典，然后按照key:value写出来即可。最后一个key:value的值可以省略。
print(len(d))
print(d.values())'''
'''#访问字典
d={
    "wangshuai":95,
    "wangchuan":89,
    "wangyun":90
}
print(d["wangshuai"])#注意：当访问字典的时候，必须要使d后面的括号为中括号【】否则会出错。
if "liuzhe" in d:
    print(d["liuzhe"])
else:
    print("don't have this people")'''
#dic的第一个特点
#dic的第一个特点就是速度快，不管有多少个key都是一样的速度，而list的速度随着元素的增加速度下降
#缺点，dic的缺点就是占用内存过大，会浪费很多内存，注意：由于dic中是按照key查找，所以key不可以重复。
#dic的第二个特点
#存储key-value序对是没有顺序的,及打印的顺序与创建的顺序是不同的，这可以说明dic内部是无序的。
'''d={
    "wangshuai":95,
    "wangchuan":89,
    "wangyun":90
}
print(d)'''
#dic的第三个特点就是
#key的元素不可改变，但是list的元素是可以改变的，就不可以作为key，最常用的key还是用字符串来作为key值的。
#更新dict
#dict是可变的，也就是说，可以随时往dict中添加key-value值，比如有dic：
'''d={
    "wangshuai":95,
    "wangchuan":89,
    "wangyun":90
}'''
#要把tom同学的成绩添加进去，即用
'''d["tom"]=72
print(d)'''
#如果这个键值（key）已经存在，就会替换它的值
#遍历dic
#由于dict也是一个集合，所以遍历dict和遍历list是类似的，都可以通过for循环来进行
#直接使用for循环可以遍历dict的键（key）：
d={
    "wangshuai":95,
    "wangchuan":89,
    "wangyun":90
}
for key in d:
    print(key)
#由于直接使用key可以获取对应的value，应此可以在循环体中直接，获取到value的值。

#5.set。
 
'''dic的作用是建立一组key和一组value的映射关系
dict的键值（key）是不可以重复的.
有的时候我们只想要dic的键值（key），并不需要key所对应的value值。目的就是保证这个集合的元素不会重复，这时set就派上了用场。
set持有一系列元素但和list不同的是,这些元素没有重复的，而且是无序的。这点和dic中的key很像。
创建set的方式为调用set（）函数并传入一个list，list的元素将作为set的元素.
'''
'''a=set(["a","b","c"])#无序性体现得淋漓尽致。
print(a)'''
'''a=set(["a","b","c","a"])#无序性体现得淋漓尽致。
print(a)
print(len(a))#连长度都只会是去掉重复的元素后的集合长度。'''
'''
2.访问set
由于set存储的是无序的元素，所以我们没法用访问索引的方式来访问元素。
访问一个元素用set，就是判断该元素否在set中存在。
'''
'''a=set(["alice","bloom","cook","alex"])#无序性体现得淋漓尽致。
print(a)
print("alex" in a)#可以直接判断元素是否在set集合中存在。'''
'''
3.set的特点：
（1）set的内部结构和dict很象，唯一不同的区别是不存储value的值，因此判断一个元素是否在set中的速度很快。
（2）任何可变对象都是不可以存放在set中的。
（3）set中的元素是无序的。
set的这些特点用在什么地方？
让用户输入星期，可以用set来判断用户输入是否正确。
'''
'''months=(["mon","tue","wed","tues","fri","sta","sun"])
x1="feb"
x2="sun"
if x1 in months:
    print("ok")
else:
    print("terror")
if x2 in months:
    print("ok too")
else:
    print("terror too")'''
'''
4,遍历set
由于set也是一个集合，所以遍历set和遍历list是一样的，都可以通过for循环实现。
直接使用for循环来实现遍历set
'''
'''a=(["adam","lisa","bart","wangshuai"])
for name in a:
    print(name)
#注意：由于set是无序的，所以for循环出来的结果在不同的电脑上可能是不同的。'''
'''
5.更新set。
（1）把元素添加到set中。
（2）把现有元素从set中删除。
'''
a=set([1,2,3])
a.add(4)
print(a)#实现在set中添加一个指定元素（但是位置不定）
a.remove(1)
print(a)#实现在set中删除一个指定元素（但是位置不定）
#但是要删除set中不存在的元素就会报错：所以一定要删除set中有的元素。
