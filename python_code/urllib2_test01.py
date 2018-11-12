#!/usr/bin python3
# -*- coding:utf-8 -*-
import urllib.request
import http

import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
# response = urllib.request.urlopen('http://www.baidu.com/')
# html = response.read()

location_list = urllib.request.urlopen('http://i.tq121.com.cn/j/wap2016/news/city_search_data.js')
data_list = location_list.read()
print(data_list.decode('utf-8'))
req = urllib.request.urlopen('http://m.weather.com.cn/weather/101190401.shtml')
content = req.read()
#print(content)


w = open('d:\\horace\\install_hadoop.txt','a')
w.write('write some words.')
w.close()

f = open('d:\\horace\\install_hadoop.txt')
data = f.read()
print(data)
f.close()

