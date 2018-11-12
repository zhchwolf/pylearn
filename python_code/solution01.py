#!/usr/bin/python
# -*- coding:UTF-8 -*-
# python 入门经典以解决计算问题为导向的python编程实践

# a1 = input('input a number:')
a1 = 88
a2 = (( int(a1) + 2 )*3 -6 )/3
print ("((number+2)*3 -6)/3 The result is ",a2)

'''
我要去圣艾夫斯，我碰到一个男人，他有7个妻子，
每个妻子有7个麻袋，每个麻袋有7只猫，每只猫有7只小猫，
一共有多少人和物要去圣艾夫斯。
'''
all_object = 1 + 7 + 7*7 +7*7*7 + 7*7*7*7
print ('一共有',all_object,'人和物要去圣艾夫斯')

# Draw a 6-pointed star
import turtle

turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(-60)
turtle.forward(50)
turtle.done()

