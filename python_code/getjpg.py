# -*- coding = utf-8 -*-
import re
import urllib.request
import urllib.parse
import sys
import importlib

importlib.reload(sys)

def getHtml(url):
    page = urllib.request.urlopen(url)
    ahtml = page.read()
    #dhtml = ahtml.decode().replace('\&quot;','')
    #print (ahtml)
    return ahtml
def  getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    print (imgre)
    imglist = re.findall(imgre,urllib.parse.quote(html))
    print (imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl ,'%s.jpg' % x)
        x += 1

html = getHtml('http://tieba.baidu.com/p/3691190214')
print (getImg(html))
