#!/usr/bin/pythons
# -*- coding:utf-8 -*-

flist = []
for i in range(3):
    def func(x): return x * i
    flist.append(func)
for f in flist:
    print(i)
    print (f(2))
#444

flist3 = []
for k in range(3):
    def func(x, k=k): # the *value* of k is copied in func() environment
        return x * k
    flist3.append(func)
for p in flist3:
    print (p(2))
#024

def greet(msg,*args,**kwargs):
    if msg:
        print(msg)
    else:
        print("error")
greet(0j)
greet("ni hao!")

a = 10

def b():
    pass
class c:
    pass
obj = c()
print (isinstance(a,(int,str)))
print (isinstance(a,(float,str)))
print (isinstance(b,(str,int)))
print (isinstance(obj,(c,int)))
#isinstance 和 type的区别在于:对于subclass之类的type就不行了，所以,强烈建议不要使用type判断对象类型。

import math
def way(a,b,c):
    if(a==0):
        print("这就不是一个一元二次方程")
    if(b**2-4*a*c<0):
        print("无可行解")
    elif(b**2-4*a*c==0):
        print("有两个相同的根")
        #print("x1=x2=%d"%((-b)/(2*a)))
        #return(x1,x2)
    else:
        print("有两个不同的实数根")
        x1=(math.sqrt((b**2-4*a*c))-b)/(2*a)
        x2=-(math.sqrt((b**2-4*a*c))+b)/(2*a)
        #print("x1:",x1,"x2:",x2)
        return(x1,x2)

print(way(14,23,1))

#理解迭代的意义
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
#n=int(input('请输入汉诺塔的层数：'))
n=3
hanoi(n,'x','y','z')

a=set(["a","b","c","a"])
print(a)

filetest = open("file.txt", "w+")
filetest.write("python 编程语言可以用到很多地方")
print ("文件是否关闭：", filetest.closed)
print ("文件模式：", filetest.mode)
print ("文件名称：", filetest.name)
#print ("是否强制在末尾加空格：", filetest.softspace)
filetest.close()
print ("文件是否关闭：", filetest.closed)
filetest=open("file.txt","r+")
strs=filetest.read()
print(strs)

import os
import time
#1.Thefilesanddirectoriestobebackeduparespecifiedinalist.
source=['"C:\\MyDocuments"', 'E:\\learn\\Python\\pythonNote']
#Notice we had to use double quotes inside the string for names with spaces in it.
#2.The backup must be stored in a main backup directory
target_dir='E:\\Backup'#Remember to change this to what you will be using
#3.The files are backedup into a zipfile.
#4.The name of the zip archive is the current date and time
target=target_dir+os.sep+time.strftime('%Y%m%d%H%M%S')+'.zip'
#5.We use the zip command to put the files in a zip archive
zip_command="zip -qr {0} {1}".format(target,' '.join(source))
#Runthebackup
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

