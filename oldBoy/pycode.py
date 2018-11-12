s = 'hello' + u'似的'
print(s)
print(type(s))

u = '愤怒'
b1 = u.encode('utf8')
print(b1,type(b1))
print(type(u))

import  json

print(json.dumps(u))