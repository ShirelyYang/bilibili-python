# 请编写代码，验证self就是实例本身
class Person:
    def weight(self):
        print("self=%s" % id(self))
        pass
    pass
lm = Person()
lm.weight()
print(id(lm))