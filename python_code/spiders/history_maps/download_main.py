#-*-coding:utf-8-*-

#urllib模块提供了读取Web页面数据的接口
import urllib.request,urllib.parse
#re模块主要包含了正则表达式
import re,os
#定义一个getHtml()函数
def getHtml(url):
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
    # 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    # request = urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(url)  #urllib.urlopen()方法用于打开一个URL地址
    html = page.read().decode('gbk')  #read()方法用于读取URL上的数据
    return html

def getSubUrl(html):
    reg = r'class="" href="(.+?\.html)"'    #正则表达式，得到图片地址
    #print(reg)
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    imglist = list(set(re.findall(imgre,html)))     #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    htmllist = ['http://map.ps123.net'+x for x in imglist]
    return htmllist

def generalurl(url,num):
    finalurl = url + '/china/' + str(num) + '.html'
    return finalurl
#http://map.ps123.net/china/4907.html
def getImg(pagestart,pageend):
    for pagenum in range(pagestart,pageend):
        url = generalurl('http://map.ps123.net',pagenum)
        reg = r'src="(.+?\.jpg)"'    #正则表达式，得到图片地址
        refolder = r'<title>(.*)</title>'
        #print(reg)
        imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
        #print(url)
        htmlcontent=getHtml(url)
        imglist = re.findall(imgre,htmlcontent)     #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
        title_all = re.search(refolder,htmlcontent).group(1)
        isfind1 = title_all.find('：')
        isfind2 = title_all.count('_')
        if isfind1 == 0:
            imgfolder = title_all[0:title_all.index('：')]
            imgname =  title_all[title_all.index('：')+1:title_all.index('_')]
        elif isfind2==1:
            imgname = title_all[:title_all.index('_')]
            imgfolder = title_all[title_all.index('_')+1:-2]
        else:
            continue
        filefolder = os.curdir + '/output/' + imgfolder
        filepath = filefolder + '/' + imgname + '.jpg'
        if os.path.exists(filefolder) is False:
            os.makedirs(filefolder)
        # print(title_all)
        # print(filepath)
        x = 0
        for img in imglist:    #把筛选的图片地址通过for循环遍历并保存到本地
            imgurl='http://map.ps123.net'+ img
            print(imgurl)
            urllib.request.urlretrieve(imgurl,filepath)       #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
            print('Save picture ' + filepath)
            x+=1

#html = getHtml("http://map.ps123.net/china/477.html")
#hlist=getSubUrl(html)
print (getImg(1,50))
