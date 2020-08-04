# 编写一段代码以完成下面的要求
# 定义一个Person类，类中要有初始化方法，方法中要有人的姓名，年龄两个私有属性
# 提供获取用户信息的函数
# 提供获取私有属性的方法
# 提供可以设置私有属性的方法
# 设置年龄的范围在（0-120）的方法，如果不在这个范围，不能设置成功


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        pass

    def __str__(self):
        return "{}的年龄是{}".format(self.__name, self.__age)

    # @property
    # def name(self):     # 函数的名称为私有属性的属性名
    #     return self.__name
    #
    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, params):
    #     if params not in range(0, 120):
    #         print("年龄不能大于120，小于0，设置不成功……")
    #         pass
    #     else:
    #         self.__age = params
    #         pass
    #     pass

    # def get_private(self):
    #     return self.__name, self.__age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age not in range(0, 120):
            print("年龄不能大于120，小于0，设置不成功……")
            pass
        else:
            self.__age = age
            pass

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    pass


p1 = Person("Amy", 3)
print(p1.name, p1.age)
p1.age = 22
print(p1.age)
