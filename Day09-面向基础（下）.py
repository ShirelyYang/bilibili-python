# 属性私有化
# 使用私有属性的场景
# 1.把特定的一个属性隐藏起来    不想让类的外部进行直接调用
# 2.我想保护这个属性 不想让属性的值随意的改变
# 3.保护这个属性  不想让派生类【子类】去继承


# class Person:
#     def __init__(self):
#         self.__name = "李四"  # 加两个下划线，将此属性私有化    就不能在外部直接访问了，当然在类的内部是可以访问的
#         self.age = 30
#         pass
#
#     def __str__(self):
#         """
#         私有化的属性在内部可以使用 self.__name
#         :return:
#         """
#         return "{}的年龄是{}".format(self.__name, self.age)
#     pass
#
#
# class Student(Person):
#     def prinInfo(self):
#         print(self.__name)  # 在此访问父类中的私有属性  可以吗？
#     pass
#
# # xl = Person()
# # # print(xl.__name)  # 是通过类对象 在外部访问的 不能访问私有属性
# # print(xl)
#
# stu = Student()
# print(stu.__name)

# 小结：
# 1.私有化的【实例】属性 不能在外部直接的访问 可以在类的内部随意的使用
# 2.子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
# 3.在属性名的前面直接加两个下划线__ 就可以变为私有化了

# 私有化方法

# class Animal:
#     def __eat(self):
#         print("吃东西")
#         pass
#
#     def run(self):
#         self.__eat()    # 调用私有化的方法
#         print("飞快的跑")
#         pass
#     pass
#
#
# class Bird(Animal):
#     pass
#
# b1 = Bird()
# # print(b1.eat())
# # b1.eat()
# b1.run()

# Property属性


# class Person:
#     def __init__(self):
#         self.__age = 18
#         pass

    # def getAge(self):
    #     return self.__age
    #
    # def setAge(self, age):
    #     if age < 0:
    #         print("年龄不能小于0")
    #         pass
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    # # 定义一个类属性 实现通过直接访问属性的形式去访问私有的属性
    # age = property(getAge, setAge)
    # 实现方式2 通过装饰器的方式去声明
#     @property   # 用装饰器修饰 添加属性标志 提供一个getter方法
#     def age(self):
#         return self.__age
#
#     @age.setter   # 提供一个setter方法
#     def age(self, params):
#         if params < 0:
#             print("年龄不能小于0")
#             pass
#         else:
#             self.__age = params
#             pass
#     pass
#
# p1 = Person()
# print(p1.age)
# p1.age = 25
# print(p1.age)

# new 实例化


# class Animal:
#     def __init__(self):
#         self.color = "红色"
#         pass
#
#     # 在Python中，如果不重写 new 默认结构如下
#     def __new__(cls, *args, **kwargs):
#         return super.__new__(cls, *args, **kwargs)
#     pass
# tigger = Animal()   # 实例化的过程会自动调用 new 去创建实例
# 在新式类中 __new__ 才是真正的实例化的方法，为提供外壳制造出实例框架，然后调用该框架内的构造方法__init__进行操作
# 比喻建房子 __new__ 方法负责开发地皮 打地基 并将原料存放在工地，而__init__负责从工地取材料建造出地皮开发图纸规定的大楼 负责细节设计、建造，最终完成

# 单例模式  是一种常用的软件设计模式 目的：确保某一个类只有一个实例存在
# 如果希望在整个系统中 某个类只能出现一个实例的时候，那么这个单例对象就满足要求

# 创建一个单例对象 基于__new__去实现的【推荐的一种】


# class DataBaseClass(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance
#     pass
#
# db1 = DataBaseClass()
# print(id(db1))

# 异常处理
# except 在捕获错误异常的时候 是要根据具体的错误类型来捕获的
# 用一个块 可以捕获多个不同类型的异常
try:
    print(b)    # 捕获逻辑的代码
    pass
except NameError as msg:
    # 捕获到的错误 才会在这里执行
    print(msg)
    pass
