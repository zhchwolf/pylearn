__metaclass__=type
class FooBar:
	def __init__(self):
		self.somevar=42

f = FooBar()
f.somevar
print (f.somevar)

class FooBarWithVar:
	def __init__(self,value=42):
		self.somevar=value

g=FooBarWithVar(101)
print(g.somevar)

class Bird:
	"""docstring for ClassName"""
	def __init__(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print ("Awoooooo")
			self.hungry=False
		else:
			print ('No, thanks!!')

class SongBird(Bird):
	"""docstring for ClassName"""
	def __init__(self):
		#call supper class
		Bird.__init__(self)
		self.sound='Squawk!'
	def sing(self):
		print (self.sound)

sb = SongBird()
print (sb.sing())

#__len__(self)
#__getitem__(self,key)
#__setitem__(self,key,value)
#__delitem__(self,key)

def checkIndex(key):
	if not isinstance(key,(int)):raise TypeError
	if key<0:raise IndexError

class ArithmeticSequence:
	def __init__(self,start=0,step=1):
		self.start=start
		self.step=step
		self.changed={}
	def  __getitem__(self,key):
		checkIndex(key)
		try:
			return self.changed[key]
		except KeyError:
			return self.start+key*self.step
	def __setitem__(self,key,value):
		checkIndex(key)
		self.changed[key]=value

a=ArithmeticSequence(1,2)
a[4]=2
print(a[4])

class CounterList(list):
	"""docstring for CountList"""
	def __init__(self, *agrs):
		super(CounterList, self).__init__(*agrs)
		self.counter = 0
	def __getitem__(self,index):
		self.counter += 1
		return super(CounterList, self).__getitem__(index)

c1 = CounterList(range(10))
print (c1)
del c1[3:6]
print (c1.counter)

class Rectangle:
	"""docstring for Rectangle"""
	def __init__(self):
		self.width = 0
		self.heigh = 0
	def setSize(self,size):
		self.width,self.heigh=size
	def getSize(self):
		return self.width,self.heigh

r=Rectangle()
r.width = 10
r.heigh = 5
r1=r.getSize()

print(r1)
