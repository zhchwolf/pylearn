#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xdrlib
import sys
import xlrd
import xlsxwriter
import openpyxl
import xlwings as xw
import pandas as pd
import numpy as np

# wb = xw.Book() # Creates a connection with a new workbook
# xw.Range('A5').value = 'Foo 1'
# xw.Range('A5').value
# a = [1,2]
# a.extend([5])
# print(a)

# 打开文件
test = xw.Book('Shift.xlsx')

#Range的用法
xw.Range('A1').value = 'MD劳动工时统计表'
xw.Range('A1')
xw.Range('A1:C3')
xw.Range((1,1))
xw.Range((1,1),(3,3))
xw.Range(xw.Range('A1'), xw.Range('B2'))
#圆括号是1-based取法， 而方括号是0-based取法，xlwings遵循app到book到sheet的层次
xw.apps[0].books[0].sheets[0].range('A1')
xw.apps(1).books(1).sheets(1).range('A1')
xw.apps[0].books['Shift.xlsx'].sheets['4-1'].range('A1')
xw.apps(1).books('Shift.xlsx').sheets('4-1').range('A1')
#range本身也能切片，只是要记住，range[]里面仍然是0-based.
rng = xw.Book().sheets[0].range('A1:D5')
print(rng[0,0])
# <Range [Workbook1]Sheet1!$A$1>
print(rng[1])
# <Range [Workbook1]Sheet1!$B$1>
print(rng[1:3,1:3])
# <Range [Workbook1]Sheet1!$B$2:$C$3>
#不用range也一样
sht = xw.Book().sheets['Sheet1']
print(sht['A1'])
print(sht['A1:B5'])
print(sht[0,1].value)
# 给列赋值是多个方括号，给行赋值是直接的[1,2,3,4,5]
sht = xw.Book().sheets[0]
sht.range('A1').value = [[1],[2],[3],[4],[5]]
print(sht.range('A1:A5').value)
sht.range('A1').options(transpose=True).value = [1,2,3,4]
sht.range('A1').value = [1,2,3,4,5]
print(sht.range('A1:E1').value)
# 一般来说单个单元格返回的数值是float型，如果让它返回list型可以这样做
sht.range('A1').options(ndim=1).value
sht.range('A1:A5').options(ndim=2).value
#也会把每个格子的值作为list放在一个list中返回，其中2是作为list，1是作为float
sht.range('A1:E1').options(ndim=2).value
#然而，对一行的value返回值居然是list中间包含了一个大list
# [[1.0,2.0,3.0,4.0,5.0]] ndim选项 number of array dimensions是这个选项的意思，用来控制你输入的列表内元素维度
#xlwings是这样看待orientation的，每次在大方框下面，同一个小方框是同一行的数据，而另一个方框则是换行了
sht.range('A1').value = [[1,2],[3,4]]
#A1,B1赋值，然后换行到A2，B2赋值
#np的eye应该是实现几阶的单元矩阵，然后在range的option下面np.array实际上是convert的选项，就是希望用array的方式来显示
sht.range('A1').value = np.eye(3)
sht.range('A1').options(np.array, expand='table').value
# array([[1.,2.,0.],
#        [0.,0.,4.],
#        [0.,0.,7.]])
type(sht.range('A1').options(np.array, expand='table').value)
#发现输出是array对象。不是数值的list
###DataFrame相关
df = pd.DataFrame([[1.1,2.2],[3.3,None]], columns=['one','two'])
print(df)
sht.range('A1').value = df
print(sht.range('A1').value)  # why None？
print(sht.range('A1:C3').options(pd.DataFrame).value)
# 这里读出来是一个dataframe格式，如果你直接用range。value来读取，会连带index和columns一起读出来
#options：work for read and writing
sht.range('A5').options(index=False).value = df
# 后面会看到index在读取和写入的作用不同
sht.range('A9').options(index=False, header=False).value = df
#变成这样，用range.value就可以读出数据，应该控制了index和columns读不读
