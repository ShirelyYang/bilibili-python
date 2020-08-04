# # 单继承
# class Animal:
#     def eat(self):
#         print("吃饭了")
#         pass
#
#     def drink(self):
#         print("喝喝喝")
#         pass
#
#
# class Dog(Animal):  # 继承Animal父类 此时Dog是子类
#     def wwj(self):
#         print("小狗汪汪叫")
#     pass
#
#
# class Cat(Animal):
#     def mmj(self):
#         print("小猫喵喵叫")
#     pass
# d1 = Dog()
# d1.eat()    # 具备了吃的行为    是继承了父类的行为
# c1 = Cat()
# c1.drink()

# 多继承


# class shenxian:
#     def fly(self):
#         print("神仙都会飞")
#         pass
#     pass
#
#
# class Monkey():
#     def chitao(self):
#         print("猴子喜欢吃桃")
#         pass
#     pass


# class Sunwukong(shenxian, Monkey):
#     pass
# swk = Sunwukong()
# swk.fly()
# swk.chitao()

# 重写父类方法
# 为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写父类或者完善父类的方法


# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#         pass
#
#     def bark(self):
#         print("汪汪叫……")
#         pass
#     pass
#
#
# class Corgi(Dog):
#     def __init__(self, name, color):     # 重写父类的方法
#         # 针对这种需求    我们就需要去调用父类的构造函数
#         Dog.__init__(self, name, color)     # 手动调用 调用父类的方法了  执行完毕就可以具备name，color这两个实例属性了
#         super().__init__(name, color)       # super是自动找到父类 进而调用方法， 假设继承了多个父类，那么会按照顺序逐个去找 然后再调用
#         # 拓展其他的属性
#         self.height = 90
#         self.weight = 20
#         pass
#
#     def bark(self):     # 属于重写父类的方法
#         super().bark()   # 调用父类的方法
#         print("叫的跟神一样……")
#     pass
#
#     def __str__(self):
#         return "{}的颜色是{} 他的身高是{}cm 体重是{}kg" .format(self.name, self.color, self.height, self.weight)
#
# kj = Corgi("柯基犬", "红色")
# kj.bark()
# print(kj)

# 多态

# class Animal:
#     """
#     父类【基类】
#     """
#     def say_who(self):
#         print("我是一个动物……")
#         pass
#     pass
#
#
# class Duck(Animal):
#     """
#     子类【派生类】
#     """
#     def say_who(self):
#         print("我是一只漂亮的鸭子")
#         pass
#     pass
#
#
# class Dog(Animal):
#     def say_who(self):
#         print("我是一只哈巴狗……")
#         pass
#     pass
#
#
# class Cat(Animal):
#     def say_who(self):
#         print("我是一只小猫 喵喵喵喵……")
#         pass
#     pass
#
#
# def commonInvoke(obj):
#     """
#     统一调用的方法
#     :param obj: 对象的实例
#     :return:
#     """
#     obj.say_who()
#     pass
#
# # duck = Duck()
# # duck.say_who()
# # dog = Dog()
# # dog.say_who()
# listObj = [Duck(), Dog(), Cat()]
# for item in listObj:
#     commonInvoke(item)
#     pass


# 属性： 类属性和实例属性
# 类属性 就是类对象所拥有的属性


# class Student:
#     name = "黎明"     # 属于类属性 就是student类对象所拥有的
#
#     def __init__(self, age):
#         self.age = age      # 实例属性
#         pass
#     pass
#
# lm = Student(18)
# print(lm.name)  # 通过实例对象去访问类属性
# print(lm.age)
# print("--------------------------通过类对象去访问name--------------------------------------")
# print(Student.name)
# # 小结
# # 类属性是可以 被类对象和实例对象共同访问使用的
# # 实例属性只能由实例对象所访问

# 类方法和静态方法
# class People:
#     country = "China"
#
#     @classmethod    # 类方法   用classmethod 来进行修饰
#     def getCountry(cls):
#         return cls.country      # 访问类属性
#         pass
#
#     @classmethod
#     def changeCountry(cls, data):
#         cls.country = data      # 修改类属性的值   在类方法中
#         pass
#
#     @staticmethod
#     def getData():
#         return People.country
#     pass
# print(People.getData())
# p = People()
# print(p.getData())  # 注意 一般情况下 我们不会通过实例对象去访问静态方法
# print(People.getCountry())
# p = People()
# print(p.getCountry())   # 通过实例对象去引用
# print("----------------修改之后-------------------------------")
# People.changeCountry("英国")
# print(People.getCountry())

# 为什么要使用静态方法
# 由于静态方法主要来存放逻辑性的代码， 本身和类以及实例对象没有交互，也就是说，在静态方法中，不会涉及到类中方法和属性的操作
# 优点：数据资源能够得到有效的充分利用


# demo 返回当前的系统时间
import time


class TimeTest:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        pass

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())

    @staticmethod
    def add(x, y):
        return x+y
    pass

print(TimeTest.showTime())
print(TimeTest.add(10, 56))