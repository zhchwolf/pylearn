__metaclass__=type

import random
class person :
	def __init__(self):
		self.name="武将"
		self.sex="男"
	def setAttr(self):
		self.attack = random.randint(80,100)
		self.intelligence = random.randint(50,80)
		self.defence = random.randint(50,90)
		self.speed = random.randint(50,100)
	def getAttr(self):
		self.attribute = (self.attack,self.intelligence,self.defence,self.speed)
		return self.attribute


p1 = person()
p1.setAttr()
a1 = p1.getAttr()
print (a1)

