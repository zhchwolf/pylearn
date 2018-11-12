class per:
    category_name = 'Human'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self,something):
        print(something)

    def walk(self):
        print('walking')

    def speak(self,say_content):
        print(say_content)

class peasent(per):
    income_per_hour = 5000
    cropland_list = 'cropland_01'
    # def __init__(self,cropland_list):
    #     self.cropland_name = cropland_list
    #     self.income = 0

    @classmethod
    def cls_fun(cls):
        print('cls function')

    def tillage(self,corpland_name,is_till):
        if is_till :
            print('till in the %s' % self.cropland_list)
            self.income = peasent.income_per_hour * 1
            print('income increment:', self.income)
        else:
            print('no till, no income.')

    @staticmethod
    def sta(a1):
        print(a1)

    @property
    def getname(self):
        print(self.category_name)

    @getname.setter
    def getname(self,alias_name):
        print('gege: ' ,alias_name)
    @getname.deleter
    def getname(self):
        print('del something')

# per01 = per('李四',21,'男')
peasent01 = peasent('李四',21,'男')

peasent.sta('23423')
peasent.cls_fun()
peasent01.tillage('cropland_01',True)
peasent01.getname
peasent01.getname = 'gege'
del peasent01.getname




