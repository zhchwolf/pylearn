import urllib
req = urllib.Request('http://www.baidu.com')
response = urllib.urlopen(req)
the_page = response.read()
print (the_page)
