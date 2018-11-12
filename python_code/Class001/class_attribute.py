__metaclass__=type
class Rectangle:
	"""docstring for Rectangle"""
	def __init__(self):
		self.width = 0
		self.heigh = 0
	def setSize(self,size):
		self.width,self.heigh=size
	def getSize(self):
		return self.width,self.heigh
	size=property(getSize,setSize)

class Rectangle2:
	"""docstring for Rectangle"""
	def __init__(self):
		self.width = 0
		self.heigh = 0
	def __setattr__(self,name,value):
		if name=='size':
			self.width,self.heigh=value
		else:
			self.__dict__[name]=value
	def __getattr__(self,name):
		if name=='size':
			return self.width,self.heigh
		else:
			raise AttributeError
		

r=Rectangle()
r.width=10
r.heigh=5
print (r.size)
r.size=(23,55)
print (r.size)

r2=Rectangle2()
r2.size=(100,200)
print (r2.size)
r2.a=12
print (r2.a)
#print (r2.abc)

class myClass:
	def smeth():
		print ("This is a static method")
	smeth = staticmethod(smeth)
	def cmeth(cls):
		print ('This is a class method of',cls)
	cmeth=classmethod(cmeth)

print (myClass.cmeth())

class myClass2:
	@staticmethod
	def smeth():
		print ("This is a static method")
	@classmethod
	def cmeth(cls):
		print ('This is a class method of',cls)

print (myClass.cmeth())
print (myClass2.cmeth())
