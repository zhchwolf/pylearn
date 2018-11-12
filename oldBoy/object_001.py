import re
#
# s= ' 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# print(re.search('\([^()]+\)',s).group())
#
# class f0:
#     def __init__(self):
#         print('f0.init')
#     def foo(self):
#         print('f0_foo')
#
# class f1(f0):
#     print('f1.print')
#     def foo(self):
#         print('f1_foo')
#
# class f3(f1):
#     print('f3.print')
#     def foo(self):
#         print('f3_foo')
# class f2(f1):
#
#     def __init__(self,current_page):
#         try:
#             p=int(current_page)
#         except:
#             p = 1
#         self.page = p
#
#     def foo(self):
#         print('f2_foo')
#     @property
#     def start(self):
#         val = (self.page-1)*10
#         return val
#     @property
#     def end(self):
#         val = self.page*10
#         return val
#
# class s(f2,f3):
#     def __init__(self):
#         print('s.init')
#
# son = s()
# son.foo()
#
#
# pl = []
# for i in range(10000):
#     pl.append(i)
#
# while True:
#     p = input('Please input your page number:')
#     if p == 'q':
#         break
#     p001 = f2(p)
#     print(p001.start,p001.end)
#     print(pl[p001.start:p001.end])
#
#
# # import  socketserver
# # obj = socketserver.ThreadingTCPServer(1,2)
# # obj.serve_forever()
#
#
# class per:
#     category_name = 'Human'
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def eat(self,something):
#         print(something)
#
#     def walk(self):
#         print('walking')
#
#     def speak(self,say_content):
#         print(say_content)
#
# class peasent(per):
#     income_per_hour = 5000
#     cropland_list = 'cropland_01'
#     # def __init__(self,cropland_list):
#     #     self.cropland_name = cropland_list
#     #     self.income = 0
#
#     @classmethod
#     def cls_fun(cls):
#         print('cls function')
#
#     def tillage(self,corpland_name,is_till):
#         if is_till :
#             print('till in the %s' % self.cropland_list)
#             self.income = peasent.income_per_hour * 1
#             print('income increment:', self.income)
#         else:
#             print('no till, no income.')
#
#     @staticmethod
#     def sta(a1):
#         print(a1)
#
#     @property
#     def getname(self):
#         print(self.category_name)
#
#     @getname.setter
#     def getname(self,alias_name):
#         print('gege: ' ,alias_name)
#     @getname.deleter
#     def getname(self):
#         print('del something')
#
# # per01 = per('李四',21,'男')
# peasent01 = peasent('李四',21,'男')
#
# peasent.sta('23423')
# peasent.cls_fun()
# peasent01.tillage('cropland_01',True)
# peasent01.getname
# peasent01.getname = 'gege'
# del peasent01.getname


class Foo:
    def f1(self):
        return 123
    def f2(self,v):
        print(v)
    def f3(self):
        print('del obj')

    per = property(fget=f1,fset=f2,fdel=f3)

object = Foo()
ret = object.per
print(ret)
object.per = 4565
del object.per

class girl:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.__age)
        return self.__age

obj = girl('alex',18)
print(obj.name)
#print(obj.__age)
ret = obj.show()
print(ret)
