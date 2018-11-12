class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    __v = None

    @classmethod
    def getobj(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = Foo('alex',18)
            return cls.__v


obj1 = Foo.getobj()
print(obj1)
obj2 = Foo.getobj()
print(obj2)
obj3 = Foo.getobj()
print(obj3)
