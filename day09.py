# 捕获异常
# def A(s):
#     return 10/int(s)
#     pass
#
#
# def B(s):
#     return A(s)*2
#
#
# def main():
#     try:
#         B("0")
#         pass
#     except Exception as msg:
#         print(msg)
#         pass
#     pass
#
#
# main()
# 不需要在每个可能出错的地方去捕获，只要在合适的层次去捕获错误就可以了 这样的话 就大大减少我们写 try----except的麻烦
# 异常的抛出机制
# 如果在运行时发生异常 解释器会查找相应的异常捕获类型
# 如果在当前函数里面没有找到的话 它会将异常传递给上层的调用函数，看能否处理
# 如果在最外层没有找到的话，解释器就会退出 程序down掉

# 自定义异常


# class ToolongMyException(Exception):
#     def __init__(self, length):
#         self.len = length
#         pass
#
#     def __str__(self):
#         return "您输入姓名数据长度是"+str(self.len)+",已经超过长度了……"
#     pass
#
#
# def name_Test():
#     name = input("请输入姓名：")
#     try:
#         if len(name) > 5:
#             raise ToolongMyException(len(name))
#         else:
#             print(name)
#             pass
#         pass
#     except ToolongMyException as result:
#         print(result)
#     finally:
#         print("执行完毕……")
#     pass
#
#
# name_Test()


# 动态添加属性和方法
# import types    # 添加方法的库
#
#
# def dymicMethod(self):
#     print("{}的体重是：{}kg，在{}读大学".format(self.name, self.weight, Student.school))
#     pass
#
#
# @classmethod
# def classTest(cls):
#     print("这是一个类方法")
#     pass
#
#
# @staticmethod
# def staticMethodTest():
#     print("这是一个静态方法")
#     pass
#
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass
#
#     def __str__(self):
#         return "{}今天{}岁了".format(self.name, self.age)
#     pass
#
#
# print("绑定类方法")
# Student.TestMethod = classTest
# Student.TestMethod()
# print("---------------绑定类方法执行结束----------------------------")
# print("绑定静态方法")
# Student.staticTest = staticMethodTest
# Student.staticTest()
# print("---------------绑定静态方法执行结束----------------------------")
# zyh = Student("张艳华", 20)
# zyh.weight = 50   # 动态添加
# zyh.printInfo = types.MethodType(dymicMethod, zyh)     # 动态的绑定方法
# zyh.TestMethod()
# print("----------------------------------------------------")
# # print(zyh)
# # print(zyh.weight)
# print("-----------------另外一个实例对象    张明----------------------------")
# zm = Student("张明", 20)
# print(zm)
# # print(zm.weight)
# print("-----------------类对象添加属性----------------------------")
# Student.school = "北京邮电大学"   # 动态添加类属性
# print(zm.school)
# print("-----------------动态添加实例方法----------------------------")
# zyh.printInfo()     # 执行动态绑定的方法


# slots属性限制


# class Student(object):
#     __slots__ = ("name", "age")
#
#     def __str__(self):
#         return "{}……{}".format(self.name, self.age)
#     pass
#
#
# xw = Student()
# xw.name = "小王"
# xw.age = 20
# # print(xw.__dict__)      # 所有可以用的属性都在这里存储    不足的地方就是占用的内存空间大
# # 可以看到 在定义了 slots变量之后 student类的实例已经不能随意创建   不在__slots__定义的属性了
# # 同时还可以看到实例当中也不再有__dict__
# # print(xw)
#
# # 在继承关系当中使用     __slots__
# # 子类未声明 __slots__时，那么是不会继承父类的__slots__,此时子类是可以随意的属性赋值的
# # 子类声明了 __slots__时，继承父类的__slots__，也就是子类__slots__的范围是为 其自身+父类
#
#
# class subStudent(Student):
#     __slots__ = ("gender")
#     pass
#
#
# ln = subStudent()
# ln.gender = "男"
# # ln.pro = "网络工程"
# ln.name = "李楠"
# print(ln.name, ln.gender

# Property属性函数


class Person:
    def __init__(self):
        self.__age = 18     # 定义一个私有化属性，属性名字前加两个__ 下划线

    # def get_age(self):      # 访问私有实例属性
    #     return self.__age
    #
    # def set_age(self, age):     # 修改私有实例属性
    #     if self.__age < 0:
    #         print("年龄不能小于0")
    #         pass
    #     else:
    #         self.__age = age
    #     pass

    # 定义一个类属性 实现通过直接访问属性的形式去访问私有的属性
    # age = property(get_age, set_age)

    # 实现方式2 通过装饰器的方式去声明
    @property   # 用装饰器修饰，添加属性标志 提供一个getter方法
    def age(self):
        return self.__age

    @age.setter     # 提供一个setter方法
    def age(self, params):
        if params < 0:
            print("年龄不能小于0")
            pass
        else:
            self.__age = params
    pass


# p1 = Person()
# print(p1.age)
# p1.age = 25
# print(p1.age)


# new 实例化


# class Animai:
#     def __init__(self):
#         self.color = "red"
#         pass
#
#     # 在python当中，如果不重写 __new__ 默认结构如下：
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#     pass
#
#
# tigger = Animai()   # 实例化的过程会自动调用 new 去创建实例
# 在新式类中 __new__ 才是这正的实例化方法，为类提供外壳制造出实例框架，然后调用该框架内的构造方法 __init__ 进行丰满操作
# 比喻建房子， __new__ 方法负责开发地皮、打地基，并将原料存放在工地，而__init__负责从工地取材料建造出地皮开发图纸规定的大楼 ，负责细节设计、建造，最终完成


# 单例模式  是一种常用的软件设计模式 目的：确保某一个类只有一个实例存在
# 如果希望在整个系统中 某个类只能出现一个实例的时候，那么这个单例对象就能满足要求
# 创建一个单例对象  基于__new__去实现的【推荐的一种】


# class DataBaseClass(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):      # 如果不存在就开始创建
#             cls._instance = object().__new__(cls, *args, **kwargs)
#         return cls._instance
#     pass
#
#
# class DBopsingle(DataBaseClass):
#     pass
#
#
# db1 = DBopsingle()
# print(id(db1))
# db2 = DBopsingle()
# print(id(db2))
# db3 = DBopsingle()
# print(id(db3))


# 类属性和实例属性
# 类属性就是类对象所拥有的的属性


# class Student:
#     name = "Amy"    # 属于类属性 就是student类对象所拥有的
#
#     def __init__(self, age):
#         self.age = age  # 实例属性
#         pass
#     pass
#
#
# amy = Student(3)
# print(amy.name)     # 通过实例对象去访问类属性
# print(amy.age)
# print("--------------通过类对象 student  去访问name------------------------------")
# print(Student.name)
# print(Student.age)
# 小结
# 类属性是可以 被类对象和实例对象共同访问使用的
# 实例属性只能有实例对象所访问


# 私有化方法
class Animal:
    def __eat(self):
        print("吃东西")
        pass

    def run(self):
        self.__eat()        # 调用私有化方法
        print("飞快的跑")
        pass
    pass


class Bird(Animal):
    pass


b1 = Bird()
# print(b1.eat())
b1.run()
