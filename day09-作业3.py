# 创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法。利用property属性给调用者提供  属性方式的调用获取和设置私有属性方法的方式。


class Animal:
    def __init__(self, variety, name):
        self.__variety = variety
        self.__name = name
        pass

    @property
    def variety(self):
        return self.__variety

    @property
    def name(self):
        return self.__name

    @variety.setter
    def variety(self, variety):
        self.__variety = variety
        pass

    @name.setter
    def name(self, name):
        self.__name = name
        pass

    def __call__(self, *args, **kwargs):
        print(self.__variety+"的名字是："+self.__name)
    pass


dog = Animal("小狗", "汪汪")
cat = Animal("小猫", "喵喵")
# print(dog.variety, dog.name)
# print(cat.variety, cat.name)
dog()   # 将实例对象以函数的形式去调用
cat.name = "咪咪"
cat()
