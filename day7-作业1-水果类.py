# 定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象 并分别添加上颜色属性
class Fruit:
    def __init__(self, name, co):
        self.name = name
        self.color = co
        pass

    def __str__(self):
        return "%s 的颜色是：%s" % (self.name, self.color)
    pass
apple = Fruit("apple", "Green")
orange = Fruit("orange", "Orange")
melon = Fruit("melon", "Red")
print(apple)
print("*" * 40)
print(orange)
print("*" * 40)
print(melon)