# 创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法,给类绑定一个类属性colour,给类绑定一个类方法打印字符串'ok'。
import types


def run(self, name):
    self.name = name
    print("{}在飞快的跑".format(self.name))


class Animal:
    pass

@classmethod
def info(cls):
    print("OK")
    pass


Animal.color = "白色"
Animal.info = info
cat = Animal()
cat.run = types.MethodType(run, cat)    # 动态绑定
cat.run("喵喵")
print(Animal.color)
Animal.info()
