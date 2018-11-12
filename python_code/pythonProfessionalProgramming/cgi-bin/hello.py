#!/usr/bin/env python
import sys
import 

print(sys.getdefaultencoding())
print("200 OK")
print("Content-Type: text/plain")
print("")
print("Hello CGI!")

#python -m CGIHTTPServer

a =b'\xF0\x9F\x98\x8A\x0A'
b ='鶸'
c=a.decode('utf8')
print(b.__class__)
print(a.__class__)
print(a)
print(c) # smile face can not display here.
print(isinstance(a,str))

#python2
u = u'中文' #显示指定unicode类型对象u
str = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
#u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
#python3
u1 = '中文' #指定字符串类型对象u
str10 = u1.encode('gb2312') #以gb2312编码对u1进行编码，获得bytes类型对象str
u10 = str10.decode('gb2312')#以gb2312编码对字符串str10进行解码，获得字符串类型对象u1
#u20 = str10.decode('utf-8')#如果以utf-8的编码对str10进行解码得到的结果，将无法还原原来的字符串内容
print(str10)
print(u10)
