# 定义一个Animal类
# （1）使用__init__初始化方法为对象添加初始属性，如颜色、名字、年龄
# （2）定义动物方法，如run、eat等方法。如调用eat方法时打印xx正在吃东西
# （3）定义一个__str__方法，输出对象的所有属性


class Animal:
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age
        pass

    def run(self):
        print("%s正在奔跑……" % self.name)
        pass

    def eat(self, food):
        print("%s正在吃%s……" % (self.name, food))
        pass

    def __str__(self):
        """
        输出对象的属性

        :return:
        """
        return "该动物的名字叫%s，年龄%s，颜色%s。" % (self.name, self.age, self.color)
    pass
cat = Animal("白色", "咪咪", "2岁")
cat.run()
cat.eat("小鱼干")
print(cat)