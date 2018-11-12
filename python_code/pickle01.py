try:
    import cpickle as pickle
except:
    import pickle
import pprint
import os

info = [1,2,3,'abc','iplaypython']
print ('source data:')
pprint.pprint(info)

data1 = pickle.dumps(info)
data2 = pickle.loads(data1)

print('序列化：%r' %data1)
print('反序列化：%r' %data2)

data3 = {'a':[1,2.0,3,4+6j],
'b':('string',u'Unicode string'),
'c': None}

f1 = file('temp.pkl','wb')
pickle.dump(data1,f1,True)
pickle.dump(data2,f1,True)
pickle.dump(data3,f1,True)
f1.close()

f2 = file('temp.pkl','rb')
a2 = pickle.load(f2)
print(a2)

selfref_list = [1,2,5]
selfref_list.append(selfref_list)

