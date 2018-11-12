# /usr/bin/python
# -*- coding = utf-8 -*-

from functools import reduce

print ('\n'.join([''.join([('Zhangyue'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') \
    for x in range(-30,30)])for y in range(15,-15,-1)]))

print ('\n'.join([''.join(['*'if abs((lambda a:lambda z,c,n:a(a,z,c,n))(lambda s,z,c,n:z if n==0 else s(s,z*z+c,c,n-1)) (0,0.02*x+0.05j*y,40)) else' 'for x in range(-80,20)])for y in range(-20,20)]))

print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))

print (*(i for i in range(2, 1000) if all(tuple(i%j for j in range(2, int(i**.5))))))  

print ([x[0] for x in [  (a[i][0], a.append((a[i][1], a[i][0]+a[i][1]))) for a in ([[1,1]], ) for i in range(100) ]])
print(reduce ( lambda x,y:x*y,  range(1,10)))

#print ((lambda i:i not in [1,2] and "Invalid input!" or i==1 and (lambda f:f<-459.67 and "Invalid input!" or f)(float(input("Please input a Celsius temperature:"))*1.8+32) or i==2 and (lambda c:c<-273.15 and "Invalid input!" or c)((float(input("Please input a Fahrenheit temperature:"))-32)/1.8))(int(input("1,Celsius to Fahrenheit\n2,Fahrenheit to Celsius\nPlease input 1 or 2\n"))))
#"".join((lambda x:(x.sort(),x)[1])(list(‘string’)))
qsort = lambda arr: len(arr) > 1 and  qsort(filter(lambda x: x<=arr[0], arr[1:] )) + arr[0:1] + qsort(filter(lambda x: x>arr[0], arr[1:] )) or arr


# def guess_my_number(n):
#     while True:
#         user_input = input("Enter a positive integer to guess: ")
#         #user_input = '10'
#         if len(user_input)==0 or not user_input.isdigit():
#             print ("Not a positive integer!")
#         else:
#             user_input = int(user_input)
#             if user_input > n:
#                 print ("Too big ! Try again!")
#             elif user_input < n:
#                 print ("Too small ! Try again!")
#             else:
#                 print ("You win!")
#                 return True
# guess_my_number(42)

import antigravity
# pip install pyftpdlib
# 我们可以把python的文件打包，做成库的形式，然后import进来，是一种偷换概念和前提的一行代码。例如，为了与windows 传输文件，再Mac上临时搭个ftp：
# $ python -m pyftpdlib
# 这当然要依赖pyftpdlib 这个库了，机器上没有，pip install pyftpdlib 就可以了。
# 如果一行代码中允许分号存在，那就只是牺牲可读性而已了，那就基本上无所不能。
# 在连网的前提下，获取公网IP地址
# python -c "import socket; sock=socket.create_connection(('ns1.dnspod.net',6666)); print sock.recv(16); sock.close()"
# 一行代码就可以轻易写个小游戏了，来模拟一下golf击球。
# python -c "import math as m;a,v=eval(input());[print('%03d'%x+' '*m.floor(0.5+x*m.tan(a)-x*x/(v*m.cos(a)))+'o') for x in range(102)]"
# 输入角度和力量大小如（0.8,80)，就能得到一条字符描画的抛物线了。
# 增加上while 等语句，画一个没完没了的
# python -c "while 1:import random;print(random.choice('╱╲'), end='')"

