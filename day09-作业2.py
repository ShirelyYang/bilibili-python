# 请写一个单例模式


class DataBaseClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = object().__new__(cls, *args, **kwargs)
        return cls._instance
    pass


db1 = DataBaseClass()
print(id(db1))
db2 = DataBaseClass()
print(id(db2))
db3 = DataBaseClass()
print(id(db3))